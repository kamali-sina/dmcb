from django.db.models import Max

from .models import Team

def get_max():
    for i in Team.objects.all().order_by('balance'):
        print(i.id, i.balance)