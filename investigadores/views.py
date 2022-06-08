from django.shortcuts import render
from investigadores.models import Investigador

def lista(request):
    investigadores = Investigador.objects.all()
    return render(request, "lista.html", {"investigadores":investigadores})
