import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from flask import Flask, render_template, request,url_for


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

@app.route('/mujeres')
def mujeres():
    url = 'https://randomuser.me/api/?results=6&nat=es&gender=female'
    lista_contactos = requests.get(url).json()
    return render_template('mujeres.html',contactos=lista_contactos['results'])


@app.route('/grafico')
def grafico():
    url = 'https://randomuser.me/api/?results=100&nat=es'
    data = requests.get(url).json()
    results = data['results']
    lista_sexos =[user['gender'] for user in results]
    lista_edades = [user['dob']['age'] for user in results]
    
    df_users = pd.DataFrame({'sexo': lista_sexos, 'edad': lista_edades})
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_users, x='edad', hue='sexo', multiple='dodge', stat='count', bins=10)
    plt.title('Distribución de Edades por Sexo')
    plt.xlabel('Edad') 
    plt.ylabel('Cantidad')
    plt.legend(title='Sexo')
    grafico_path = os.path.join('static','images','grafico.png')
    plt.savefig(grafico_path)
    plt.close()
    
    return render_template('grafico.html', grafico_url=url_for('static', filename='images/grafico.png'))

app.run(debug=True)