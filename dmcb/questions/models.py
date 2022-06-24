from django.db import models

# Create your models here.

class Participant(models.Model):
    stdid = models.CharField(max_length=20, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE)
class Team(models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)
    burned_questions = models.ManyToManyField('questions.Question', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name