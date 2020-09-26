import importlib
import logging


from flask import Flask, request
from flask.helpers import get_env
from flask_apscheduler import APScheduler
scheduler = APScheduler()

from hobbit_core.err_handler import ErrHandler

from app.exts import db, migrate, ma, hobbit, celery


class Config(object):
    JOBS = [
        {
            'id': 'checkBuyMiner',
            'func': 'app.tasks.planjob:chain_search',
            'args': "",
            'trigger': 'interval',
            'seconds': 1200
        },{
            'id': 'setReward',
            'func': 'app.tasks.planjob:set_reward',
            'args': "",
            # 'trigger': 'interval',
            # 'seconds': 10
            'trigger': 'cron',
            'hour': 0,
            'minute': 20
        },{
            'id': 'Reward',
            'func': 'app.tasks.planjob:reward',
            'args': "",
            'trigger': 'cron',
            'hour': 0,
            'minute': 10
        }
    ]
    SCHEDULER_API_ENABLED = True


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    hobbit.init_app(app, db)



def register_blueprints(app):
    from app import views
    for name in views.__all__:
        bp = getattr(importlib.import_module(f'app.views.{name}'), 'bp', None)
        if bp is not None:
            app.register_blueprint(bp, url_prefix='/api')


def register_error_handler(app):
    app.register_error_handler(Exception, ErrHandler.handler)


def register_cmds(app):
    pass


def make_celery(app):
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    from app import tasks  # NOQA
    return celery


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('app.configs.{}'.format(get_env()))
    app.config.from_object(Config())
    with app.app_context():
        register_extensions(app)
        register_blueprints(app)
    register_error_handler(app)
    register_cmds(app)
    make_celery(app)

    scheduler.init_app(app)
    scheduler.start()
    @app.before_request
    def log_request_info():
        logger = logging.getLogger('werkzeug')
        if request.method in ['POST', 'PUT']:
            logger.info('Body: %s', request.get_data())

    return app


app = create_app()
