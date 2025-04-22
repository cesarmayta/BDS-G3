from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1><center>Hola mundo con Flask!</center></h1>"

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre', 'Mundo')
    return f"<h1><center>Hola {nombre}!</center></h1>"

@app.route('/sumar')
def suma():
    try:
        num1 = int(request.args.get('num1', 0))
        num2 = int(request.args.get('num2', 0))
        resultado = num1 + num2
        return f"<h1><center>La suma de {num1} y {num2} es {resultado}</center></h1>"
    except ValueError:
        return "<h1><center>Error: Por favor, ingrese números válidos.</center></h1>"
    
@app.route('/restar/<int:num1>/<int:num2>')
def resta(num1, num2):
    resultado = num1 - num2
    return f"<h1><center>La resta de {num1} y {num2} es {resultado}</center></h1>"

# crear una ruta en donde yo coloque la operacion/n1/n2 ejem suma/3/4 resta/4/2 multiplicacion/2/1 division/4/2
# la función debe llamarse operaciones

@app.route('/<operacion>/<int:num1>/<int:num2>')
def operaciones(operacion, num1, num2):
    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
    elif operacion == 'division':
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "<h1><center>Error: División por cero no permitida.</center></h1>"
    else:
        return "<h1><center>Error: Operación no válida.</center></h1>"
    
    return f"<h1><center>El resultado de {operacion} entre {num1} y {num2} es {resultado}</center></h1>"

app.run(debug=True)