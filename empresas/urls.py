from django.urls import path, include
from empresas.views import empresas_lista, Empresas

app_name = "empresas"

urlpatterns = [
    path('', empresas_lista, name="lista"),
    path('fetch', Empresas.as_view(), name="empresas_fetch"),
]
