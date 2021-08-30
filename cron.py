#!/usr/bin/python
from config.data import importadores_lista
from datetime import datetime
from importing.get_data import get_sorteos_fecha
from functions.get_conn import get_conn_db
from api import db
from entities.sorteo import *

today = datetime.today().strftime('%Y%m%d')

for importer in importadores_lista:
    url = importer[4]
    result = get_sorteos_fecha(url, today)
    if type(result) is list:
        for sorteo in result:
            s = Sorteo(fecha_sorteo=sorteo.get('fecha_sorteo'), 
                       dia_semana=sorteo.get('dia_semana'), 
                       id_sorteo=sorteo.get('id_sorteo'),
                       game_id=sorteo.get('game_id'),
                       anyo=sorteo.get('anyo'),
                       premio_bote=sorteo.get('premio_bote'),
                       cdc=sorteo.get('cdc'),
                       apuestas=sorteo.get('apuestas'),
                       recaudacion=sorteo.get('recaudacion'),
                       combinacion=sorteo.get('combinacion'),
                       premios=sorteo.get('premios'),
                       fondo_bote=sorteo.get('fondo_bote'),
                       escrutinio=sorteo.get('escrutinio'),
                    )
            db.session.add(s)
    else: # Error no no hay datos
        print(result)

db.session.commit()