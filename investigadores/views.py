from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required

from investigadores.models import Investigador, Investigacion

@login_required
def investigadores_lista(request):
    investigadores = Investigador.objects.all()
    categorias = []
    for investigador in investigadores:
        categorias_investigador = set()
        for investigacion in investigador.investigacion_set.all():
            for categoria in investigacion.categorias.all():
                categorias_investigador.add(categoria.nombre)
        categorias.append(list(categorias_investigador))

    return render(request, "vinculacion/investigadores_lista.html", {"investigadores":zip(investigadores, categorias)})

class Investigadores(View):
    def get(self, request):
        investigadores = list(Investigador.objects.all())

        def investigador_to_dic(investigador):
            investigaciones = Investigacion.objects.filter(autores=investigador.pk)
            categorias = []
            for investigacion in investigaciones:
                categorias.extend(list(map(lambda categoria: str(categoria),investigacion.categorias.all())))
                
            return {
                    "username": investigador.user.username,
                    "latitud": investigador.latitud,
                    "longitud": investigador.longitud,
                    "tipoUsuario": str(investigador.user.tipo_usuario),
                    "categorias": categorias
            }

        investigadores = list(map(investigador_to_dic, investigadores))

        return JsonResponse(list(investigadores), safe = False)
