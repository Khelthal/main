from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from investigadores.forms import SolicitudTrabajoForm
from usuarios.models import TipoUsuario
from vinculacion.models import Categoria, Noticia
from vinculacion.helpers import (
    get_author,
    get_publications,
    get_user_specific_data)
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from administracion.forms import (
    FormInvestigadorBase,
    FormEmpresaUpdate,
    FormInstitucionEducativaUpdate,
    FormInvestigacion)
from investigadores.models import (
    Investigador,
    NivelInvestigador,
    Investigacion,
    InvestigacionGoogleScholar,
    SolicitudTrabajo)
from empresas.models import Empresa
from instituciones_educativas.models import (
    InstitucionEducativa,
    SolicitudIngreso)
from django.contrib import messages
from administracion.helpers import obtener_coordenadas
from usuarios.models import User, MUNICIPIOS
import itertools
from urllib.parse import urlparse, parse_qs
from . import helpers


# Create your views here.


def index(request):
    return redirect("usuarios:login")


@login_required
def dashboard(request):
    tipos_usuario = TipoUsuario.objects.all()
    tipos_usuario_snake_case = [
        "_".join(t.tipo.split()).lower() for t in tipos_usuario]
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
        "categorias": list(set(itertools.chain.from_iterable(
            [list(
                map(
                    str,
                    investigacion.categorias.all())
            ) for investigacion in Investigacion.objects.filter(
                autores=u.pk)]))),
        "municipio": u.municipio,
        "url": reverse_lazy("vinculacion:investigador_perfil", args=[u.pk])
    } for u in investigadores])
    usuarios.extend([{
        "username": u.encargado.username,
        "latitud": u.latitud,
        "longitud": u.longitud,
        "tipoUsuario": u.encargado.tipo_usuario.tipo,
        "categorias": list(map(str, u.especialidades.all())),
        "municipio": u.municipio,
        "url": ""
    } for u in empresas])
    usuarios.extend([{
        "username": u.encargado.username,
        "latitud": u.latitud,
        "longitud": u.longitud,
        "tipoUsuario": u.encargado.tipo_usuario.tipo,
        "categorias": list(map(str, u.especialidades.all())),
        "municipio": u.municipio,
        "url": ""
    } for u in instituciones_educativas])

    areas_conocimiento = list(
        set(map(lambda categoria: categoria.area_conocimiento, categorias)))
    areas_conocimiento = [{
        "area": area,
        "categorias": Categoria.objects.filter(
            area_conocimiento=area)
    } for area in areas_conocimiento]

    return render(
        request,
        "vinculacion/map.html",
        {
            "tipos_usuario": zip(tipos_usuario, tipos_usuario_snake_case),
            "categorias": categorias,
            "usuarios": usuarios,
            "municipios": MUNICIPIOS,
            "areas_conocimiento": areas_conocimiento
        })


@login_required
def noticias(request):
    noticias = Noticia.objects.all().order_by('fecha')

    return render(request, "vinculacion/noticias.html", {"noticias": noticias})


@login_required
def noticia(request, id):
    noticia = Noticia.objects.get(id=id)

    return render(request, "vinculacion/noticia.html", {"noticia": noticia})


@login_required
def perfil(request):
    usuario = request.user

    if usuario.is_staff:
        return redirect("administracion:dashboard")

    if not usuario.tipo_usuario:
        return render(request, "vinculacion/perfil_seleccionar.html")

    if not usuario.aprobado:
        return render(request, "vinculacion/perfil_pendiente.html")

    usuario_data = get_user_specific_data(usuario)

    return render(
        request,
        "vinculacion/perfil.html",
        {"usuario_data": usuario_data})


