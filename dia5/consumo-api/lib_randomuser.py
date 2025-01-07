import requests
import mysql.connector

class RandomUserApi:
    
    def __init__(self, api_url = 'https://randomuser.me/api'):
        self.api_url = api_url
    
    def get_users(self,results=1):
        url = self.api_url + f"?results={results}&nat=es&noinfo"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['results']
        else:
            print(f"Error: {response.status_code}")
            return []