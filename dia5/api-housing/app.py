from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


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
        
### creamos un esquema para serializar los datos ###
ma = Marshmallow(app)
class HousingSchema(ma.Schema):
    id = ma.Integer()
    rooms = ma.Integer()
    price = ma.Float()

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

@app.route('/housing', methods=['POST'])
def set_data():
    rooms = request.json['rooms']
    new_housing = Housing(rooms)
    
    #insertamos el nuevo registro en la base de datos
    db.session.add(new_housing)
    db.session.commit()
    
    context = {
        'status':True,
        'message': 'Registro creado',
        'content': HousingSchema().dump(new_housing)
    }
    
    return jsonify(context),201


@app.route('/housing', methods=['GET'])
def get_data():
    data = Housing.query.all() # select * from housing
    #print(data)
    
    data_schema = HousingSchema(many=True)
    
    context = {
        'status': True,
        'message': 'Registros obtenidos',
        'content': data_schema.dump(data)
    }
    
    return jsonify(context), 200

app.run(debug=True)