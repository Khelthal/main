from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from instituciones_educativas.models import InstitucionEducativa

class InstitucionesEducativas(View):
    def get(self, request):
        instituciones_educativas = InstitucionEducativa.objects.all()        
        
        def institucion_to_dic(institucion):
            return {
                    "username": institucion.nombre_institucion,
                    "latitud": institucion.latitud,
                    "longitud": institucion.longitud,
                    "tipoUsuario": institucion.encargado.tipo_usuario.tipo,
                    "categorias": []
            }
        instituciones_educativas = [institucion_to_dic(institucion) for institucion in instituciones_educativas]

        return JsonResponse(instituciones_educativas, safe = False)
