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
    
    def insert_pokemon_to_db(self,pokemons):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='datag3'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS pokemon(
                               id INT AUTO_INCREMENT PRIMARY KEY,
                               name VARCHAR(255),
                               height INT,
                               weight INT,
                               base_experience INT
                           )
                           """)
            connection.commit()
            for pokemon in pokemons:
                pokemon_detail = self.get_pokemon_detail(pokemon['url'])
                cursor.execute("""
                               INSERT INTO pokemon (name, height, weight, base_experience)
                               VALUES (%s, %s, %s, %s)
                               """, (pokemon['name'], pokemon_detail['height'], pokemon_detail['weight'], pokemon_detail['base_experience']))
                connection.commit()
                
            cursor.close()
            connection.close()