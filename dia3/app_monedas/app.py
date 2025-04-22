from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    resultado = 0
    
    if request.method == 'POST':
        origen = request.form['origen']
        resultado = int(origen) / 3.7
    
    
    nombre_request = request.args.get('nombre', 'Mundo')
    return render_template('index.html',nombre=nombre_request,destino=round(resultado,2))

app.run(debug=True)