from flask_restful import Resource,Api
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
    
    
api.add_resource(CarApiResource, '/')