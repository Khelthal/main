from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from usuarios.models import TipoUsuario
from vinculacion.models import Categoria, Noticia
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.http.response import JsonResponse
from administracion.forms import FormInvestigadorBase, FormEmpresaUpdate, FormInstitucionEducativaUpdate
from investigadores.models import Investigador, NivelInvestigador, Investigacion, SolicitudTrabajo
from empresas.models import Empresa
from instituciones_educativas.models import InstitucionEducativa, SolicitudIngreso
from django.contrib import messages
from administracion.helpers import obtener_coordenadas
from usuarios.models import User, MUNICIPIOS
import requests
import json
import itertools

# Create your views here.
def index(request):
    return render(request, "vinculacion/index.html")

@login_required
def dashboard(request):
    tipos_usuario = TipoUsuario.objects.all()
    tipos_usuario_snake_case = ["_".join(t.tipo.split()).lower() for t in tipos_usuario]
    categorias = Categoria.objects.all()
    usuarios = []
    investigadores = Investigador.objects.all()
    empresas = Empresa.objects.all()
    instituciones_educativas = InstitucionEducativa.objects.all()
    
    usuarios.extend([{
        "username": u.user.username,
        "latitud": u.latitud,
        "longitud": u.longitud,
        "tipoUsuario": u.user.tipo_usuario.tipo,
        "categorias": list(set(itertools.chain.from_iterable([list(map(str, investigacion.categorias.all())) for investigacion in Investigacion.objects.filter(autores=u.pk)]))),
        "municipio": u.municipio,
    } for u in investigadores])
    usuarios.extend([{
        "username": u.encargado.username,
        "latitud": u.latitud,
        "longitud": u.longitud,
        "tipoUsuario": u.encargado.tipo_usuario.tipo,
        "categorias": list(map(str, u.especialidades.all())),
        "municipio": u.municipio,
    } for u in empresas])
    usuarios.extend([{
        "username": u.encargado.username,
        "latitud": u.latitud,
        "longitud": u.longitud,
        "tipoUsuario": u.encargado.tipo_usuario.tipo,
        "categorias": list(map(str, u.especialidades.all())),
        "municipio": u.municipio,
    } for u in instituciones_educativas])
    
    areas_conocimiento = list(set(map(lambda categoria: categoria.area_conocimiento, categorias)))
    areas_conocimiento = [{"area":area, "categorias":Categoria.objects.filter(area_conocimiento=area)} for area in areas_conocimiento]
    
    return render(request, "vinculacion/map.html", {"tipos_usuario":zip(tipos_usuario, tipos_usuario_snake_case), "categorias":categorias, "usuarios":usuarios, "municipios":MUNICIPIOS, "areas_conocimiento":areas_conocimiento})

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
    
    tipo_usuario = "_".join(usuario.tipo_usuario.tipo.split()).lower()
    
    if tipo_usuario == "investigador":
        usuario_investigador = Investigador.objects.get(user=usuario)
        # usuario_data = {
        #     'email': usuario_investigador.email
        # }

    elif tipo_usuario == "empresa":
        pass
    elif tipo_usuario == "institucion_educativa":
        pass
    else:
        pass

    return render(request, f"vinculacion/perfil.html")

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
            return super(InvestigadorSolicitud, self).form_invalid(form)

        investigador.latitud = coordenadas.latitud
        investigador.longitud = coordenadas.longitud
        investigador.user.tipo_usuario = TipoUsuario.objects.get(tipo="Investigador")
        investigador.nivel = NivelInvestigador.objects.get(nivel=1)
        
        investigador.save()
        investigador.user.save()

        messages.success(self.request, "Solicitud registrada correctamente")
        return redirect('vinculacion:perfil')

class InvestigadorActualizar(UpdateView):
    model = Investigador
    form_class = FormInvestigadorBase
    template_name = "vinculacion/formulario_perfil.html"
    
    def get_object(self):
        return get_object_or_404(Investigador, user=self.request.user)

    def form_valid(self, form):
        investigador = form.save(commit=False)
        coordenadas = obtener_coordenadas(form.cleaned_data)
        
        if not coordenadas:
            messages.error(self.request, "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos.")
            return super(InvestigadorActualizar, self).form_invalid(form)

        investigador.latitud = coordenadas.latitud
        investigador.longitud = coordenadas.longitud
        
        investigador.save()

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
            return super(EmpresaSolicitud, self).form_invalid(form)

        empresa.latitud = coordenadas.latitud
        empresa.longitud = coordenadas.longitud
        empresa.encargado.tipo_usuario = TipoUsuario.objects.get(tipo="Empresa")
        
        empresa.save()
        empresa.encargado.save()
        form.save_m2m()

        messages.success(self.request, "Solicitud registrada correctamente")
        return redirect('vinculacion:perfil')

