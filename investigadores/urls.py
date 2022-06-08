from django.urls import path
from investigadores.views import *

app_name = 'investigadores'

urlpatterns = [
    path('', lista, name='lista'),
    path('eliminar/<int:pk>', EliminarInvestigadorView.as_view(), name='eliminar-investigador'),
]
