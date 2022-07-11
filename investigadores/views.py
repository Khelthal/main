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