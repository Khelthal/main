from investigadores.models import Investigador, NivelInvestigador

def crear_nivel_investigador(nivel, descripcion):
    nivel_investigador = NivelInvestigador.objects.create(
        nivel=nivel,
        descripcion=descripcion
    )
    return nivel_investigador

def crear_investigador(usuario, nivel, curp, latitud, longitud, codigo_postal, municipio, colonia, calle, numero_exterior, acerca_de):
    investigador = Investigador.objects.create(
            user=usuario,
            nivel=nivel,
            curp=curp,
            latitud=latitud,
            longitud=longitud,
            codigo_postal=codigo_postal,
            municipio=municipio,
            colonia=colonia,
            calle=calle,
            numero_exterior=numero_exterior,
            acerca_de=acerca_de
        )
    return investigador