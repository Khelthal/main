from django.shortcuts import render
from vinculacion.models import Categoria
from investigadores.models import Investigador
from usuarios.models import Empresa, InstitucionEducativa

# Create your views here.
def index(request):
    return render(request, "index.html")

def dashboard(request):
    categorias = Categoria.objects.all()
    investigadores = Investigador.objects.all()
    empresas = Empresa.objects.all()
    instituciones = InstitucionEducativa.objects.all()
    usuarios = []
    usuarios.extend(list(investigadores))
    usuarios.extend(list(empresas))
    usuarios.extend(list(instituciones))
    return render(request, "map.html", {"categorias":categorias, "usuarios":usuarios})
