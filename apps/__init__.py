from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from config import config

db = SQLAlchemy()


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from .asset import asset as asset_blueprint
    app.register_blueprint(asset_blueprint)

    from .system_user import system_user as system_user_blueprint
    app.register_blueprint(system_user_blueprint)

    return app
