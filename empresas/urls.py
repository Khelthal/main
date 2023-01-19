from django.urls import path
from django.contrib.auth.decorators import login_required
import empresas.views as views

app_name = "empresas"

urlpatterns = [
    path(
        'formularios/empresa', login_required(
            views.EmpresaSolicitud.as_view()),
        name='empresa_form'),
    path(
        'formularios/empresa/actualizar',
        views.EmpresaActualizar.as_view(),
        name='empresa_actualizar'),
    path(
        'empresas', views.empresas_lista,
        name='empresas_lista'),
]
