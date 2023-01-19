import asyncio
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from administracion.helpers import obtener_coordenadas
from investigadores.models import (
    Investigador,
    Investigacion,
    NivelInvestigador,
    SolicitudTrabajo,
    InvestigacionGoogleScholar
)
from investigadores.forms import (
    FormInvestigadorBase,
    FormInvestigacion,
)
from vinculacion.helpers import (
    get_author,
    get_publications
)
from usuarios.models import TipoUsuario
from urllib.parse import urlparse, parse_qs


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


@login_required
def investigadores_lista(request):
    investigadores = list(Investigador.objects.filter(user__aprobado=True))
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


class InvestigadorInvestigaciones(ListView):
    paginate_by = 10
    model = Investigacion
    template_name = "vinculacion/investigaciones_lista.html"

    def get_queryset(self):
        investigador = get_object_or_404(Investigador, user=self.request.user)
        return Investigacion.objects.filter(
            autores__in=[investigador]).order_by('titulo')


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

        publicaciones = asyncio.run(get_publications(author))

        for publicacion in publicaciones:
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
