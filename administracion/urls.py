from django.urls import path
from administracion.views import *

app_name = 'administracion'

urlpatterns = [
    path('', dashboard, name='dashboard'),

    #Usuarios
    path('usuarios/lista', usuarios_lista, name='usuarios_lista'),
    path('usuarios/nuevo', UsuarioNuevo.as_view(), name='usuarios_nuevo'),
    path('usuarios/editar/<int:pk>', UsuarioEditar.as_view(), name='usuarios_editar'),
    path('usuarios/eliminar/<int:pk>', UsuarioEliminar.as_view(), name='usuarios_eliminar'),
    
    #Investigadores
    path('investigadores/lista', investigadores_lista, name='investigadores_lista'),
    path('investigadores/nuevo', InvestigadorNuevo.as_view(), name='investigadores_nuevo'),
    path('investigadores/editar/<int:pk>', InvestigadorEditar.as_view(), name='investigadores_editar'),
    path('investigadores/eliminar/<int:pk>', InvestigadorEliminar.as_view(), name='investigadores_eliminar'),
    
    #Empresas
    path('empresas/lista', empresas_lista, name='empresas_lista'),
    path('empresas/nuevo', EmpresaNuevo.as_view(), name='empresas_nuevo'),
    path('empresas/editar/<int:pk>', EmpresaEditar.as_view(), name='empresas_editar'),
    path('empresas/eliminar/<int:pk>', EmpresaEliminar.as_view(), name='empresas_eliminar'),
    
    #Instituciones Educativas
    path('instituciones_educativas/lista', instituciones_educativas_lista, name='instituciones_educativas_lista'),
    path('instituciones_educativas/nuevo', InstitucionEducativaNuevo.as_view(), name='instituciones_educativas_nuevo'),
    path('instituciones_educativas/editar/<int:pk>', InstitucionEducativaEditar.as_view(), name='instituciones_educativas_editar'),
    path('instituciones_educativas/eliminar/<int:pk>', InstitucionEducativaEliminar.as_view(), name='instituciones_educativas_eliminar'),
    
    #Categorias
    path('categorias/lista', categorias_lista, name='categorias_lista'),
    path('categorias/nuevo', CategoriaNuevo.as_view(), name='categorias_nuevo'),
    path('categorias/editar/<int:pk>', CategoriaEditar.as_view(), name='categorias_editar'),
    path('categorias/eliminar/<int:pk>', CategoriaEliminar.as_view(), name='categorias_eliminar'),
]
