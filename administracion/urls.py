from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from administracion.user_tests import user_is_staff_member
import administracion.views as views
from django.contrib.auth.views import LogoutView

app_name = 'administracion'

urlpatterns = [
    path('', user_passes_test(user_is_staff_member)
         (views.dashboard), name='dashboard'),
    path('aprobar_perfil/<int:pk>', user_passes_test(user_is_staff_member)
         (views.aprobar_perfil), name='aprobar_perfil'),
    path('salir', LogoutView.as_view(), name='logout'),

    # Usuarios
    path('usuarios/lista', user_passes_test(user_is_staff_member)
         (views.UsuarioLista.as_view()), name='usuarios_lista'),
    path('usuarios/nuevo', user_passes_test(user_is_staff_member)
         (views.UsuarioNuevo.as_view()), name='usuarios_nuevo'),
    path('usuarios/editar/<int:pk>', user_passes_test(user_is_staff_member)
         (views.UsuarioEditar.as_view()), name='usuarios_editar'),
    path('usuarios/eliminar/<int:pk>', user_passes_test(user_is_staff_member)
         (views.UsuarioEliminar.as_view()), name='usuarios_eliminar'),

    # Investigadores
    path('investigadores/lista', user_passes_test(user_is_staff_member)
         (views.InvestigadorLista.as_view()), name='investigadores_lista'),
    path(
          'investigadores/solicitud', user_passes_test(user_is_staff_member)
          (views.InvestigadorSolicitud.as_view()),
          name='investigadores_solicitud'),
    path(
          'investigadores/nuevo',
          user_passes_test(user_is_staff_member)
          (views.InvestigadorNuevo.as_view()),
          name='investigadores_nuevo'),
    path(
          'investigadores/editar/<int:pk>',
          user_passes_test(user_is_staff_member)
          (views.InvestigadorEditar.as_view()),
          name='investigadores_editar'),
    path(
          'investigadores/eliminar/<int:pk>',
          user_passes_test(user_is_staff_member)
          (views.InvestigadorEliminar.as_view()),
          name='investigadores_eliminar'),

    # Empresas
    path('empresas/lista', user_passes_test(user_is_staff_member)
         (views.EmpresaLista.as_view()), name='empresas_lista'),
    path('empresas/solicitud', user_passes_test(user_is_staff_member)
         (views.EmpresaSolicitud.as_view()), name='empresas_solicitud'),
    path('empresas/nuevo', user_passes_test(user_is_staff_member)
         (views.EmpresaNuevo.as_view()), name='empresas_nuevo'),
    path('empresas/editar/<int:pk>', user_passes_test(user_is_staff_member)
         (views.EmpresaEditar.as_view()), name='empresas_editar'),
    path('empresas/eliminar/<int:pk>', user_passes_test(user_is_staff_member)
         (views.EmpresaEliminar.as_view()), name='empresas_eliminar'),

    # Instituciones Educativas
    path(
          'instituciones_educativas/lista',
          user_passes_test(user_is_staff_member)
          (views.InstitucionEducativaLista.as_view()),
          name='instituciones_educativas_lista'),
    path(
          'instituciones_educativas/solicitud',
          user_passes_test(user_is_staff_member)
          (views.InstitucionEducativaSolicitud.as_view()),
          name='instituciones_educativas_solicitud'),
    path(
          'instituciones_educativas/nuevo',
          user_passes_test(user_is_staff_member)
          (views.InstitucionEducativaNuevo.as_view()),
          name='instituciones_educativas_nuevo'),
    path(
          'instituciones_educativas/editar/<int:pk>',
          user_passes_test(user_is_staff_member)
          (views.InstitucionEducativaEditar.as_view()),
          name='instituciones_educativas_editar'),
    path(
          'instituciones_educativas/eliminar/<int:pk>',
          user_passes_test(user_is_staff_member)
          (views.InstitucionEducativaEliminar.as_view()),
          name='instituciones_educativas_eliminar'),

    # Categorias
    path('categorias/lista', user_passes_test(user_is_staff_member)
         (views.CategoriaLista.as_view()), name='categorias_lista'),
    path('categorias/nuevo', user_passes_test(user_is_staff_member)
         (views.CategoriaNuevo.as_view()), name='categorias_nuevo'),
    path('categorias/editar/<int:pk>', user_passes_test(user_is_staff_member)
         (views.CategoriaEditar.as_view()), name='categorias_editar'),
    path('categorias/eliminar/<int:pk>', user_passes_test(user_is_staff_member)
         (views.CategoriaEliminar.as_view()), name='categorias_eliminar'),

    # Investigaciones
    path('investigaciones/lista', user_passes_test(user_is_staff_member)
         (views.InvestigacionLista.as_view()), name='investigaciones_lista'),
    path('investigaciones/nuevo', user_passes_test(user_is_staff_member)
         (views.InvestigacionNuevo.as_view()), name='investigaciones_nuevo'),
    path(
          'investigaciones/editar/<int:pk>',
          user_passes_test(user_is_staff_member)
          (views.InvestigacionEditar.as_view()),
          name='investigaciones_editar'),
    path(
          'investigaciones/eliminar/<int:pk>',
          user_passes_test(user_is_staff_member)
          (views.InvestigacionEliminar.as_view()),
          name='investigaciones_eliminar'),

    # Noticias
    path('noticias/lista', user_passes_test(user_is_staff_member)
         (views.NoticiaLista.as_view()), name='noticias_lista'),
    path('noticias/nuevo', user_passes_test(user_is_staff_member)
         (views.NoticiaNueva.as_view()), name='noticias_nuevo'),
    path('noticias/editar/<int:pk>', user_passes_test(user_is_staff_member)
         (views.NoticiaEditar.as_view()), name='noticias_editar'),
    path('noticias/eliminar/<int:pk>', user_passes_test(user_is_staff_member)
         (views.NoticiaEliminar.as_view()), name='noticias_eliminar'),
]
