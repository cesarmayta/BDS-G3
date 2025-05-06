from flask_restful import Resource,Api,abort
from flask import request
from . import bp_api
from .models import Car
from .schemas import CarSchema

api = Api(bp_api)

class CarApiResource(Resource):
    
    def get(self):
        
        data = Car.get_all()
        car_schema = CarSchema(many=True)
        
        context = {
            'status':True,
            'message':'lista de autos',
            'content':car_schema.dump(data)
        }
        
        return context,200
    
    def post(self):
        data = request.get_json()
        brand = data.get('brand')
        cylinders = data.get('cylinders')
        year = data.get('year')
        car = Car(brand, cylinders, year)
        car.save()
        
        data_schema = CarSchema()
        
        context = {
            'status':True,
            'message':'auto creado',
            'content':data_schema.dump(car)
        }
        return context,201
    
class CarApiResourceDetail(Resource):
    
    def get_car(self,id):
        housing = Car.get_by_id(id)
        if not housing:
            abort(404, message="auto no encontrado")
            
        return housing
    
    def get(self,id):
        data = self.get_car(id)
        data_schema = CarSchema()
        
        context = {
            'status':True,
            'message':'Casa encontrada',
            'content': data_schema.dump(data)
        }
        
        return context
    
    def put(self,id):
        data = request.get_json()
        
        
        car = self.get_car(id)
        car.brand = data.get('brand')
        car.cylinders = data.get('cylinders')
        car.year = data.get('year')
        car.save()
        
        data_schema = CarSchema()
        
        context = {
            'status':True,
            'message':'Casa actualizada',
            'content': data_schema.dump(car)
        }
        
        return context
    
    def delete(self,id):
        car = self.get_car(id)
        car.delete()
        
        context = {
            'status':True,
            'message':'Casa eliminada',
        }
        
        return context, 204
    
    
api.add_resource(CarApiResource, '/')
api.add_resource(CarApiResourceDetail, '/<int:id>')