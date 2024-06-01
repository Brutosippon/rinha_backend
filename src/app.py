import logging
from flask import Flask, jsonify
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException
from controllers import person_bp
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

db.init_app(app)
migrate = Migrate(app, db) 

app.register_blueprint(person_bp)

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

@app.route('/')
def hello():
    return 'Hello, fidalgo docker is working!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)