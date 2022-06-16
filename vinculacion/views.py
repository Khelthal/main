from django.shortcuts import render
from vinculacion.models import Categoria
from investigadores.models import Investigador
from usuarios.models import Empresa, InstitucionEducativa

# Create your views here.
def index(request):
    return render(request, "vinculacion/index.html")

def dashboard(request):
    categorias = Categoria.objects.all()
    investigadores = Investigador.objects.all()
    empresas = Empresa.objects.all()
    instituciones = InstitucionEducativa.objects.all()
    usuarios = []
    usuarios.extend(list(investigadores))
    usuarios.extend(list(empresas))
    usuarios.extend(list(instituciones))
    return render(request, "vinculacion/map.html", {"categorias":categorias, "usuarios":usuarios})

def empresas(request):
    return render(request, "vinculacion/empresas.html")
    
def investigadores(request):
    investigadores = Investigador.objects.all()
    categorias = []
    for investigador in investigadores:
        categorias_investigador = set()
        for investigacion in investigador.investigacion_set.all():
            for categoria in investigacion.categorias.all():
                categorias_investigador.add(categoria.nombre)
        categorias.append(list(categorias_investigador))

    return render(request, "vinculacion/investigadores_lista.html", {"investigadores":zip(investigadores, categorias)})

def noticias(request):
    noticias = ["", "", ""]

    return render(request, "vinculacion/noticias.html", {"noticias":noticias})
