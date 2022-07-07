from .models import Team, Participant
import pandas as pd
import numpy as np


def load():
    """
    Loads the teams from the teams.csv file.
    """
    teams = pd.read_csv('teams/data/teams.csv')
    for index, row in teams.iterrows():
        team = Team(id=index, name='BLABLA'+str(index))
        team.save()
        for i in 'abc':
            if pd.notnull(row[i]):
                participant = Participant(stdid=int(row[i]), name='BLABLA'+str(index)+i, email='BLABLA@BLABLA.com', team=team)
                participant.save()
