from django.urls import path, include
from .views import *

app_name = "vinculacion"

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('investigadores', investigadores, name='investigadores'),
]
