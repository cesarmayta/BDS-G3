import requests
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://randomuser.me/api/?results=6&nat=es'
    lista_contactos = requests.get(url).json()
    return render_template('index.html',contactos=lista_contactos['results'])

@app.route('/hombres')
def hombres():
    url = 'https://randomuser.me/api/?results=6&nat=es&gender=male'
    lista_contactos = requests.get(url).json()
    return render_template('hombres.html',contactos=lista_contactos['results'])

app.run(debug=True)