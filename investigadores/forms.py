from django import forms
from .models import SolicitudTrabajo

class SolicitudTrabajoForm(forms.ModelForm):
    class Meta:
        model = SolicitudTrabajo
        fields = ('titulo','descripcion')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control form-control-xl', 'placeholder':'Título del trabajo'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control form-control-xl', 'placeholder':'Decripción del trabajo'}),
        }