from attr import fields
from django import forms
from django.contrib.auth.models import User

from .models import TipoUsuario, Ubicacion, InstitucionEducativa, Empresa

class UserForm(forms.ModelForm):
    repassword = forms.CharField()
    class Meta:
        model = User
        fields = ('username','password','email','repassword')

class TipoUsuarioForm(forms.ModelForm):
    class Meta:
        model = TipoUsuario
        fields = '__all__'

class UbiacionForm(models.Model):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class InstitucionEducativaForm(models.Model):
    class Meta:
        model = InstitucionEducativa
        exclude = ['user']

class EmpresaForm(models.Model):
    class Meta:
        model = Empresa
        exclude = ['user']