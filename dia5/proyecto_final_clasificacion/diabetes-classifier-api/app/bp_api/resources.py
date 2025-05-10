from flask_restful import Resource,Api,abort
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
        

class ApiResourceDetail(Resource):
    
    def get_object(self,id):
        diabetes = Diabetes.get_by_id(id)
        if not diabetes:
            abort(404, message="Diabetes record not found")
        return diabetes
    
    def get(self,id):
        diabetes = self.get_object(id)
        diabetes_schema = DiabetesSchema()
        
        context = {
            'status':True,
            'message':'registro encontrado',
            'content':diabetes_schema.dump(diabetes)
        }
        return context, 200
    
    def put(self,id):
        data = request.get_json()
        if not data:
            return {'status': False, 'message': 'No data provided'}, 400

        glucose = data.get('glucose')
        age = data.get('age')
        bmi = data.get('bmi')
        
        diabetes = self.get_object(id)
        
        if glucose:
            diabetes.glucose = glucose
        if age:
            diabetes.age = age
        if bmi:
            diabetes.bmi = bmi
        
        diabetes.save()
        
        diabetes_schema = DiabetesSchema()
        
        context = {
            'status':True,
            'message':'registro actualizado',
            'content':diabetes_schema.dump(diabetes)
        }
        return context, 200
    
    def delete(self,id):
        diabetes = self.get_object(id)
        diabetes.delete()
        
        context = {
            'status':True,
            'message':'registro eliminado',
            'content':None
        }
        return context, 204

    
api.add_resource(ApiResource, '/')
api.add_resource(ApiResourceDetail, '/<int:id>')