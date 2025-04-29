from flask import Blueprint,jsonify

bp_housing_api = Blueprint('bp_housing_api', __name__)

@bp_housing_api.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Bienvenido a la API de Housing"}), 200