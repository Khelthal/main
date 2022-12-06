from django.urls import path
from django.contrib.auth.decorators import login_required
import vinculacion.views as views

app_name = "vinculacion"

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('noticias', views.noticias, name='noticias'),
    path('noticias/<int:id>', views.noticia, name='noticia'),
    path('perfil', views.perfil, name='perfil'),

    # Acciones
    path(
        'perfil/eliminar', views.UsuarioEliminar.as_view(),
        name='usuario_eliminar'),
    path(
        'investigador/solicitud_ingreso/<int:institucion_id>',
        views.crearSolicitudIngreso, name='crear_solicitud_ingreso'),
    path(
        'institucion_educativa/solicitud_ingreso/' +
        '<int:investigador_id>/<int:respuesta>',
        views.contestarSolicitudIngreso, name='contestar_solicitud_ingreso'),
    path(
        'institucion_educativa/miembros/eliminar/<int:investigador_id>',
        views.miembroEliminar, name='miembro_eliminar'),

    # Formularios
    path(
        'formularios/investigador',
        login_required(views.InvestigadorSolicitud.as_view()),
        name='investigador_form'),
    path(
        'formularios/investigador/actualizar',
        views.InvestigadorActualizar.as_view(),
        name='investigador_actualizar'),
    path(
        'formularios/solicitud_trabajo/<int:investigador_id>',
        views.CrearSolicitudTrabajo.as_view(), name='solicitud_trabajo_nueva'),

    path(
        'formularios/empresa', login_required(
            views.EmpresaSolicitud.as_view()),
        name='empresa_form'),
    path(
        'formularios/empresa/actualizar',
        views.EmpresaActualizar.as_view(), name='empresa_actualizar'),

    path(
        'formularios/institucion_educativa',
        login_required(views.InstitucionEducativaSolicitud.as_view()),
        name='institucion_educativa_form'),
    path(
        'formularios/institucion_educativa/actualizar',
        views.InstitucionEducativaActualizar.as_view(),
        name='institucion_educativa_actualizar'),

    path(
        'formularios/investigacion',
        views.InvestigacionNuevo.as_view(), name='investigacion_nuevo'),

    # Listas
    path(
        'investigadores',
        views.investigadores_lista, name='investigadores_lista'),
    path(
        'perfil/investigaciones', views.InvestigadorInvestigaciones.as_view(),
        name='investigaciones_lista'),
    path(
        'perfil/investigaciones/fetch',
        views.investigaciones_google, name='investigaciones_fetch'),
    path(
        'perfil/solicitudes_trabajo',
        views.InvestigadorSolicitudesTrabajo.as_view(),
        name='solicitudes_trabajo_lista'),
    path('empresas', views.empresas_lista, name="empresas_lista"),
    path(
        'instituciones_educativas/', views.instituciones_educativas_lista,
        name="instituciones_educativas_lista"),
    path(
        'institucion_educativa/solicitud_ingreso',
        views.solicitudIngresoLista,
        name="institucion_educativa_solicitudes"),
    path(
        'institucion_educativa/miembros', views.miembrosLista,
        name="institucion_educativa_miembros"),

    # Perfiles públicos
    path(
        'investigadores/<int:investigador_id>',
        views.investigador_perfil, name='investigador_perfil'),

    # Solicitudes
    path(
        'perfil/solicitudes_trabajo/aprobar/<int:pk>',
        views.aceptar_solicitud,
        name='aceptar_solicitud'),
    path(
        'perfil/solicitudes_trabajo/rechazar/<int:pk>',
        views.rechazar_solicitud,
        name='rechazar_solicitud'),

    # Trabajos
    path(
        'perfil/trabajos', views.trabajos_en_curso,
        name='trabajos_lista'),
    path(
        'perfil/trabajos/historial', views.historial_trabajos,
        name='trabajos_historial'),
    path(
        'perfil/trabajos/cambiar_estado/<int:pk>/<str:estado>',
        views.cambiar_estado,
        name='cambiar_estado_solicitud'),
]
