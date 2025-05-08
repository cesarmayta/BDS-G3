from airflow.models.operator import BaseOperator
import requests


class RequestOperator(BaseOperator):
    """
    Custom operator to make an HTTP request.
    """
    def __init__(self, url: str, **kwargs):
        super().__init__(**kwargs)
        self.url = url
        

    def execute(self, context):
        response = requests.get(self.url)
        users = []
        if response.status_code == 200:
            data = response.json()
            
            for usuario in data['results']:
                dict_usuario = {
                    'name': usuario['name'],
                    'location': usuario['location'],
                    'email': usuario['email'],
                    'phone': usuario['phone']
                }
                users.append(dict_usuario)
        else:
            print(f"algo salio mal {response.status_code}")
        return users