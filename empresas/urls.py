from django.urls import path, include
from .views import *

app_name = "empresas"

urlpatterns = [
    path('empresas', empresas_lista, name="lista"),
]
