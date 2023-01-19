from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import CreateView, UpdateView
from administracion.helpers import obtener_coordenadas
from empresas.models import Empresa
from empresas.forms import FormEmpresaUpdate
from usuarios.models import TipoUsuario


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


@login_required
def empresas_lista(request):
    empresas = Empresa.objects.filter(encargado__aprobado=True)
    return render(
        request,
        "vinculacion/empresas_lista.html",
        {"empresas": empresas})