class EmpresaActualizar(UpdateView):
    model = Empresa
    form_class = FormEmpresaUpdate
    template_name = "vinculacion/formulario_perfil.html"

    def get_object(self):
        return get_object_or_404(Empresa, encargado=self.request.user)

    def form_valid(self, form):
        empresa = form.save(commit=False)
        coordenadas = obtener_coordenadas(form.cleaned_data)
        
        if not coordenadas:
            messages.error(self.request, "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos.")
            return super(EmpresaActualizar, self).form_invalid(form)

        empresa.latitud = coordenadas.latitud
        empresa.longitud = coordenadas.longitud
        
        empresa.save()
        form.save_m2m()

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
            return super(InstitucionEducativaSolicitud, self).form_invalid(form)

        institucion_educativa.latitud = coordenadas.latitud
        institucion_educativa.longitud = coordenadas.longitud
        institucion_educativa.encargado.tipo_usuario = TipoUsuario.objects.get(tipo="Institucion Educativa")
        
        institucion_educativa.save()
        institucion_educativa.encargado.save()
        form.save_m2m()

        messages.success(self.request, "Solicitud registrada correctamente")
        return redirect('vinculacion:perfil')

class InstitucionEducativaActualizar(UpdateView):
    model = InstitucionEducativa
    form_class = FormInstitucionEducativaUpdate
    template_name = "vinculacion/formulario_perfil.html"

    def get_object(self):
        return get_object_or_404(InstitucionEducativa, encargado=self.request.user)

    def form_valid(self, form):
        institucion_educativa = form.save(commit=False)
        coordenadas = obtener_coordenadas(form.cleaned_data)
        
        if not coordenadas:
            messages.error(self.request, "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos.")
            return super(InstitucionEducativaActualizar, self).form_invalid(form)

        institucion_educativa.latitud = coordenadas.latitud
        institucion_educativa.longitud = coordenadas.longitud
        
        institucion_educativa.save()
        form.save_m2m()

        messages.success(self.request, "Solicitud registrada correctamente")
        return redirect('vinculacion:perfil')

@login_required
def solicitudIngresoLista(request):
    institucion = get_object_or_404(InstitucionEducativa, encargado=request.user)
    solicitudes = SolicitudIngreso.objects.filter(institucion_educativa=institucion)

    return render(request, "vinculacion/solicitudes_ingreso.html", {"solicitudes":solicitudes})

class UsuarioEliminar(DeleteView):
    model = User
    success_url = reverse_lazy('vinculacion:index')
    template_name = "vinculacion/confirm_delete.html"
    
    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        messages.success(self.request, "Cuenta eliminada correctamente")
        return self.delete(request, *args, **kwargs)

@login_required
def investigadores_lista(request):
    investigadores = list(Investigador.objects.all())
    investigadores.sort(key=lambda investigador: SolicitudTrabajo.objects.filter(usuario_a_vincular=investigador, estado="F").count(), reverse=True)
    categorias = []
    for investigador in investigadores:
        categorias_investigador = set()
        for investigacion in investigador.investigacion_set.all():
            for categoria in investigacion.categorias.all():
                categorias_investigador.add(categoria.nombre)
        categorias.append(list(categorias_investigador))

    return render(request, "vinculacion/investigadores_lista.html", {"investigadores":zip(investigadores, categorias)})

@login_required
def empresas_lista(request):
    empresas = Empresa.objects.all()
    return render(request, "vinculacion/empresas_lista.html", {"empresas":empresas})

@login_required
def instituciones_educativas_lista(request, solicitada=None):
    instituciones = InstitucionEducativa.objects.all()
    print(type(solicitada))
    if request.user.tipo_usuario and request.user.tipo_usuario.tipo == "Investigador":
        investigador = Investigador.objects.get(user = request.user)

        for institucion in instituciones:
            solicitudes = SolicitudIngreso.objects.filter(institucion_educativa = institucion)
            institucion.es_posible_solicitar = True

            if solicitudes:
                for solicitud in solicitudes:
                    if solicitud.investigador == investigador:
                        institucion.es_posible_solicitar = False
                        break

    if solicitada != None:
        solicitada = InstitucionEducativa.objects.get(pk = solicitada)

    return render(request, "vinculacion/instituciones_educativas_lista.html", {"instituciones":instituciones, "institucion":solicitada})

@login_required
def crearSolicitudIngreso(request, institucion_id):
    institucion = InstitucionEducativa.objects.get(pk = institucion_id)
    investigador = Investigador.objects.get(user = request.user)
    solicitud_ingreso = SolicitudIngreso(institucion_educativa=institucion, investigador=investigador)
    solicitud_ingreso.save()

    return redirect("vinculacion:instituciones_educativas_lista", institucion.pk)

@login_required
def contestarSolicitudIngreso(request, investigador_id, respuesta):

    if respuesta == 1:
        institucion = InstitucionEducativa.objects.get(encargado = request.user)
        investigador = Investigador.objects.get(pk = investigador_id)
        institucion.miembros.add(investigador)

    solicitud = SolicitudIngreso.objects.get(investigador = investigador)
    solicitud.delete()

    return redirect("vinculacion:institucion_educativa_solicitudes")

@login_required
def miembrosLista(request):
    institucion = InstitucionEducativa.objects.get(encargado = request.user)
    miembros = institucion.miembros.all()

    return render(request, "vinculacion/miembros_lista.html", {"miembros":miembros})

@login_required
def miembroEliminar(request, investigador_id):
    institucion = InstitucionEducativa.objects.get(encargado = request.user)
    investigador = Investigador.objects.get(pk = investigador_id)
    institucion.miembros.remove(investigador)

    return redirect("vinculacion:institucion_educativa_miembros")