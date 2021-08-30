from flask import Flask, request, jsonify
from configload import config
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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from entities.user import *

@app.route('/')
def index():
    return 'Hello, Lotoes Server'


@app.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name

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
