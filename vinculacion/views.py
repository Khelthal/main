from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from usuarios.models import TipoUsuario
from vinculacion.models import Categoria, Noticia
from django.views import View
from django.views.generic import CreateView
from django.http.response import JsonResponse
from administracion.forms import FormInvestigadorBase
from investigadores.models import Investigador, NivelInvestigador
from django.contrib import messages
import requests
import json

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
    usuario = request.user

    if not usuario.tipo_usuario:
        return render(request, "vinculacion/perfil_seleccionar.html")
    
    if not usuario.aprobado:
        return render(request, "vinculacion/perfil_pendiente.html")

    return render(request, "vinculacion/perfil_investigador.html")

class InvestigadorSolicitud(CreateView):
    model = Investigador
    form_class = FormInvestigadorBase
    success_url = reverse_lazy('vinculacion:perfil')
    template_name = "vinculacion/formulario.html"

    def form_valid(self, form):
        investigador = form.save(commit=False)
        investigador.user = self.request.user
        codigo_postal = form.cleaned_data['codigo_postal']
        municipio = form.cleaned_data['municipio']
        colonia = form.cleaned_data['colonia']
        calle = form.cleaned_data['calle']
        numero_exterior = form.cleaned_data['numero_exterior']
        
        headers = {
            'User-agent': 'Script de consulta de ubicacion'
        }
        r = requests.get(f"https://nominatim.openstreetmap.org/search?street='{numero_exterior} {calle}'&city={municipio}&country=Mexico&state=Zacatecas&postalcode={codigo_postal}&format=json", headers=headers)
        
        if r.status_code != 200:
            messages.error(self.request, "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos.")
            return redirect('administracion:investigadores_nuevo')

        data = json.loads(r.text)
        
        if len(data) == 0:
            messages.error(self.request, "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos.")
            return redirect('administracion:investigadores_nuevo')
            
        data = data[0]

        if "lat" not in data or "lon" not in data:
            messages.error(self.request, "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos.")
            return redirect('administracion:investigadores_nuevo')
        
        investigador.latitud = float(data["lat"])
        investigador.longitud = float(data["lon"])
        investigador.user.tipo_usuario = TipoUsuario.objects.get(tipo="Investigador")
        investigador.nivel = NivelInvestigador.objects.get(nivel=1)
        
        investigador.save()
        investigador.user.save()

        messages.success(self.request, "Investigador registrado correctamente")
        return redirect('vinculacion:perfil')

class Categorias(View):
    def get(self, request):
        categorias = Categoria.objects.all()
        categorias = [{"nombre":categoria.nombre} for categoria in categorias]

        return JsonResponse(categorias, safe = False)
