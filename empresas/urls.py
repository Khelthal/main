from django.urls import path, include
from empresas.views import empresas_lista

app_name = "empresas"

urlpatterns = [
    path('', empresas_lista, name="lista"),
]
