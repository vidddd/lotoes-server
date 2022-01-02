#!/usr/bin/python
from config.data import importadores_lista
from datetime import timedelta, datetime
from importing.get_data import get_sorteos_fecha
from functions.get_conn import get_conn_db, exists_sorteo, get_sorteo_id_bbdd
from api import db
from entities.sorteo import *
from sqlalchemy import exc
import json
from pprint import pprint

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
                s = Sorteo(
                        nombre=sorteo.get('nombre'),
                        fecha_sorteo=sorteo.get('fecha_sorteo'), 
                        dia_semana=sorteo.get('dia_semana'), 
                        id_sorteo=sorteo.get('id_sorteo'),
                        game_id=sorteo.get('game_id'),
                        anyo=sorteo.get('anyo'),
                        numero_sorteo=sorteo.get('num_sorteo'),
                        lugar=sorteo.get('lugar'),
                        premio_bote=sorteo.get('premio_bote'),
                        cdc=sorteo.get('cdc'),
                        apuestas=sorteo.get('apuestas'),
                        recaudacion=sorteo.get('recaudacion'),
                        combinacion_json=json.dumps(sorteo.get('combinacion')),
                        premios=sorteo.get('premios'),
                        fondo_bote=sorteo.get('fondo_bote'),
                        escrutinio=sorteo.get('escrutinio'),
                        )
                db.session.add(s)
                try:
                    db.session.commit()
                except exc.SQLAlchemyError as e:
                    print('add '+sorteo.get('id_sorteo')+ ' '+sorteo.get('dia_semana')+ ' ' +sorteo.get('game_id'))
                    print(str(e.__dict__['orig']))
            else:
                id_sorteo=sorteo.get('id_sorteo')
                sorteo_id = get_sorteo_id_bbdd(db,id_sorteo)
                su = Sorteo.query.filter_by(id_sorteo=id_sorteo).first()
                if su:
                    su.fecha_sorteo = sorteo.get('fecha_sorteo')
                    su.recaudacion=sorteo.get('recaudacion')
                    su.combinacion_json=json.dumps(sorteo.get('combinacion')),
                    su.premios=sorteo.get('premios')
                    su.fondo_bote=sorteo.get('fondo_bote')
                    su.escrutinio=sorteo.get('escrutinio')
                    su.apuestas=sorteo.get('apuestas')
                    
                    if(su.game_id == 'LNAC'):
                        lnaccomb = LoteriaNacionalCombinacion(
                                sorteo_id = sorteo_id,
                                primer_premio = sorteo.get('combinacion').get('primer_premio'),
                                segundo_premio = sorteo.get('combinacion').get('segundo_premio'),
                                tercer_premio = sorteo.get('combinacion').get('tercer_premio'),
                                fraccion = sorteo.get('combinacion').get('fraccion'),
                                serie = sorteo.get('combinacion').get('serie'))
                        db.session.add(lnaccomb)
                        
                    if(su.game_id == 'BONO'):
                        combinacion = sorteo.get('combinacion')
                        print(combinacion)
                        
                        '''
                        bonocomb = BonolotoCombinacion(
                                sorteo_id = sorteo_id,
                                bola_1 = ,
                                bola_2 = ,
                                bola_3 = ,
                                bola_4 = ,
                                bola_5 = 
                                bola_6 =
                                reintegro = 
                        db.session.add(bonocomb)
                        '''
                    
                    if(su.game_id == 'LAPR'):
                        print('LAPR')
                    
                    if(su.game_id == 'ELGR'):
                        print('ELGR')
                    
                    if(su.game_id == 'LNAC'):
                        print('LANC')
                    
                             
                    
                    db.session.add(su)
                    
                    try:
                        db.session.commit()
                    except exc.SQLAlchemyError as e:
                        print('update '+sorteo.get('id_sorteo')+ ' '+sorteo.get('dia_semana')+ ' ' +sorteo.get('game_id'))
                        print(str(e.__dict__['orig']))
                    
    else: # Error no no hay datos
        print(result)


    
