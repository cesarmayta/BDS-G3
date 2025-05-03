from flask_restful import Resource,Api
from . import bp_api

api = Api(bp_api)

class CarApiResource(Resource):
    
    def get(self):
        
        context = {
            'status':True,
            'message':'lista de autos',
        }
        
        return context,200
    
    
api.add_resource(CarApiResource, '/')