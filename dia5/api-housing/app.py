from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from model import HousingModel


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
    
    #calculamos el precio de la vivienda
    hmodel = HousingModel()
    price = hmodel.predict(rooms)
    new_housing.price = price
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

@app.route('/housing/<int:id>', methods=['GET'])
def get_data_id(id):
    data = Housing.query.get(id) # select * from housing where id = id
    data_schema = HousingSchema()
    
    context = {
        'status': True,
        'message': 'Registro obtenido',
        'content': data_schema.dump(data)
    }
    
    return jsonify(context), 200

@app.route('/housing/<int:id>', methods=['PUT'])
def update_data(id):
    data = Housing.query.get(id) # select * from housing where id = id
    rooms = request.json['rooms']
    
    hmodel = HousingModel()
    price = hmodel.predict(rooms)
    
    data.rooms = rooms
    data.price = price
    db.session.commit()
    
    data_schema = HousingSchema()
    context = {
        'status': True,
        'message': 'Registro actualizado',
        'content': data_schema.dump(data)
    }
    
    return jsonify(context), 200

@app.route('/housing/<int:id>', methods=['DELETE'])
def delete_data(id):
    data = Housing.query.get(id) # select * from housing where id = id
    db.session.delete(data)
    db.session.commit()
    
    data_schema = HousingSchema()
    context = {
        'status': True,
        'message': 'Registro eliminado',
        'content': data_schema.dump(data)
    }
    return jsonify(context), 200

app.run(debug=True)