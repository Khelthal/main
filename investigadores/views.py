from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
import json

from investigadores.models import Investigador, Investigacion
from investigadores.forms import InvestigadorForm, InvestigacionForm

def lista(request):
    investigadores = Investigador.objects.all()
    return render(request, "investigadores.html", {"investigadores":investigadores})

class NuevoInvestigadorView(LoginRequiredMixin, CreateView):
    model = Investigador
    # fields = '__all__'
    form_class = InvestigadorForm
    extra_context = {'accion':'Nuevo'}
    success_url = reverse_lazy('investigadores:lista_investigador')
    
    def form_valid(self,form):
        try:
            form.save()
            messages.success(self.request, 'Se creó el investigador')
        except:
            messages.error(self.request, 'Error al guardar los cambios')

        return HttpResponseRedirect(self.success_url)
        
    def form_invalid(self, form):
        messages.error(self.request,"Hubo uno o más errores en el formulario")

class EliminarInvestigadorView(LoginRequiredMixin,DeleteView):
    model = Investigador
    extra_context = {'accion':'Eliminar'}
    success_url = reverse_lazy('investigadores:lista_investigador')
    
    def form_valid(self,form):
        try:
            self.object.delete()
            messages.success(self.request, 'Se eliminó el investigador')
        except:
            messages.error(self.request, 'Error al guardar los cambios')

        return HttpResponseRedirect(self.success_url)
        
    def form_invalid(self, form):
        messages.error(self.request,"Hubo uno o más errores en el formulario") 

def editar_investigador(request, id):
    investigador = Investigador.objects.get(pk=id)
    if request.method == 'POST':
        form = InvestigadorForm(request.POST, instance=investigador)
        if form.is_valid():
            form.save()
            return redirect('investigadores:lista_investigador')
    else:
        form = InvestigadorForm(instance=investigador)
    return render(request, 'investigadores/investigador_form.html', {'form':form, 'accion':'Modificar','a': id})

def investigaciones(request):
    investigaciones = Investigacion.objects.all()
    return render(request, 'investigaciones.html', {'investigaciones':investigaciones})

class NuevaInvestigacionView(LoginRequiredMixin, CreateView):
    model = Investigacion
    # fields = '__all__'
    form_class = InvestigacionForm
    extra_context = {'accion':'Nuevo'}
    success_url = reverse_lazy('investigadores:lista_investigacion')
    
    def form_valid(self,form):
        try:
            form.save()
            messages.success(self.request, 'Se creó la investigacion')
        except:
            messages.error(self.request, 'Error al guardar los cambios')

        return HttpResponseRedirect(self.success_url)
        
    def form_invalid(self, form):
        messages.error(self.request,"Hubo uno o más errores en el formulario")

class EliminarInvestigacionView(LoginRequiredMixin,DeleteView):
    model = Investigacion
    extra_context = {'accion':'Eliminar'}
    success_url = reverse_lazy('investigadores:lista_investigacion')
    
    def form_valid(self,form):
        try:
            self.object.delete()
            messages.success(self.request, 'Se eliminó la investigacion')
        except:
            messages.error(self.request, 'Error al guardar los cambios')

        return HttpResponseRedirect(self.success_url)
        
    def form_invalid(self, form):
        messages.error(self.request,"Hubo uno o más errores en el formulario") 

def editar_investigacion(request, id):
    investigacion = Investigacion.objects.get(pk=id)
    if request.method == 'POST':
        form = InvestigacionForm(request.POST, instance=investigacion)
        if form.is_valid():
            form.save()
            return redirect('investigadores:lista_investigacion')
    else:
        form = InvestigacionForm(instance=investigacion)
    return render(request, 'investigadores/investigacion_form.html', {'form':form, 'accion':'Modificar','a': id})

class Investigadores(View):

    def get(self, request):
        investigadores = list(Investigador.objects.all())

        def investigador_to_dic(investigador):
            investigaciones = Investigacion.objects.filter(autores=investigador.pk)
            categorias = []
            for investigacion in investigaciones:
                categorias.extend(list(map(lambda categoria: str(categoria),investigacion.categorias.all())))
                
            return {
                    "username": investigador.user.username,
                    "latitud": investigador.ubicacion.latitud,
                    "longitud": investigador.ubicacion.longitud,
                    "tipoUsuario": str(investigador.user.tipo_usuario),
                    "categorias": categorias
            }

        investigadores = list(map(investigador_to_dic, investigadores))

        return JsonResponse(list(investigadores), safe = False)
