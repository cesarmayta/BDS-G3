from flask import Blueprint

bp_housing_api = Blueprint('bp_housing_api', __name__)

from . import resources
