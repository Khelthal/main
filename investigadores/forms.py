from attr import fields
from django import forms

from .models import Investigador, Investigacion, NivelInvestigador

class InvestigadorForm(forms.ModelForm):
    
    class Meta:
        model = Investigador 
        exclude = ['user']

class InvestigacionForm(forms.ModelForm):
    
    class Meta:
        model = Investigacion
        fields = '__all__'

class NivelInvestigadorForm(forms.ModelForm):
    
    class Meta:
        model = NivelInvestigador
        fields = '__all__'
