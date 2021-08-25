from flask import Flask, request, jsonify
from config import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

params_general = config('general')
params_postgres = config()

SECRET_KEY = params_general["secret_key"]
HOST = params_postgres["host"]
DATABASE = params_postgres["database"]
USERNAME = params_postgres["user"]
PASSWORD = params_postgres["password"]

DATABASE_CONNECTION = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'

app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from entities import Result

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)


class Loteria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    localidad = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)


@app.route('/')
def index():
    return 'Hello, Lotoes Server'


@app.route('/user', methods=['GET'])
def get_all_users():
    return ''


@app.route('/user/<public_id>', methods=['GET'])
def get_one_user():
    return''


# Default port:
if __name__ == '__main__':
    app.run(debug=True)

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
