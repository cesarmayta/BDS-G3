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
    
    def post(self):
        data = request.get_json()
        rooms = int(data['rooms'])
        
        housing = Housing(rooms=rooms)
        housing.save()
        
        data_schema = HousingSchema()
        
        context = {
            'status':True,
            'message':'Casa creada',
            'content': data_schema.dump(housing)
        }
        
        return context, 201
    
class HousingResourceDetail(Resource):
    
    def get(self,id):
        data = Housing.get_by_id(id)
        data_schema = HousingSchema()
        
        context = {
            'status':True,
            'message':'Casa encontrada',
            'content': data_schema.dump(data)
        }
        
        return context
    
    def put(self,id):
        data = request.get_json()
        rooms = int(data['rooms'])
        
        housing = Housing.get_by_id(id)
        housing.rooms = rooms
        housing.save()
        
        data_schema = HousingSchema()
        
        context = {
            'status':True,
            'message':'Casa actualizada',
            'content': data_schema.dump(housing)
        }
        
        return context
    
api_housing.add_resource(HousingResource, '/')
api_housing.add_resource(HousingResourceDetail, '/<int:id>')