class InvestigadorSolicitud(CreateView):
    model = Investigador
    form_class = FormInvestigadorBase
    template_name = "vinculacion/formulario.html"
    extra_context = {"formulario_archivos": True}

    def form_valid(self, form):
        investigador = form.save(commit=False)
        investigador.user = self.request.user
        coordenadas = obtener_coordenadas(form.cleaned_data)

        if not coordenadas:
            messages.error(
                self.request,
                "Error al obtener los datos de ubicación, por favor" +
                " verifique que los datos de dirección" +
                " ingresados son correctos.")
            return super(InvestigadorSolicitud, self).form_invalid(form)

        investigador.latitud = coordenadas.latitud
        investigador.longitud = coordenadas.longitud
        investigador.user.tipo_usuario = TipoUsuario.objects.get(
            tipo="Investigador")
        investigador.nivel = NivelInvestigador.objects.get(nivel=1)

        investigador.save()
        investigador.user.save()

        messages.success(self.request, "Solicitud registrada correctamente")
        return redirect('vinculacion:perfil')


class InvestigadorActualizar(UpdateView):
    model = Investigador
    form_class = FormInvestigadorBase
    template_name = "vinculacion/formulario_perfil.html"
    extra_context = {"formulario_archivos": True}

    def get_object(self):
        return get_object_or_404(Investigador, user=self.request.user)

    def form_valid(self, form):
        investigador = form.save(commit=False)
        coordenadas = obtener_coordenadas(form.cleaned_data)

        if not coordenadas:
            messages.error(
                self.request,
                "Error al obtener los datos de ubicación, por favor" +
                " verifique que los datos de dirección" +
                " ingresados son correctos.")
            return super(InvestigadorActualizar, self).form_invalid(form)

        investigador.latitud = coordenadas.latitud
        investigador.longitud = coordenadas.longitud

        investigador.save()

        messages.success(self.request, "Perfil actualizado correctamente")
        return redirect('vinculacion:perfil')


class EmpresaSolicitud(CreateView):
    model = Empresa
    form_class = FormEmpresaUpdate
    template_name = "vinculacion/formulario.html"
    extra_context = {"formulario_archivos": True}

    def form_valid(self, form):
        empresa = form.save(commit=False)
        empresa.encargado = self.request.user
        coordenadas = obtener_coordenadas(form.cleaned_data)

        if not coordenadas:
            messages.error(
                self.request,
                "Error al obtener los datos de ubicación, por favor" +
                " verifique que los datos de dirección" +
                " ingresados son correctos.")
            return super(EmpresaSolicitud, self).form_invalid(form)

        empresa.latitud = coordenadas.latitud
        empresa.longitud = coordenadas.longitud
        empresa.encargado.tipo_usuario = TipoUsuario.objects.get(
            tipo="Empresa")

        empresa.save()
        empresa.encargado.save()
        form.save_m2m()

        messages.success(self.request, "Solicitud registrada correctamente")
        return redirect('vinculacion:perfil')


class EmpresaActualizar(UpdateView):
    model = Empresa
    form_class = FormEmpresaUpdate
    template_name = "vinculacion/formulario_perfil.html"
    extra_context = {"formulario_archivos": True}

    def get_object(self):
        return get_object_or_404(Empresa, encargado=self.request.user)

    def form_valid(self, form):
        empresa = form.save(commit=False)
        coordenadas = obtener_coordenadas(form.cleaned_data)

        if not coordenadas:
            messages.error(
                self.request,
                "Error al obtener los datos de ubicación, por favor" +
                " verifique que los datos de dirección" +
                " ingresados son correctos.")
            return super(EmpresaActualizar, self).form_invalid(form)

        empresa.latitud = coordenadas.latitud
        empresa.longitud = coordenadas.longitud

        empresa.save()
        form.save_m2m()

        messages.success(self.request, "Perfil actualizado correctamente")
        return redirect('vinculacion:perfil')


class InstitucionEducativaSolicitud(CreateView):
    model = InstitucionEducativa
    form_class = FormInstitucionEducativaUpdate
    template_name = "vinculacion/formulario.html"
    extra_context = {"formulario_archivos": True}

    def form_valid(self, form):
        institucion_educativa = form.save(commit=False)
        institucion_educativa.encargado = self.request.user
        coordenadas = obtener_coordenadas(form.cleaned_data)

        if not coordenadas:
            messages.error(
                self.request,
                "Error al obtener los datos de ubicación, por favor" +
                " verifique que los datos de dirección" +
                " ingresados son correctos.")
            return super(
                InstitucionEducativaSolicitud, self).form_invalid(form)

        institucion_educativa.latitud = coordenadas.latitud
        institucion_educativa.longitud = coordenadas.longitud
        institucion_educativa.encargado.tipo_usuario = TipoUsuario.objects.get(
            tipo="Institucion Educativa")

        institucion_educativa.save()
        institucion_educativa.encargado.save()
        form.save_m2m()

        messages.success(self.request, "Solicitud registrada correctamente")
        return redirect('vinculacion:perfil')


