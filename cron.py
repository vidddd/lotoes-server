#!/usr/bin/python
from config.data import importadores_lista
from datetime import timedelta, datetime
from importing.get_data import get_sorteos_fecha
from functions.get_conn import get_conn_db, exists_sorteo
from api import db
from entities.sorteo import *
from sqlalchemy import exc
import json

today = datetime.today()

for importer in importadores_lista:
    url = importer[3]
    param_fecha = importer[4]
    dias = importer[5]
    if(param_fecha):
        fecha = (today + timedelta(dias)).strftime('%Y%m%d')
    else:
        fecha = today.strftime('%Y%m%d')
    
    result = get_sorteos_fecha(url, fecha)
    
    if type(result) is list:
        for sorteo in result:
            if(exists_sorteo(db,sorteo.get('id_sorteo'))):
                if len(str(sorteo.get('combinacion'))) > 250:
                            combinacion='',
                else: combinacion=sorteo.get('combinacion')
                s = Sorteo(fecha_sorteo=sorteo.get('fecha_sorteo'), 
                        dia_semana=sorteo.get('dia_semana'), 
                        id_sorteo=sorteo.get('id_sorteo'),
                        game_id=sorteo.get('game_id'),
                        anyo=sorteo.get('anyo'),
                        premio_bote=sorteo.get('premio_bote'),
                        cdc=sorteo.get('cdc'),
                        apuestas=sorteo.get('apuestas'),
                        recaudacion=sorteo.get('recaudacion'),
                        #combinacion=combinacion,
                        combinacion_json=json.dumps(sorteo.get('combinacion')),
                        premios=sorteo.get('premios'),
                        fondo_bote=sorteo.get('fondo_bote'),
                        escrutinio=sorteo.get('escrutinio'),
                        )
                db.session.add(s)
                db.session.commit()
            else:
                su = Sorteo.query.filter_by(id_sorteo=sorteo.get('id_sorteo')).first() 
                if su:
                    # if len(str(sorteo.get('combinacion'))) > 249:
                    #    combinacion='',
                    # else: combinacion=str(sorteo.get('combinacion'))
                    su.fecha_sorteo = sorteo.get('fecha_sorteo')
                    su.recaudacion=sorteo.get('recaudacion')
                    combinacion_json=json.dumps(sorteo.get('combinacion')),
                    su.premios=sorteo.get('premios')
                    su.fondo_bote=sorteo.get('fondo_bote')
                    su.escrutinio=sorteo.get('escrutinio')
                    db.session.add(su)
                    db.session.commit()
                    
    else: # Error no no hay datos
        print(result)

try:
    print()
except exc.SQLAlchemyError as e:
    print(str(e.__dict__['orig']))
    
