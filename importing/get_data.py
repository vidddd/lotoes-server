import requests
import json


def get_sorteos_fecha(url, fecha):
    url = url + "&fecha_sorteo="+fecha
    response = requests.get(url)
    return response.json()
    
