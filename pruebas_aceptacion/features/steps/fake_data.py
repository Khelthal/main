from behave import given
from investigadores.models import NivelInvestigador, Investigador
from usuarios.models import User, TipoUsuario


def poblar_base_de_datos():
    if TipoUsuario.objects.count() != 3:
        TipoUsuario.objects.create(tipo="Investigador")
        TipoUsuario.objects.create(tipo="Empresa")
        TipoUsuario.objects.create(tipo="Institucion Educativa")
    NivelInvestigador.objects.create(
        nivel=1,
        descripcion="lorem"
    )
    User.objects.create(
        username="usuario_visitante",
        email="usuario@visitante.com",
        aprobado=False,
        is_active=True,
    )
    User.objects.create(
        username="usuario_investigador",
        email="usuario@investigador.com",
        aprobado=False,
        is_active=True,
    )
    Investigador.objects.create(
        nivel=NivelInvestigador.objects.get(nivel=1),
        acerca_de="a",
        calle="Esmeralda",
        codigo_postal=98613,
        colonia="Las joyas",
        curp="BEGE010204HZSLNLA5",
        latitud=0,
        longitud=0,
        municipio=16,
        numero_exterior=35,
        user=User.objects.get(username="usuario_investigador")
    )


@given(u'que inicio el sistema')
def step_impl(context):
    poblar_base_de_datos()
