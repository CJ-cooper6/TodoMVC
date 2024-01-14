import os
from flask import Flask
from flask_cors import CORS
from .configuration import config_provider
from backend import database as todo_db
from backend.database import db

def create_app():
    app = Flask(__name__)
    CORS(app)
    config_file_path = get_config_file_path()
    config_provider.load(config_file_path)
    todo_db.init_app(app)
    _register_blueprints(app)
    with app.app_context():
        db.create_all()
    return app


def _register_blueprints(app):
    from backend.api import bp as api
    app.register_blueprint(api, url_prefix="/api")


def get_config_file_path():
    from utils import get_project_root
    config_file = os.path.join(get_project_root(), f"conf/config.yml")
    return config_file