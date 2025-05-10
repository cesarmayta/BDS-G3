from flask import Flask
from app.bp_api import bp_api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_api, url_prefix='/')
    return app