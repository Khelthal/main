from django.urls import path
from instituciones_educativas.views import InstitucionesEducativas

app_name = 'investigadores'

urlpatterns = [
    path('fetch', InstitucionesEducativas.as_view(), name='instituciones_educativas_fetch'),
]
