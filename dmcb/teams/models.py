from django.db import models

from questions.models import Question

class Team(models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)
    burned_questions = models.ManyToManyField(Question, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Participant(models.Model):
    stdid = models.CharField(max_length=20, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
