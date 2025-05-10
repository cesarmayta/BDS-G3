from flask_restful import Resource,Api
from flask import request
from . import bp_api


api = Api(bp_api)

class ApiResource(Resource):
    def get(self):
        context = {
            'status':True,
            'message':'API is working'
        }
        return context, 200

    
api.add_resource(ApiResource, '/')