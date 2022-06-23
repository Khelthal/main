from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.models import TipoUsuario
from vinculacion.models import Categoria, Noticia
from django.views import View
from django.http.response import JsonResponse

# Create your views here.
def index(request):
    return render(request, "vinculacion/index.html")

@login_required
def dashboard(request):
    tipos_usuario = TipoUsuario.objects.all()
    tipos_usuario_snake_case = ["_".join(t.tipo.split()).lower() for t in tipos_usuario]
    return render(request, "vinculacion/map.html", {"tipos_usuario":zip(tipos_usuario, tipos_usuario_snake_case)})

@login_required
def noticias(request):
    noticias = Noticia.objects.all().order_by('fecha')

    return render(request, "vinculacion/noticias.html", {"noticias":noticias})

@login_required
def noticia(request, id):
    noticia = Noticia.objects.get(id = id)

    return render(request, "vinculacion/noticia.html", {"noticia":noticia})

@login_required
def perfil(request):
    return render(request, "vinculacion/perfil.html")

class Categorias(View):
    def get(self, request):
        categorias = Categoria.objects.all()
        categorias = [{"nombre":categoria.nombre} for categoria in categorias]

        return JsonResponse(categorias, safe = False)
