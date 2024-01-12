from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    _register_blueprints(app)
    print("create_app")
    return app



def _register_blueprints(app):
    from todo.api import bp as api
    app.register_blueprint(api, url_prefix="/api")
    print("_register_blueprints")