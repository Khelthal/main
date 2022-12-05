from vinculacion.models import AreaConocimiento, Categoria, Noticia


def crear_area_conocimiento(nombre, descripcion):
    area_conocimiento = AreaConocimiento.objects.create(
        nombre=nombre,
        descripcion=descripcion
    )

    return area_conocimiento

def crear_categoria(nombre, area_conocimiento, descripcion):
    categoria = Categoria.objects.create(
        nombre=nombre,
        area_conocimiento=area_conocimiento,
        descripcion=descripcion
    )
    return categoria

def crear_noticia(titulo, contenido, escritor, imagen):
    noticia = Noticia.objects.create(
        titulo=titulo,
        contenido=contenido,
        escritor=escritor,
        imagen=imagen
    )
    return noticia