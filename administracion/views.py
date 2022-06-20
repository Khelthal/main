from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from usuarios.models import User, TipoUsuario
from investigadores.models import Investigador
from empresas.models import Empresa
from instituciones_educativas.models import InstitucionEducativa
from django.views.generic import CreateView, UpdateView, DeleteView
from administracion.forms import *
from django.contrib import messages
import requests
import json

def dashboard(request):
    return render(request, "administracion/dashboard.html")

# Usuarios

def usuarios_lista(request):
    usuarios = User.objects.all()
    return render(request, "administracion/usuarios_lista.html", {"usuarios":usuarios})

class UsuarioNuevo(CreateView):
    model = User
    form_class = FormUser
    success_url = reverse_lazy('administracion:usuarios_lista')
    template_name = "administracion/usuarios_form.html"
    extra_context = { "accion": "Crear" }

class UsuarioEditar(UpdateView):
    model = User
    form_class = FormUser
    success_url = reverse_lazy('administracion:usuarios_lista')
    template_name = "administracion/usuarios_form.html"
    extra_context = { "accion": "Editar" }

class UsuarioEliminar(DeleteView):
    model = User
    success_url = reverse_lazy('administracion:usuarios_lista')
    template_name = "administracion/confirm_delete.html"
    extra_context = { "nombre_modelo": "usuario" }

# Investigadores

def investigadores_lista(request):
    investigadores = Investigador.objects.all()
    return render(request, "administracion/investigadores_lista.html", {"investigadores":investigadores})

class InvestigadorNuevo(CreateView):
    model = Investigador
    form_class = FormInvestigador
    success_url = reverse_lazy('administracion:investigadores_lista')
    template_name = "administracion/investigadores_form.html"
    extra_context = { "accion": "Crear" }

    def form_valid(self, form):
        investigador = form.save(commit=False)
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
        
        investigador.save()
        investigador.user.save()

        messages.success(self.request, "Investigador registrado correctamente")
        return redirect('administracion:investigadores_lista')

class InvestigadorEditar(UpdateView):
    model = Investigador
    form_class = FormInvestigadorUpdate
    success_url = reverse_lazy('administracion:investigadores_lista')
    template_name = "administracion/investigadores_form.html"
    extra_context = { "accion": "Editar" }

    def form_valid(self, form):
        investigador = form.save(commit=False)
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
        
        investigador.save()

        messages.success(self.request, "Investigador actualizado correctamente")
        return redirect('administracion:investigadores_lista')
        
class InvestigadorEliminar(DeleteView):
    model = Investigador
    success_url = reverse_lazy('administracion:investigadores_lista')
    template_name = "administracion/confirm_delete.html"
    extra_context = { "nombre_modelo": "investigador" }

    def post(self, request, *args, **kwargs):
        investigador = self.get_object()
        investigador.user.tipo_usuario = None
        investigador.user.save()

        return self.delete(request, *args, **kwargs)

# Empresas

def empresas_lista(request):
    empresas = Empresa.objects.all()
    return render(request, "administracion/empresas_lista.html", {"empresas":empresas})

class EmpresaNuevo(CreateView):
    model = Empresa
    form_class = FormEmpresa
    success_url = reverse_lazy('administracion:empresas_lista')
    template_name = "administracion/empresas_form.html"
    extra_context = { "accion": "Crear" }

    def form_valid(self, form):
        empresa = form.save(commit=False)
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
            return redirect('administracion:empresas_nuevo')

        data = json.loads(r.text)
        
        if len(data) == 0:
            messages.error(self.request, "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos.")
            return redirect('administracion:empresas_nuevo')
            
        data = data[0]

        if "lat" not in data or "lon" not in data:
            messages.error(self.request, "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos.")
            return redirect('administracion:empresas_nuevo')
        
        empresa.latitud = float(data["lat"])
        empresa.longitud = float(data["lon"])
        empresa.encargado.tipo_usuario = TipoUsuario.objects.get(tipo="Empresa")
        
        empresa.save()
        empresa.encargado.save()

        messages.success(self.request, "Empresa registrada correctamente")
        return redirect('administracion:empresas_lista')

class EmpresaEditar(UpdateView):
    model = Empresa
    form_class = FormEmpresaUpdate
    success_url = reverse_lazy('administracion:empresas_lista')
    template_name = "administracion/empresas_form.html"
    extra_context = { "accion": "Editar" }

    def form_valid(self, form):
        empresa = form.save(commit=False)
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
            return redirect('administracion:empresas_nuevo')

        data = json.loads(r.text)
        
        if len(data) == 0:
            messages.error(self.request, "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos.")
            return redirect('administracion:empresas_nuevo')
            
        data = data[0]

        if "lat" not in data or "lon" not in data:
            messages.error(self.request, "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos.")
            return redirect('administracion:empresas_nuevo')
        
        empresa.latitud = float(data["lat"])
        empresa.longitud = float(data["lon"])
        
        empresa.save()

        messages.success(self.request, "Empresa actualizada correctamente")
        return redirect('administracion:empresas_lista')
        
class EmpresaEliminar(DeleteView):
    model = Empresa
    success_url = reverse_lazy('administracion:empresas_lista')
    template_name = "administracion/confirm_delete.html"
    extra_context = { "nombre_modelo": "empresa" }

    def post(self, request, *args, **kwargs):
        empresa = self.get_object()
        empresa.encargado.tipo_usuario = None
        empresa.encargado.save()

        return self.delete(request, *args, **kwargs)

# Instituciones Educativas

def instituciones_educativas_lista(request):
    instituciones_educativas = InstitucionEducativa.objects.all()
    return render(request, "administracion/instituciones_educativas_lista.html", {"instituciones_educativas":instituciones_educativas})