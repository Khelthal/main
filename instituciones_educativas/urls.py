from django.urls import path
from instituciones_educativas.views import InstitucionesEducativas

app_name = 'instituciones_educativas'

urlpatterns = [
    path('fetch', InstitucionesEducativas.as_view(), name='instituciones_educativas_fetch'),
]
