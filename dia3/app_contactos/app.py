import requests
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://randomuser.me/api/?results=3&nat=es'
    lista_contactos = requests.get(url).json()
    print(lista_contactos)
    return render_template('index.html',contactos=lista_contactos['results'])

app.run(debug=True)