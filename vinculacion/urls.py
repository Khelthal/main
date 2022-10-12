from django.urls import path, include
from .views import *

app_name = "vinculacion"

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('noticias', noticias, name='noticias'),
    path('noticias/<int:id>', noticia, name='noticia'),
    path('perfil', perfil, name='perfil'),

    # Acciones
    path('perfil/eliminar',UsuarioEliminar.as_view(),name='usuario_eliminar'),
    path('investigador/solicitud_ingreso/<int:institucion_id>', crearSolicitudIngreso, name='crear_solicitud_ingreso'),
    path('institucion_educativa/solicitud_ingreso/<int:investigador_id>/<int:respuesta>', contestarSolicitudIngreso, name='contestar_solicitud_ingreso'),
    path('institucion_educativa/miembros/eliminar/<int:investigador_id>', miembroEliminar, name='miembro_eliminar'),
    
    # Formularios
    path('formularios/investigador', InvestigadorSolicitud.as_view(), name='investigador_form'),
    path('formularios/investigador/actualizar', InvestigadorActualizar.as_view(), name='investigador_actualizar'),
    path('formularios/solicitudTrabajo/<int:investigador_id>', solicitudTrabajoNueva, name='solicitud_trabajo_nueva'),

    path('formularios/empresa', EmpresaSolicitud.as_view(), name='empresa_form'),
    path('formularios/empresa/actualizar', EmpresaActualizar.as_view(), name='empresa_actualizar'),

    path('formularios/institucion_educativa', InstitucionEducativaSolicitud.as_view(), name='institucion_educativa_form'),
    path('formularios/institucion_educativa/actualizar', InstitucionEducativaActualizar.as_view(), name='institucion_educativa_actualizar'),

    path('formularios/investigacion', InvestigacionNuevo.as_view(), name='investigacion_nuevo'),
    
    # Listas
    path('investigadores', investigadores_lista, name='investigadores_lista'),
    path('perfil/investigaciones', InvestigadorInvestigaciones.as_view(),name='investigaciones_lista'),
    path('perfil/investigaciones/fetch', investigaciones_google,name='investigaciones_fetch'),
    path('perfil/solicitudes_trabajo', InvestigadorSolicitudesTrabajo.as_view(),name='solicitudes_trabajo_lista'),
    path('empresas', empresas_lista, name="empresas_lista"),
    path('instituciones_educativas/', instituciones_educativas_lista, name="instituciones_educativas_lista"),
    path('institucion_educativa/solicitud_ingreso', solicitudIngresoLista, name="institucion_educativa_solicitudes"),
    path('institucion_educativa/miembros', miembrosLista, name="institucion_educativa_miembros"),

    # Perfiles públicos
    path('investigadores/<int:investigador_id>', investigador_perfil, name='investigador_perfil'),
]
