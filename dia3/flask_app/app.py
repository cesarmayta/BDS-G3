from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1><center>Hola mundo con Flask!</center></h1>"

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre', 'Mundo')
    return f"<h1><center>Hola {nombre}!</center></h1>"


app.run(debug=True)