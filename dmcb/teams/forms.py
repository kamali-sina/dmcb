from random import choices
from secrets import choice
from django import forms

class BuyForm(forms.Form):
    DIFFICULTY_CHOISES = (
        ("E", "Easy"),
        ("M", "Medium"),
        ("H", "Hard"),
        ("A", "Alan Turing"),
    )
    stdid = forms.CharField(max_length=20)
    question_difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOISES)

class SellForm(forms.Form):
    stdid = forms.CharField(max_length=20)
    question_id = forms.CharField(max_length=30)

class SolveForm(forms.Form):
    stdid = forms.CharField(max_length=20)
    question_id = forms.CharField(max_length=30)

class TransferForm(forms.Form):
    from_id = forms.CharField(max_length=20)
    to_id = forms.CharField(max_length=20)
    amount = forms.IntegerField()