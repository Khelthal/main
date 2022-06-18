from django.shortcuts import render
from vinculacion.models import Categoria
from investigadores.models import Investigador

# Create your views here.
def index(request):
    return render(request, "vinculacion/index.html")

def dashboard(request):
    return render(request, "vinculacion/map.html")

def noticias(request):
    noticias = ["", "", ""]

    return render(request, "vinculacion/noticias.html", {"noticias":noticias})

def noticia(request):
    noticia = {"":""}

    return render(request, "vinculacion/noticia.html", {"noticia":noticia})

def perfil(request):
    return render(request, "vinculacion/perfil.html")