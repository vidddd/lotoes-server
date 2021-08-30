#!/usr/bin/python
from api import db
from sqlalchemy.dialects.postgresql import JSON

class Sorteo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_sorteo = db.Column(db.String(20))
    dia_semana = db.Column(db.String(10))
    id_sorteo = db.Column(db.Integer, unique=True)
    game_id = db.Column(db.String(5))
    anyo = db.Column(db.Integer)
    premio_bote = db.Column(db.Integer)
    cdc = db.Column(db.Integer)
    apuestas = db.Column(db.Integer)
    recaudacion = db.Column(db.Integer)
    combinacion = db.Column(db.Integer)
    premios = db.Column(db.Integer)
    fondo_bote = db.Column(db.Integer)
    escrutinio = db.Column(JSON)
