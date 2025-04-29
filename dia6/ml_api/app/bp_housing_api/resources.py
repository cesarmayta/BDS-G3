from flask_restful import Resource,Api
from flask import request

from . import bp_housing_api

api_housing = Api(bp_housing_api)

class HousingResource(Resource):
    
    def get(self):
        context = {
            'status':True,
            'message':'Lista de casas'
        }
        
        return context, 200
    
api_housing.add_resource(HousingResource, '/')