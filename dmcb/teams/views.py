from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Team, Participant
from questions.models import Question

from .forms import *

from questions.consts import *

class BuyView(View):
    def get(self, request):
        form = BuyForm()
        context = {
            'form': form,
        }
        return render(request, 'form.html', context)

    def handle_buy(self, team, form):
        message = 'Success'
        question_id = form.cleaned_data['question_id']
        if Question.objects.filter(question_id=question_id).exists():
            question = Question.objects.get(question_id=question_id)
        else:
            question = Question(question_id=question_id, difficulty=question_id[0])
            question.save()
        if team.balance >= INITIAL_PRICES[question.difficulty]:
            team.balance -= INITIAL_PRICES[question.difficulty]
            team.save()
        else:
            message = 'Insufficent balance'
        return message
    
    def post(self, request):
        form = BuyForm(request.POST)
        message = 'Not Valid'
        if form.is_valid():
            stdid = form.cleaned_data['stdid']
            participant = Participant.objects.get(stdid=stdid)
            team = participant.team
            message = self.handle_buy(team, form)
        context = {
            'message': message
        }
        return render(request, 'result.html', context)

class SellView(View):
    def get(self, request):
        form = SellForm()
        context = {
            'form': form,
        }
        return render(request, 'form.html', context)

    def calculate_payout(self, question):
        return int(INITIAL_PRICES[question.difficulty] * SELL_COEF)


    def handle_sell(self, team, form):
        question_id = form.cleaned_data['question_id']
        if Question.objects.filter(question_id=question_id).exists():
            question = Question.objects.get(question_id=question_id)
        else:
            question = Question(question_id=question_id, difficulty=question_id[0])
            question.save()
        team.balance += self.calculate_payout(question)
        team.burned_questions.add(question)
        question.sell_count += 1
        question.save()
        team.save()
        return 'Success'
    
    def post(self, request):
        form = SellForm(request.POST)
        message = 'Not Valid'
        if form.is_valid():
            stdid = form.cleaned_data['stdid']
            participant = Participant.objects.get(stdid=stdid)
            team = participant.team
            message = self.handle_sell(team, form)
        context = {
            'message': message
        }
        return render(request, 'result.html', context)

class SolveView(View):
    def get(self, request):
        form = SolveForm()
        context = {
            'form': form,
        }
        return render(request, 'form.html', context)

    def calculate_payout(self, question):
        coef = COEFS[question.difficulty]
        coef -= question.solve_count * SOLVE_DELTA
        coef += question.sell_count * SELL_DELTA
        coef = max(MIN_COEF, min(MAX_COEF, coef))
        return int(INITIAL_PRICES[question.difficulty] * coef)


    def handle_solve(self, team, form):
        message = 'Success'
        question_id = form.cleaned_data['question_id']
        if Question.objects.filter(question_id=question_id).exists():
            question = Question.objects.get(question_id=question_id)
        else:
            question = Question(question_id=question_id, difficulty=question_id[0])
            question.save()
        if not question in team.burned_questions.all():
            team.balance += self.calculate_payout(question)
            question.solve_count += 1
            team.burned_questions.add(question)
            question.save()
            team.save()
        else:
            message = 'Question already burned'
        return message
    
    def post(self, request):
        form = SolveForm(request.POST)
        message = 'Not Valid'
        if form.is_valid():
            stdid = form.cleaned_data['stdid']
            participant = Participant.objects.get(stdid=stdid)
            team = participant.team
            message = self.handle_solve(team, form)
        context = {
            'message': message
        }
        return render(request, 'result.html', context)

class TransferView(View):
    def get(self, request):
        form = TransferForm()
        context = {
            'form': form,
        }
        return render(request, 'form.html', context)

    def handle_transfer(self, from_team, to_team, form):
        message = 'Success'
        amount = form.cleaned_data['amount']
        if from_team.balance >= amount:
            from_team.balance -= amount
            to_team.balance += amount
            from_team.save()
            to_team.save()
        else:
            message = 'Insufficent balance'
        return message
    
    def post(self, request):
        form = TransferForm(request.POST)
        message = 'Not Valid'
        if form.is_valid():
            from_id = form.cleaned_data['from_id']
            from_participant = Participant.objects.get(stdid=from_id)
            from_team = from_participant.team
            to_id = form.cleaned_data['to_id']
            to_participant = Participant.objects.get(stdid=to_id)
            to_team = to_participant.team
            message = self.handle_transfer(from_team, to_team, form)
        context = {
            'message': message
        }
        return render(request, 'result.html', context)