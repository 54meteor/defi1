from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from celery import Celery
import pymysql
from hobbit_core import HobbitManager

pymysql.install_as_MySQLdb()
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
celery = Celery()
hobbit = HobbitManager()
