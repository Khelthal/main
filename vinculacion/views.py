from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.models import User
from vinculacion.models import Categoria, Noticia
from investigadores.models import Investigador

# Create your views here.
@login_required
def index(request):
    return render(request, "vinculacion/index.html")

@login_required
def dashboard(request):
    return render(request, "vinculacion/map.html")

@login_required
def noticias(request):
    noticias = Noticia.objects.all().order_by('fecha')

    return render(request, "vinculacion/noticias.html", {"noticias":noticias})

@login_required
def noticia(request):
    noticia = {"":""}

    return render(request, "vinculacion/noticia.html", {"noticia":noticia})

@login_required
def perfil(request):
    return render(request, "vinculacion/perfil.html")