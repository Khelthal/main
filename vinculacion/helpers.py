from scholarly import scholarly, ProxyGenerator


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
