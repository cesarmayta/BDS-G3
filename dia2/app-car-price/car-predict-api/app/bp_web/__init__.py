from flask import Blueprint

bp_web = Blueprint('bp_web', __name__)

from . import views