from django.urls import path
from investigadores.views import *

app_name = 'investigadores'

urlpatterns = [
    path('', lista, name='lista_investigador'),
    path('nuevo', NuevoInvestigadorView.as_view(), name='nuevo_investigador'),
    path('eliminar/<int:pk>', EliminarInvestigadorView.as_view(), name='eliminar_investigador'),
    path('editar/<int:id>', editar_investigador, name='editar_investigador'),

    path('investigaciones', investigaciones, name='lista_investigacion'),
    path('investigaciones/nueva', NuevaInvestigacionView.as_view(), name='nueva_investigacion'),
    path('investigadores/eliminar/<int:pk>', EliminarInvestigacionView.as_view(), name='eliminar_investigacion'),
    path('investigadores/editar/<int:id>', editar_investigacion, name='editar_investigacion'),
]
