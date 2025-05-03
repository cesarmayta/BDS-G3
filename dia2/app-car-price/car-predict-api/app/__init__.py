from flask import Flask
from app.bp_web import bp_web
from app.bp_api import bp_api
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(bp_web, url_prefix='/')
    app.register_blueprint(bp_api, url_prefix='/api')
    return app