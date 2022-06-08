from django import forms

from .models import Investigador, Investigacion, NivelInvestigador

class InvestigadorForm(forms.ModelForm):
    
    class Meta:
        model = Investigador 
        fields = '__all__'

        widgets = {
            'user': forms.Select(attrs={'class':'form-control'}),
            'ubicacion': forms.Select(attrs={'class':'form-control'}),
            'nivel': forms.Select(attrs={'class':'form-control'}),
            'curp': forms.TextInput(attrs={'class':'form-control'}),
        }

class InvestigacionForm(forms.ModelForm):
    
    class Meta:
        model = Investigacion
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'categorias': forms.SelectMultiple(attrs={'class':'form-control'}),
            'autores': forms.SelectMultiple(attrs={'class':'form-control'}),
            'contenido': forms.Textarea(attrs={'class':'form-control'}),
        }

class NivelInvestigadorForm(forms.ModelForm):
    
    class Meta:
        model = NivelInvestigador
        fields = '__all__'
