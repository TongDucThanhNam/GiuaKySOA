from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
login = LoginManager()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .transaction import transaction as transaction_blueprint
    app.register_blueprint(transaction_blueprint, url_prefix='/transaction')

    return app
