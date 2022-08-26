from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from administracion.user_tests import user_is_staff_member
from administracion.views import *
from django.contrib.auth.views import LogoutView

app_name = 'administracion'

urlpatterns = [
    path('', user_passes_test(user_is_staff_member)(dashboard), name='dashboard'),
    path('aprobar_perfil/<int:pk>', user_passes_test(user_is_staff_member)(aprobar_perfil), name='aprobar_perfil'),
    path('salir', LogoutView.as_view(), name='logout'),

    #Usuarios
    path('usuarios/lista', user_passes_test(user_is_staff_member)(UsuarioLista.as_view()), name='usuarios_lista'),
    path('usuarios/nuevo', user_passes_test(user_is_staff_member)(UsuarioNuevo.as_view()), name='usuarios_nuevo'),
    path('usuarios/editar/<int:pk>', user_passes_test(user_is_staff_member)(UsuarioEditar.as_view()), name='usuarios_editar'),
    path('usuarios/eliminar/<int:pk>', user_passes_test(user_is_staff_member)(UsuarioEliminar.as_view()), name='usuarios_eliminar'),
    
    #Investigadores
    path('investigadores/lista', user_passes_test(user_is_staff_member)(InvestigadorLista.as_view()), name='investigadores_lista'),
    path('investigadores/solicitud', user_passes_test(user_is_staff_member)(InvestigadorSolicitud.as_view()), name='investigadores_solicitud'),
    path('investigadores/nuevo', user_passes_test(user_is_staff_member)(InvestigadorNuevo.as_view()), name='investigadores_nuevo'),
    path('investigadores/editar/<int:pk>', user_passes_test(user_is_staff_member)(InvestigadorEditar.as_view()), name='investigadores_editar'),
    path('investigadores/eliminar/<int:pk>', user_passes_test(user_is_staff_member)(InvestigadorEliminar.as_view()), name='investigadores_eliminar'),
    
    #Empresas
    path('empresas/lista', user_passes_test(user_is_staff_member)(EmpresaLista.as_view()), name='empresas_lista'),
    path('empresas/solicitud', user_passes_test(user_is_staff_member)(EmpresaSolicitud.as_view()), name='empresas_solicitud'),
    path('empresas/nuevo', user_passes_test(user_is_staff_member)(EmpresaNuevo.as_view()), name='empresas_nuevo'),
    path('empresas/editar/<int:pk>', user_passes_test(user_is_staff_member)(EmpresaEditar.as_view()), name='empresas_editar'),
    path('empresas/eliminar/<int:pk>', user_passes_test(user_is_staff_member)(EmpresaEliminar.as_view()), name='empresas_eliminar'),
    
    #Instituciones Educativas
    path('instituciones_educativas/lista', user_passes_test(user_is_staff_member)(InstitucionEducativaLista.as_view()), name='instituciones_educativas_lista'),
    path('instituciones_educativas/solicitud', user_passes_test(user_is_staff_member)(InstitucionEducativaSolicitud.as_view()), name='instituciones_educativas_solicitud'),
    path('instituciones_educativas/nuevo', user_passes_test(user_is_staff_member)(InstitucionEducativaNuevo.as_view()), name='instituciones_educativas_nuevo'),
    path('instituciones_educativas/editar/<int:pk>', user_passes_test(user_is_staff_member)(InstitucionEducativaEditar.as_view()), name='instituciones_educativas_editar'),
    path('instituciones_educativas/eliminar/<int:pk>', user_passes_test(user_is_staff_member)(InstitucionEducativaEliminar.as_view()), name='instituciones_educativas_eliminar'),
    
    #Categorias
    path('categorias/lista', user_passes_test(user_is_staff_member)(CategoriaLista.as_view()), name='categorias_lista'),
    path('categorias/nuevo', user_passes_test(user_is_staff_member)(CategoriaNuevo.as_view()), name='categorias_nuevo'),
    path('categorias/editar/<int:pk>', user_passes_test(user_is_staff_member)(CategoriaEditar.as_view()), name='categorias_editar'),
    path('categorias/eliminar/<int:pk>', user_passes_test(user_is_staff_member)(CategoriaEliminar.as_view()), name='categorias_eliminar'),
    
    #Investigaciones
    path('investigaciones/lista', user_passes_test(user_is_staff_member)(InvestigacionLista.as_view()), name='investigaciones_lista'),
    path('investigaciones/nuevo', user_passes_test(user_is_staff_member)(InvestigacionNuevo.as_view()), name='investigaciones_nuevo'),
    path('investigaciones/editar/<int:pk>', user_passes_test(user_is_staff_member)(InvestigacionEditar.as_view()), name='investigaciones_editar'),
    path('investigaciones/eliminar/<int:pk>', user_passes_test(user_is_staff_member)(InvestigacionEliminar.as_view()), name='investigaciones_eliminar'),

    #Noticias
    path('noticias/lista', user_passes_test(user_is_staff_member)(NoticiaLista.as_view()), name='noticias_lista'),
    path('noticias/nuevo', user_passes_test(user_is_staff_member)(NoticiaNueva.as_view()), name='noticias_nuevo'),
    path('noticias/editar/<int:pk>', user_passes_test(user_is_staff_member)(NoticiaEditar.as_view()), name='noticias_editar'),
    path('noticias/eliminar/<int:pk>', user_passes_test(user_is_staff_member)(NoticiaEliminar.as_view()), name='noticias_eliminar'),
]
