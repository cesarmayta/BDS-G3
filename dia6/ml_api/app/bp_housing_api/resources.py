from flask_restful import Resource,Api
from flask import request

from . import bp_housing_api
from .models import Housing
from .schemas import HousingSchema

api_housing = Api(bp_housing_api)

class HousingResource(Resource):
    
    def get(self):
        
        data = Housing.get_all()
        data_schema = HousingSchema(many=True)       
        
        context = {
            'status':True,
            'message':'Lista de casas',
            'content': data_schema.dump(data)
        }
        
        return context, 200
    
api_housing.add_resource(HousingResource, '/')