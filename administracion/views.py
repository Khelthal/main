from django.shortcuts import render
from usuarios.models import User

def dashboard(request):
    return render(request, "administracion/dashboard.html")

def usuarios_lista(request):
    usuarios = User.objects.all()
    return render(request, "administracion/usuarios_lista.html", {"usuarios":usuarios})