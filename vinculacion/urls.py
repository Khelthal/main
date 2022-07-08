from django.urls import path, include
from .views import *

app_name = "vinculacion"

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('noticias', noticias, name='noticias'),
    path('noticias/<int:id>', noticia, name='noticia'),
    path('perfil', perfil, name='perfil'),
    
    #Formularios
    path('formularios/investigador', InvestigadorSolicitud.as_view(), name='investigador_form'),
    path('formularios/empresa', EmpresaSolicitud.as_view(), name='empresa_form'),
    path('formularios/institucion_educativa', InstitucionEducativaSolicitud.as_view(), name='institucion_educativa_form'),
]
