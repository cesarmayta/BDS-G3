from flask import Flask
from app.bp_web import bp_web
from app.bp_housing_api import bp_housing_api
from app.bp_insurance_api import bp_insurance_api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_web, url_prefix='/')
    app.register_blueprint(bp_housing_api, url_prefix='/api/housing')
    app.register_blueprint(bp_insurance_api, url_prefix='/api/insurance')
    return app