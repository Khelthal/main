from django.shortcuts import render
from vinculacion.models import Categoria

# Create your views here.
def index(request):
    return render(request, "index.html")

def dashboard(request):
    categorias = Categoria.objects.all()
    return render(request, "map.html", {"categorias":categorias})
