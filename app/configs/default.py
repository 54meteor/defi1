import os

ROOT_PATH = os.path.split(os.path.abspath(__name__))[0]

DEBUG = True
SECRET_KEY = 'CEIqefXLmpdKDeWbjsxhgQNtNCgKbIcfDeRCWC'
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/defi'
SQLALCHEMY_TRACK_MODIFICATIONS = False

CELERY_TIMEZONE = 'Asia/Shanghai'
BROKER_URL = 'sqla+sqlite:///celerydb.sqlite'  # CELERY_BROKER_URL
CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'

