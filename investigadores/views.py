from django.shortcuts import render
from django.urls import reverse_lazy
from investigadores.models import Investigador
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect

def lista(request):
    investigadores = Investigador.objects.all()
    return render(request, "lista.html", {"investigadores":investigadores})

class EliminarInvestigadorView(LoginRequiredMixin,DeleteView):
    model = Investigador
    extra_context = {'accion':'Eliminar'}
    success_url = reverse_lazy('usuarios:lista')
    
    def form_valid(self,form):
        try:
            self.object.delete()
            messages.success(self.request, 'Se eliminó el investigador')
        except:
            messages.error(self.request, 'Error al guardar los cambios')

        return HttpResponseRedirect(self.success_url)
        
    def form_invalid(self, form):
        messages.error(self.request,"Hubo uno o más errores en el formulario") 