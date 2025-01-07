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
        
    def insert_users_to_db(self,users):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='datag3'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS usuarios (
                                 id INT AUTO_INCREMENT PRIMARY KEY,
                                 nombre VARCHAR(255),
                                 pais VARCHAR(255),
                                 correo VARCHAR(255),
                                 telefono VARCHAR(255),
                                 foto VARCHAR(255)
                            )
                           """)
            for user in users:
                cursor.execute("""
                               INSERT INTO usuarios (nombre, pais, correo, telefono, foto)
                               VALUES (%s, %s, %s, %s, %s)
                               """, (
                                   f"{user['name']['first']} {user['name']['last']}",
                                   user['location']['country'],
                                   user['email'],
                                   user['phone'],
                                   user['picture']['large']
                               ))
                connection.commit()