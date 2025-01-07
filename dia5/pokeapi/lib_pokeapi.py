import requests
import mysql.connector

class PokeAPI:
    
    def __init__(self,api_url='https://pokeapi.co/api/v2/'):
        self.api_url = api_url
        
    def get_pokemons(self,limit=1):
        url = f'{self.api_url}pokemon?limit={limit}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Error: {response.status_code}')
            return []
        
    def get_pokemon_detail(self,pokemon_url):
        response = requests.get(pokemon_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Error: {response.status_code}')
            return {}
    