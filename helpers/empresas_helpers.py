from empresas.models import Empresa

def crear_empresa(
    encargado,
    nombre_empresa,
    especialidades,
    latitud,
    longitud,
    codigo_postal,
    municipio,
    colonia,
    calle,
    numero_exterior,
    acerca_de,
    imagen
):
    empresa = Empresa.objects.create(
        encargado=encargado,
        nombre_empresa=nombre_empresa,
        latitud=latitud,
        longitud=longitud,
        codigo_postal=codigo_postal,
        municipio=municipio,
        colonia=colonia,
        calle=calle,
        numero_exterior=numero_exterior,
        acerca_de=acerca_de,
        imagen=imagen
    )

    for especialidad in especialidades:
        empresa.especialidades.add(especialidad)

    return empresa