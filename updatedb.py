#!/usr/bin/python
from api import db

print('Update Db')
db.drop_all()
db.create_all()
