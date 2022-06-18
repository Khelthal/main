from django.urls import path
from administracion.views import *

app_name = 'administracion'

urlpatterns = [
    path('', dashboard, name='dashboard'),

    path('usuarios/lista', usuarios_lista, name='usuarios_lista'),
]
