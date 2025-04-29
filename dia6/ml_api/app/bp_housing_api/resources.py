from flask_restful import Resource,Api,abort
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
    
    def get_housing(self,id):
        housing = Housing.get_by_id(id)
        if not housing:
            abort(404, message="Casa no encontrada")
            
        return housing
    
    def get(self,id):
        housing = self.get_housing(id)
        data_schema = HousingSchema()
        
        context = {
            'status':True,
            'message':'Casa encontrada',
            'content': data_schema.dump(housing)
        }
        
        return context
    
    def put(self,id):
        data = request.get_json()
        rooms = int(data['rooms'])
        
        housing = self.get_housing(id)
        housing.rooms = rooms
        housing.save()
        
        data_schema = HousingSchema()
        
        context = {
            'status':True,
            'message':'Casa actualizada',
            'content': data_schema.dump(housing)
        }
        
        return context
    
    def delete(self,id):
        housing = self.get_housing(id)
        housing.delete()
        
        context = {
            'status':True,
            'message':'Casa eliminada',
        }
        
        return context, 204
    
api_housing.add_resource(HousingResource, '/')
api_housing.add_resource(HousingResourceDetail, '/<int:id>')