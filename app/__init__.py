import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import Flask
from flask_bootstrap import Bootstrap5

basedir = os.path.abspath(os.path.dirname(__file__))

flask_app = Flask(__name__)

flask_app.config['SECRET_KEY'] = "hard to unlock"
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_education'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap5(flask_app)
db = SQLAlchemy(flask_app)

from models import *
migrate = Migrate(flask_app, db)


