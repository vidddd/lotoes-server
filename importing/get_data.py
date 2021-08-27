import request
import json

def get_sorteos_fecha(url, fecha):
    url = url + ""
    response = requests.get(url)
