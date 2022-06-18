from django.urls import path
from administracion.views import *

app_name = 'administracion'

urlpatterns = [
    path('', dashboard, name='dashboard'),

    #Usuarios
    path('usuarios/lista', usuarios_lista, name='usuarios_lista'),
    
    #Investigadores
    path('investigadores/lista', investigadores_lista, name='investigadores_lista'),
    path('investigadores/nuevo', InvestigadorNuevo.as_view(), name='investigadores_nuevo'),
    path('investigadores/editar/<int:pk>', InvestigadorEditar.as_view(), name='investigadores_editar'),
    path('investigadores/eliminar/<int:pk>', InvestigadorEliminar.as_view(), name='investigadores_eliminar'),
    
    #Empresas
    path('empresas/lista', empresas_lista, name='empresas_lista'),
    
    #Instituciones Educativas
    path('instituciones_educativas/lista', instituciones_educativas_lista, name='instituciones_educativas_lista'),
]
