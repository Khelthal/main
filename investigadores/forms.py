from attr import fields
from django import forms

from .models import Investigador

class InvestigadorForm(forms.ModelForm):
    
    class Meta:
        model = Investigador 
        exclude = ['user']