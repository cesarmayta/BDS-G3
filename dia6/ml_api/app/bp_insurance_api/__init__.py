from flask import Blueprint,jsonify

bp_insurance_api = Blueprint('bp_insurance_api', __name__)

@bp_insurance_api.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Bienvenido a la API de insurance"}), 200