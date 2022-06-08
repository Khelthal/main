from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    #Usuarios
    path('usuarios/', include('usuarios.urls')),
]
