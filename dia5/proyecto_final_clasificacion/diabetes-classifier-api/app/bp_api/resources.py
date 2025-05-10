from flask_restful import Resource,Api
from flask import request
from . import bp_api
from .models import Diabetes
from .schemas import DiabetesSchema


api = Api(bp_api)

class ApiResource(Resource):
    def get(self):
        
        data = Diabetes.get_all()
        diabetes_schema = DiabetesSchema(many=True)
        
        context = {
            'status':True,
            'message':'lista de registros',
            'content':diabetes_schema.dump(data)
        }
        return context, 200
    
    def post(self):
        data = request.get_json()
        if not data:
            return {'status': False, 'message': 'No data provided'}, 400

        glucose = data.get('glucose')
        age = data.get('age')
        bmi = data.get('bmi')
        
        diabetes = Diabetes(glucose=glucose, age=age, bmi=bmi)
        diabetes.save()
        
        diabetes_schema = DiabetesSchema()
        
        try:
            context = {
            'status':True,
            'message':'registro creado',
            'content':diabetes_schema.dump(diabetes)
            }
            return context,201
        except Exception as e:
            return {'status': False, 'message': str(e)}, 500

    
api.add_resource(ApiResource, '/')