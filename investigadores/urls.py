from django.urls import path
from investigadores.views import *

app_name = 'investigadores'

urlpatterns = [
    path('', lista, name='lista'),
    path('nuevo', NuevoInvestigadorView.as_view(), name='nuevo_investigador'),
    path('eliminar/<int:pk>', EliminarInvestigadorView.as_view(), name='eliminar_investigador'),
    path('editar/<int:id>', editar_investigador, name='editar_investigador'),
]
