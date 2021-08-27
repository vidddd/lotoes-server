#!/usr/bin/python
from api import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, public_id, name, password, admin, created_at, updated_at):
        self.url = url
        self.name = name
        self.password = password
        self.admin = admin
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