class InstitucionEducativaActualizar(UpdateView):
    model = InstitucionEducativa
    form_class = FormInstitucionEducativaUpdate
    template_name = "vinculacion/formulario_perfil.html"
    extra_context = {"formulario_archivos": True}

    def get_object(self):
        return get_object_or_404(
            InstitucionEducativa,
            encargado=self.request.user)

    def form_valid(self, form):
        institucion_educativa = form.save(commit=False)
        coordenadas = obtener_coordenadas(form.cleaned_data)

        if not coordenadas:
            messages.error(
                self.request,
                "Error al obtener los datos de ubicación, por favor" +
                " verifique que los datos de dirección" +
                " ingresados son correctos.")
            return super(
                InstitucionEducativaActualizar, self).form_invalid(form)

        institucion_educativa.latitud = coordenadas.latitud
        institucion_educativa.longitud = coordenadas.longitud

        institucion_educativa.save()
        form.save_m2m()

        messages.success(self.request, "Perfil actualizado correctamente")
        return redirect('vinculacion:perfil')


@login_required
def solicitudIngresoLista(request):
    institucion = get_object_or_404(
        InstitucionEducativa, encargado=request.user)
    solicitudes = SolicitudIngreso.objects.filter(
        institucion_educativa=institucion)

    return render(
        request,
        "vinculacion/solicitudes_ingreso.html",
        {"solicitudes": solicitudes})


class UsuarioEliminar(LoginRequiredMixin, DeleteView):
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
    investigadores.sort(
        key=lambda investigador: SolicitudTrabajo.objects.filter(
            usuario_a_vincular=investigador, estado="F").count(), reverse=True)
    categorias = []
    for investigador in investigadores:
        categorias_investigador = set()
        for investigacion in investigador.investigacion_set.all():
            for categoria in investigacion.categorias.all():
                categorias_investigador.add(categoria.nombre)
        categorias.append(list(categorias_investigador))

    return render(
        request,
        "vinculacion/investigadores_lista.html",
        {"investigadores": zip(investigadores, categorias)})


def investigador_perfil(request, investigador_id):
    investigador = Investigador.objects.get(pk=investigador_id)
    investigaciones = Investigacion.objects.filter(autores__in=[investigador])

    return render(
        request,
        "vinculacion/perfil_investigador.html",
        {
            "investigador": investigador,
            "investigaciones_lista": investigaciones
        })


@login_required
def empresas_lista(request):
    empresas = Empresa.objects.all()
    return render(
        request,
        "vinculacion/empresas_lista.html",
        {"empresas": empresas})


@login_required
def instituciones_educativas_lista(request):
    instituciones = InstitucionEducativa.objects.all()
    if (request.user.tipo_usuario
            and request.user.tipo_usuario.tipo == "Investigador"):
        investigador = Investigador.objects.get(user=request.user)

        for institucion in instituciones:
            solicitudes = SolicitudIngreso.objects.filter(
                institucion_educativa=institucion)
            institucion.es_posible_solicitar = True

            for solicitud in solicitudes:
                if solicitud.investigador == investigador:
                    institucion.es_posible_solicitar = False
                    break

            institucion.es_miembro = False
            if investigador in institucion.miembros.all():
                institucion.es_miembro = True
                institucion.es_posible_solicitar = False

    return render(
        request,
        "vinculacion/instituciones_educativas_lista.html",
        {"instituciones": instituciones})


