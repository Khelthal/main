from django.contrib import admin
from investigadores.models import Investigador, NivelInvestigador, Investigacion

# Register your models here.
admin.site.register(Investigador)
admin.site.register(NivelInvestigador)
admin.site.register(Investigacion)
