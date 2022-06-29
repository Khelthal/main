import requests
import json

class Coordenadas:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud


def obtener_coordenadas(cleaned_data):
    codigo_postal = cleaned_data['codigo_postal']
    municipio = cleaned_data['municipio']
    colonia = cleaned_data['colonia']
    calle = cleaned_data['calle']
    numero_exterior = cleaned_data['numero_exterior']
    
    headers = {
        'User-agent': 'Script de consulta de ubicacion'
    }
    r = requests.get(f"https://nominatim.openstreetmap.org/search?street='{numero_exterior} {calle}'&city={municipio}&country=Mexico&state=Zacatecas&postalcode={codigo_postal}&format=json", headers=headers)
    
    if r.status_code != 200:
        return None

    data = json.loads(r.text)
    
    if len(data) == 0:
        return None
        
    data = data[0]

    if "lat" not in data or "lon" not in data:
        return None

    return Coordenadas(float(data["lat"]), float(data["lon"]))
