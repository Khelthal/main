from django.urls import path
from investigadores.views import investigadores_lista

app_name = 'investigadores'

urlpatterns = [
    path('', investigadores_lista, name='lista'),
]
