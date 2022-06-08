from django.contrib import admin
from usuarios.models import User, Ubicacion, TipoUsuario, InstitucionEducativa, Empresa

# Register your models here.
admin.site.register(User)
admin.site.register(Ubicacion)
admin.site.register(TipoUsuario)
admin.site.register(InstitucionEducativa)
admin.site.register(Empresa)
