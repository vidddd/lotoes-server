#!/usr/bin/python
from lotoesserver import db


class Loteria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    cp = db.Column(db.Integer)
    localidad = db.Column(db.String(100))
    telefono = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)
