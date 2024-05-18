from flask import Flask
from .controllers import person_bp
from .models import db
#from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
#migrate = Migrate(app, db)
app.register_blueprint(person_bp)

@app.route('/')
def hello():
    return 'Hello, fidalgo docker is working!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)
