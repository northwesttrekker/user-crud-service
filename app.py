from flask import Flask, request, jsonify, abort
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from models import User, db

# Configure the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'super-secret-flask'

# Configure Flask-JWT
def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)

jwt = JWT(app, authenticate, identity)

# Routes and endpoints
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
