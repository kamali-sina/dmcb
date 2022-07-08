from django.db.models import Max

import pandas as pd

from .models import Team

def save():
    data = [(i.id, i.balance) for i in Team.objects.all().order_by('balance')]
    results = pd.DataFrame(data, columns=['id', 'balance'])
    results.to_csv('teams/data/results.csv', index=False)