@login_required
def crearSolicitudIngreso(request, institucion_id):
    institucion = InstitucionEducativa.objects.get(pk=institucion_id)
    investigador = Investigador.objects.get(user=request.user)
    solicitud_ingreso = SolicitudIngreso(
        institucion_educativa=institucion, investigador=investigador)
    solicitud_ingreso.save()
    messages.success(
        request,
        "Solicitud de ingreso a la institución "+str(institucion)+" enviada")

    return redirect("vinculacion:instituciones_educativas_lista")


@login_required
def contestarSolicitudIngreso(request, investigador_id, respuesta):
    investigador = get_object_or_404(Investigador, pk=investigador_id)
    solicitud = get_object_or_404(SolicitudIngreso, investigador=investigador)

    if respuesta == 1:
        messages.success(
            request, "Se ha aceptado la solicitud del investigador")
        institucion = InstitucionEducativa.objects.get(encargado=request.user)
        institucion.miembros.add(investigador)
    else:
        messages.error(
            request, "Se ha rechazado la solicitud del investigador")

    solicitud.delete()

    return redirect("vinculacion:institucion_educativa_solicitudes")


@login_required
def miembrosLista(request):
    institucion = InstitucionEducativa.objects.get(encargado=request.user)
    miembros = institucion.miembros.all()

    return render(
        request,
        "vinculacion/miembros_lista.html",
        {"miembros": miembros})


@login_required
def miembroEliminar(request, investigador_id):
    institucion = InstitucionEducativa.objects.get(encargado=request.user)
    investigador = Investigador.objects.get(pk=investigador_id)
    institucion.miembros.remove(investigador)

    return redirect("vinculacion:institucion_educativa_miembros")


class InvestigadorInvestigaciones(ListView):
    paginate_by = 10
    model = Investigacion
    template_name = "vinculacion/investigaciones_lista.html"

    def get_queryset(self):
        investigador = get_object_or_404(Investigador, user=self.request.user)
        return Investigacion.objects.filter(autores__in=[investigador])


class InvestigadorSolicitudesTrabajo(ListView):
    paginate_by = 10
    model = SolicitudTrabajo
    template_name = "vinculacion/solicitudes_trabajo_lista.html"

    def get_queryset(self):
        investigador = get_object_or_404(Investigador, user=self.request.user)
        return SolicitudTrabajo.objects.filter(
            usuario_a_vincular__in=[investigador],
            estado='E').order_by('fecha')


class InvestigacionNuevo(CreateView):
    model = Investigacion
    form_class = FormInvestigacion
    success_url = reverse_lazy('vinculacion:investigaciones_lista')
    template_name = "vinculacion/formulario_perfil.html"

    def form_valid(self, form):
        investigador = get_object_or_404(Investigador, user=self.request.user)
        investigacion = form.save()
        if investigador not in investigacion.autores.all():
            investigacion.autores.add(investigador)
        return redirect(self.success_url)


def investigaciones_google(request):
    if request.method == "POST":
        investigador = get_object_or_404(Investigador, user=request.user)
        parsed = urlparse(request.POST["profile-url"])
        arguments = parse_qs(parsed.query)
        try:
            user_id = arguments['user'][0]
        except Exception:
            messages.error(
                request, "No se encontró el perfil de google scholar")
            return redirect("vinculacion:investigaciones_lista")

        author = get_author(user_id)

        if author is None:
            messages.error(
                request, "No se encontró el perfil de google scholar")
            return redirect("vinculacion:investigaciones_lista")

        for publicacion in get_publications(author):
            try:
                InvestigacionGoogleScholar.objects.create(
                    titulo=publicacion["titulo"],
                    investigador=investigador,
                )
                investigacion = Investigacion.objects.create(
                    titulo=publicacion["titulo"],
                    contenido=publicacion["contenido"],
                )
                investigacion.autores.add(investigador),
                investigacion.save()
            except Exception:
                continue

    messages.success(
                request, "Carga de investigaciones exitosa")
    return redirect("vinculacion:investigaciones_lista")


