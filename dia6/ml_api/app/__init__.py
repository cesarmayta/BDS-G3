from flask import Flask
from app.bp_web import bp_web

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_web, url_prefix='/')
    return app