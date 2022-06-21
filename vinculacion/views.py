from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from vinculacion.models import Categoria
from usuarios.models import TipoUsuario
from django.http.response import JsonResponse

# Create your views here.
@login_required
def index(request):
    return render(request, "vinculacion/index.html")

@login_required
def dashboard(request):
    tipos_usuario = TipoUsuario.objects.all()
    tipos_usuario_snake_case = ["_".join(t.tipo.split()).lower() for t in tipos_usuario]
    return render(request, "vinculacion/map.html", {"tipos_usuario":zip(tipos_usuario, tipos_usuario_snake_case)})

@login_required
def noticias(request):
    noticias = ["", "", ""]

    return render(request, "vinculacion/noticias.html", {"noticias":noticias})

@login_required
def noticia(request):
    noticia = {"":""}

    return render(request, "vinculacion/noticia.html", {"noticia":noticia})

@login_required
def perfil(request):
    return render(request, "vinculacion/perfil.html")

class Categorias(View):
    def get(self, request):
        categorias = Categoria.objects.all()
        categorias = [{"nombre":categoria.nombre} for categoria in categorias]

        return JsonResponse(categorias, safe = False)
