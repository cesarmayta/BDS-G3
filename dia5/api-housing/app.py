from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.app_context().push()
### CREAMOS NUESTRA PRIMER TABLA USANDO EL ORM DE SQLALCHEMY ###
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/db_mlg3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Housing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rooms = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Double,nullable=True)
    
    def __init__(self, rooms):
        self.rooms = rooms

db.create_all()
print("Base de datos creada")

##################################################################

@app.route('/')
def index():
    context = {
        'title': 'Flask Api',
        'message': 'Bienvenido a la API con Flask'
    }
    
    return jsonify(context)

app.run(debug=True)