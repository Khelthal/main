from django import forms
from investigadores.models import Investigador
from usuarios.models import User
from administracion.validators import *

class FormInvestigador(forms.ModelForm):
    codigo_postal = forms.CharField(max_length=5, validators=[cp_validator])
    municipio = forms.CharField(max_length=100)
    colonia = forms.CharField(max_length=100)
    calle = forms.CharField(max_length=100)
    numero_exterior = forms.IntegerField(min_value=0)
    
    class Meta:
        model = Investigador
        exclude = ['latitud', 'longitud']

    def __init__(self, *args, **kwargs):
        super(FormInvestigador, self).__init__(*args, **kwargs)
        self.fields["user"].queryset = User.objects.filter(tipo_usuario__isnull=True)
        self.fields["curp"].widget.attrs['class'] = 'form-control'
        self.fields["curp"].widget.attrs['placeholder'] = 'Ingresa tu CURP'
        self.fields["codigo_postal"].widget.attrs['class'] = 'form-control'
        self.fields["codigo_postal"].widget.attrs['placeholder'] = 'Ingresa tu código postal de contacto'
        self.fields["municipio"].widget.attrs['class'] = 'form-control'
        self.fields["municipio"].widget.attrs['placeholder'] = 'Ingresa tu municipio de contacto'
        self.fields["colonia"].widget.attrs['class'] = 'form-control'
        self.fields["colonia"].widget.attrs['placeholder'] = 'Ingresa tu colonia de contacto'
        self.fields["calle"].widget.attrs['class'] = 'form-control'
        self.fields["calle"].widget.attrs['placeholder'] = 'Ingresa tu calle de contacto'
        self.fields["numero_exterior"].widget.attrs['class'] = 'form-control'
        self.fields["numero_exterior"].widget.attrs['placeholder'] = 'Ingresa tu número exterior de contacto'
