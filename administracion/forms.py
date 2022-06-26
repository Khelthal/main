from django import forms
from usuarios.models import User
from investigadores.models import Investigador, Investigacion
from empresas.models import Empresa
from vinculacion.models import Categoria
from instituciones_educativas.models import InstitucionEducativa
from administracion.validators import *

class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }

    def save(self, commit=True):
        user = super(FormUser, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class FormInvestigador(forms.ModelForm):
    codigo_postal = forms.CharField(max_length=5, validators=[cp_validator])
    municipio = forms.CharField(max_length=100)
    colonia = forms.CharField(max_length=100)
    calle = forms.CharField(max_length=100)
    numero_exterior = forms.IntegerField(min_value=0)
    
    class Meta:
        model = Investigador
        exclude = ['latitud', 'longitud', 'aprobado']

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

class FormInvestigadorUpdate(forms.ModelForm):
    codigo_postal = forms.CharField(max_length=5, validators=[cp_validator])
    municipio = forms.CharField(max_length=100)
    colonia = forms.CharField(max_length=100)
    calle = forms.CharField(max_length=100)
    numero_exterior = forms.IntegerField(min_value=0)
    
    class Meta:
        model = Investigador
        exclude = ['latitud', 'longitud', 'user', 'aprobado']

    def __init__(self, *args, **kwargs):
        super(FormInvestigadorUpdate, self).__init__(*args, **kwargs)
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

class FormEmpresa(forms.ModelForm):
    codigo_postal = forms.CharField(max_length=5, validators=[cp_validator])
    municipio = forms.CharField(max_length=100)
    colonia = forms.CharField(max_length=100)
    calle = forms.CharField(max_length=100)
    numero_exterior = forms.IntegerField(min_value=0)
    
    class Meta:
        model = Empresa
        exclude = ['latitud', 'longitud', 'aprobado']

    def __init__(self, *args, **kwargs):
        super(FormEmpresa, self).__init__(*args, **kwargs)
        self.fields["encargado"].queryset = User.objects.filter(tipo_usuario__isnull=True)
        self.fields["nombre_empresa"].widget.attrs['class'] = 'form-control'
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

class FormEmpresaUpdate(forms.ModelForm):
    codigo_postal = forms.CharField(max_length=5, validators=[cp_validator])
    municipio = forms.CharField(max_length=100)
    colonia = forms.CharField(max_length=100)
    calle = forms.CharField(max_length=100)
    numero_exterior = forms.IntegerField(min_value=0)
    
    class Meta:
        model = Empresa
        exclude = ['latitud', 'longitud', 'encargado', 'aprobado']

    def __init__(self, *args, **kwargs):
        super(FormEmpresaUpdate, self).__init__(*args, **kwargs)
        self.fields["nombre_empresa"].widget.attrs['class'] = 'form-control'
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

class FormInstitucionEducativa(forms.ModelForm):
    codigo_postal = forms.CharField(max_length=5, validators=[cp_validator])
    municipio = forms.CharField(max_length=100)
    colonia = forms.CharField(max_length=100)
    calle = forms.CharField(max_length=100)
    numero_exterior = forms.IntegerField(min_value=0)
    
    class Meta:
        model = InstitucionEducativa
        exclude = ['latitud', 'longitud', 'aprobado']

    def __init__(self, *args, **kwargs):
        super(FormInstitucionEducativa, self).__init__(*args, **kwargs)
        self.fields["encargado"].queryset = User.objects.filter(tipo_usuario__isnull=True)
        self.fields["nombre_institucion"].widget.attrs['class'] = 'form-control'
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

class FormInstitucionEducativaUpdate(forms.ModelForm):
    codigo_postal = forms.CharField(max_length=5, validators=[cp_validator])
    municipio = forms.CharField(max_length=100)
    colonia = forms.CharField(max_length=100)
    calle = forms.CharField(max_length=100)
    numero_exterior = forms.IntegerField(min_value=0)
    
    class Meta:
        model = InstitucionEducativa
        exclude = ['latitud', 'longitud', 'encargado', 'aprobado']

    def __init__(self, *args, **kwargs):
        super(FormInstitucionEducativaUpdate, self).__init__(*args, **kwargs)
        self.fields["nombre_institucion"].widget.attrs['class'] = 'form-control'
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

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
        }

class FormInvestigacion(forms.ModelForm):
    class Meta:
        model = Investigacion
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'categorias': forms.SelectMultiple(attrs={'class':'choices form-select multiple-remove'}),
            'autores': forms.SelectMultiple(attrs={'class':'choices form-select multiple-remove'}),
            'contenido': forms.Textarea(attrs={'class':'form-control'}),
        }
