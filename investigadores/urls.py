from django.urls import path
from investigadores.views import *

app_name = 'investigadores'

urlpatterns = [
    path('', investigadores_lista, name='lista'),
    path('fetch', Investigadores.as_view(), name='investigadores'),
]
