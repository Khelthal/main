from django.urls import path, include
from .views import *

app_name = "vinculacion"

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('empresas', empresas, name="empresas"),
    path('investigadores', investigadores, name='investigadores'),
    path('noticias', noticias, name='noticias'),
    path('noticia', noticia, name='noticia'),
]
