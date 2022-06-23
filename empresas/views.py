from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http.response import JsonResponse
from empresas.models import Empresa

@login_required
def empresas_lista(request):
    return render(request, "empresas/empresas_lista.html")   

class Empresas(View):
    def get(self, request):
        empresas = Empresa.objects.all()
        
        def empresa_to_dic(empresa):
            return {
                "username": empresa.nombre_empresa,
                "latitud": empresa.latitud,
                "longitud": empresa.longitud,
                "tipoUsuario": empresa.encargado.tipo_usuario.tipo,
                "categorias": []
            }

        empresas = [empresa_to_dic(empresa) for empresa in empresas]
        return JsonResponse(empresas, safe = False)
