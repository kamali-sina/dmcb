from django.urls import path

from teams.views import *

urlpatterns = [
    path('buy/', BuyView.as_view(), name='buy'),
    path('sell/', SellView.as_view(), name='sell'),
    path('solve/', SolveView.as_view(), name='solve'),
    path('transfer/', TransferView.as_view(), name='transfer'),
]
