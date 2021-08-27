from api import db
from sqlalchemy.dialects.postgresql import JSON


class Importer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    name_system = db.Column(db.String(50))
    active = db.Column(db.Boolean)
    sorteo_type = db.Column(db.String(50))
    url = db.Column(db.String())
    param_fecha = db.Column(db.Boolean)
    dias = db.Column(db.Integer)
    result = db.Column(JSON)

    def __init__(self, name, name_system, active, sorteo_type, url, param_fecha, dias, result):
        self.name = name
        self.name_system = name_system
        self.active = active
        self.sorteo_type = sorteo_type
        self.url = url
        self.param_fecha = param_fecha
        self.dias = dias
        self.result = result

    def __repr__(self):
        return '<id {}>'.format(self.id)
