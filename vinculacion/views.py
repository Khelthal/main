from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from usuarios.models import TipoUsuario
from vinculacion.models import Categoria, Noticia
from django.views import View
from django.views.generic import CreateView
from django.http.response import JsonResponse
from administracion.forms import FormInvestigadorBase, FormEmpresaUpdate, FormInstitucionEducativaUpdate
from investigadores.models import Investigador, NivelInvestigador
from empresas.models import Empresa
from instituciones_educativas.models import InstitucionEducativa
from django.contrib import messages
from administracion.helpers import obtener_coordenadas
import requests
import json

# Create your views here.
def index(request):
    return render(request, "vinculacion/index.html")

@login_required
def dashboard(request):
    tipos_usuario = TipoUsuario.objects.all()
    tipos_usuario_snake_case = ["_".join(t.tipo.split()).lower() for t in tipos_usuario]
    categorias = Categoria.objects.all()
    return render(request, "vinculacion/map.html", {"tipos_usuario":zip(tipos_usuario, tipos_usuario_snake_case), "categorias":categorias})

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
    
    if usuario.is_staff:
        return redirect("administracion:dashboard")

    if not usuario.tipo_usuario:
        return render(request, "vinculacion/perfil_seleccionar.html")
    
    if not usuario.aprobado:
        return render(request, "vinculacion/perfil_pendiente.html")

    return render(request, "vinculacion/perfil_investigador.html")

class InvestigadorSolicitud(CreateView):
    model = Investigador
    form_class = FormInvestigadorBase
    template_name = "vinculacion/formulario.html"

    def form_valid(self, form):
        investigador = form.save(commit=False)
        investigador.user = self.request.user
        coordenadas = obtener_coordenadas(form.cleaned_data)
        
        if not coordenadas:
            messages.error(self.request, "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos.")
            return redirect('vinculacion:investigador_form')

        investigador.latitud = coordenadas.latitud
        investigador.longitud = coordenadas.longitud
        investigador.user.tipo_usuario = TipoUsuario.objects.get(tipo="Investigador")
        investigador.nivel = NivelInvestigador.objects.get(nivel=1)
        
        investigador.save()
        investigador.user.save()

        messages.success(self.request, "Solicitud registrada correctamente")
        return redirect('vinculacion:perfil')

class EmpresaSolicitud(CreateView):
    model = Empresa
    form_class = FormEmpresaUpdate
    template_name = "vinculacion/formulario.html"

    def form_valid(self, form):
        empresa = form.save(commit=False)
        empresa.encargado = self.request.user
        coordenadas = obtener_coordenadas(form.cleaned_data)
        
        if not coordenadas:
            messages.error(self.request, "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos.")
            return redirect('vinculacion:empresa_form')

        empresa.latitud = coordenadas.latitud
        empresa.longitud = coordenadas.longitud
        empresa.encargado.tipo_usuario = TipoUsuario.objects.get(tipo="Empresa")
        
        empresa.save()
        empresa.encargado.save()

        messages.success(self.request, "Solicitud registrada correctamente")
        return redirect('vinculacion:perfil')

class InstitucionEducativaSolicitud(CreateView):
    model = InstitucionEducativa
    form_class = FormInstitucionEducativaUpdate
    template_name = "vinculacion/formulario.html"

    def form_valid(self, form):
        institucion_educativa = form.save(commit=False)
        institucion_educativa.encargado = self.request.user
        coordenadas = obtener_coordenadas(form.cleaned_data)
        
        if not coordenadas:
            messages.error(self.request, "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos.")
            return redirect('vinculacion:institucion_educativa_form')

        institucion_educativa.latitud = coordenadas.latitud
        institucion_educativa.longitud = coordenadas.longitud
        institucion_educativa.encargado.tipo_usuario = TipoUsuario.objects.get(tipo="Institucion Educativa")
        
        institucion_educativa.save()
        institucion_educativa.encargado.save()

        messages.success(self.request, "Solicitud registrada correctamente")
        return redirect('vinculacion:perfil')
