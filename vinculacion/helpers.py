from scholarly import scholarly, ProxyGenerator
from investigadores.models import Investigador
from empresas.models import Empresa
from instituciones_educativas.models import InstitucionEducativa


def get_author(user_id):
    pg = ProxyGenerator()
    pg.FreeProxies()
    scholarly.use_proxy(pg)

    try:
        return scholarly.search_author_id(user_id, filled=True)
    except Exception:
        return None


def get_publications(author):
    pg = ProxyGenerator()
    pg.FreeProxies()
    scholarly.use_proxy(pg)

    publicaciones = []

    for publication in author["publications"]:
        try:
            publication = scholarly.fill(publication)
        except Exception:
            pass

        titulo = publication.get("bib", {}).get("title")

        if not titulo:
            continue

        abstract = publication.get("bib", {}).get(
            "abstract", "Contenido no encontrado")
        pub_url = publication.get("pub_url")

        if pub_url:
            abstract += f"\n\nVer más: {pub_url}"

        publicaciones.append({
            "titulo": titulo,
            "contenido": abstract,
        })

    return publicaciones


def get_user_specific_data(usuario):
    tipo_usuario = "_".join(usuario.tipo_usuario.tipo.split()).lower()

    if tipo_usuario == "investigador":
        usuario_investigador = Investigador.objects.get(user=usuario)
        usuario_data = {
            'email': usuario_investigador.user.email,
            'imagen': usuario_investigador.imagen,
        }

    elif tipo_usuario == "empresa":
        usuario_empresa = Empresa.objects.get(encargado=usuario)
        usuario_data = {
            'email': usuario_empresa.encargado.email,
            'imagen': usuario_empresa.imagen,
        }

    elif tipo_usuario == "institucion_educativa":
        usuario_institucion = InstitucionEducativa.objects.get(
            encargado=usuario)
        usuario_data = {
            'email': usuario_institucion.encargado.email,
            'imagen': usuario_institucion.imagen,
        }

    return usuario_data
