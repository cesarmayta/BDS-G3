from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Flask Api',
        'message': 'Bienvenido a la API con Flask'
    }
    
    return jsonify(context)

app.run(debug=True)