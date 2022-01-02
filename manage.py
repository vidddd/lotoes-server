#!/usr/bin/python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configload import config
from flask_migrate import Migrate

app = Flask(__name__)

params_postgres = config()

HOST = params_postgres["host"]
DATABASE = params_postgres["database"]

DATABASE_CONNECTION = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION

db = SQLAlchemy(app)


migrate = Migrate(app, db)  # Initializing migrate.

# import entities
from entities.user import *
from entities.loteria import *
from entities.importer import *

from entities.sorteo import *

db.init_app(app)
migrate.init_app(app, db)

db.drop_all()
db.create_all()
