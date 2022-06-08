from django.urls import path
from investigadores.views import *

app_name = 'investigadores'

urlpatterns = [
    path('', lista, name='lista'),
]
