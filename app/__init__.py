import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_mail import Mail

basedir = os.path.abspath(os.path.dirname(__file__))

flask_app = Flask(__name__)

flask_app.config['SECRET_KEY'] = "hard to unlock"
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_education'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

flask_app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
flask_app.config['MAIL_PORT'] = 587
flask_app.config['MAIL_USE_TLS'] = True
flask_app.config["MAIL_USERNAME"] = "alextesttestovik@gmail.com"
flask_app.config["MAIL_PASSWORD"] = "jhkq wdsa hbei uyil"


bootstrap = Bootstrap5(flask_app)
db = SQLAlchemy(flask_app)
mail = Mail(flask_app)

from models import *
migrate = Migrate(flask_app, db)


