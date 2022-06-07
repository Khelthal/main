from django import forms
from django.contrib.auth.models import User

from .models import TipoUsuario

class UserForm(forms.ModelForm):
    repassword = forms.CharField()
    class Meta:
        model = User
        fields = ('username','password','email','repassword')

class TipoUsuarioForm(forms.ModelForm):
    class Meta:
        model = TipoUsuario
        fields = '__all__'