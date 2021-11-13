from flask import Flask
import os
basedir = os.path.abspath(os.path.dirname(__file__))
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#instance of Flask class
myweb = Flask(__name__)

myweb.config.from_mapping(
    SECRET_KEY = 'you-will-know',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'web.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(myweb)

from website import routes, models