# coding=utf-8

from sqlalchemy import Column, String, Integer, DateTime

class Loteria():
    id = Column(Integer, primary_key=True)
    public_id = Column(String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)
