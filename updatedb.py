#!/usr/bin/python
from api import db

db.drop_all()
db.create_all()
