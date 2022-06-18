from django.shortcuts import render

# Create your views here.
def lista(request):
    investigadores = Investigador.objects.all()
    return render(request, "investigadores/investigadores.html", {"investigadores":investigadores})

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
    return render(request, 'investigadores/investigaciones.html', {'investigaciones':investigaciones})

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
