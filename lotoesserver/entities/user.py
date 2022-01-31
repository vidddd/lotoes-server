#!/usr/bin/python
from lotoesserver import db
from datetime import datetime


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    email = db.Column(db.String(100))
    admin = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, public_id, name, password, email, admin, created_at, updated_at):
        self.url = url
        self.name = name
        self.password = password
        self.email = email
        self.admin = admin
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