class CrearSolicitudTrabajo(LoginRequiredMixin, CreateView):
    model = SolicitudTrabajo
    form_class = SolicitudTrabajoForm
    template_name = "vinculacion/formulario.html"

    def form_valid(self, form):
        investigador_id = self.kwargs['investigador_id']
        if self.request.user.pk == investigador_id:
            messages.error(
                self.request,
                "Un investigador no puede hacer una solicitud a sí mismo")
            return super(CrearSolicitudTrabajo, self).form_invalid(form)
        solicitud = form.save(commit=False)
        solicitud.usuario_solicitante = User.objects.get(
            pk=self.request.user.pk)
        investigador = get_object_or_404(
            Investigador,
            pk=investigador_id
        )
        solicitud.usuario_a_vincular = investigador
        solicitud.estado = "E"
        solicitud.save()
        messages.success(
            self.request,
            "Solicitud de trabajo a el investigador " +
            str(investigador)+" enviada")
        return redirect("vinculacion:investigador_perfil", investigador_id)


@login_required
def aceptar_solicitud(request, pk):
    investigador = get_object_or_404(
        Investigador,
        user=request.user
    )
    solicitud = get_object_or_404(
        SolicitudTrabajo,
        pk=pk,
        usuario_a_vincular=investigador,
        estado="E"
    )
    solicitud.estado = "A"
    solicitud.save()
    messages.success(request, "La solicitud ha sido aceptada")

    return redirect("vinculacion:solicitudes_trabajo_lista")


@login_required
def rechazar_solicitud(request, pk):
    investigador = get_object_or_404(
        Investigador,
        user=request.user
    )
    solicitud = get_object_or_404(
        SolicitudTrabajo,
        pk=pk,
        usuario_a_vincular=investigador,
        estado="E"
    )
    solicitud.estado = "R"
    solicitud.estado_investigador = "R"
    solicitud.save()
    messages.success(request, "La solicitud ha sido rechazada")

    return redirect("vinculacion:solicitudes_trabajo_lista")


@login_required
def trabajos_en_curso(request):
    usuario = get_object_or_404(User, pk=request.user.pk)
    trabajos = SolicitudTrabajo.objects.filter(
        Q(usuario_a_vincular__user=usuario) | Q(usuario_solicitante=usuario),
        estado__in=['A', 'P']).order_by('fecha').reverse()
    page = request.GET.get('page', 1)
    paginator = Paginator(trabajos, 5)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(
        request,
        "vinculacion/trabajos_en_curso.html",
        {"trabajos": trabajos, "page_obj": page_obj})


@login_required
def historial_trabajos(request):
    investigador = get_object_or_404(User, pk=request.user.pk)
    trabajos = SolicitudTrabajo.objects.filter(
        Q(usuario_a_vincular__user=investigador) |
        Q(usuario_solicitante=investigador),
        estado__in=['R', 'C', 'F']).order_by('fecha').reverse()

    page = request.GET.get('page', 1)
    paginator = Paginator(trabajos, 5)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(
        request,
        "vinculacion/historial_trabajos.html",
        {"trabajos": trabajos, "page_obj": page_obj})


@login_required
def cambiar_estado(request, pk, estado):
    solicitud = get_object_or_404(
        SolicitudTrabajo,
        pk=pk
    )

    if solicitud.estado == "F" or solicitud.estado == "C":
        messages.error(
            request,
            "No se puede cambiar el estado de una solicitud finalizada")
        return redirect('vinculacion:trabajos_lista')

    if estado == "C":
        messages.success(
            request,
            "Estado de trabajo canceldo")
        helpers.cancelar_trabajo(request.user.pk, solicitud)

    elif estado == "F":
        messages.success(
            request,
            "Estado de trabajo finalizado")
        helpers.finalizar_trabajo(request.user.pk, solicitud)

    elif estado == "R":
        messages.success(
            request,
            "Estado de trabajo rechazado")
        helpers.rechazar_trabajo(request.user.pk, solicitud)

    elif estado == "P":
        messages.success(
            request,
            "Estado de trabajo en proceso")
        helpers.trabajo_en_proceso(request.user.pk, solicitud)

    elif estado == "E":
        messages.success(
            request,
            "Estado de trabajo en Revision")
        helpers.trabajo_en_revision(request.user.pk, solicitud)

    else:
        messages.error(
            request,
            "Estado no válido")

    return redirect('vinculacion:trabajos_lista')
