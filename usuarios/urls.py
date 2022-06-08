from django.urls import path
from .views import *

app_name = 'usuarios'

urlpatterns = [
    path('login', login, name='login'),
    path('registrar', registrar, name='registrar'),
]
