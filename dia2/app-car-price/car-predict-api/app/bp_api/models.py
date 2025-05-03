from utils.db import db

class Car(db.Model):
    __tablename__ = 'car'
    
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(255), nullable=False)
    cylinders = db.Column(db.Double, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=True)

    def __init__(self, brand, cylinders, year):
        self.brand = brand
        self.cylinders = cylinders
        self.year = year
        self.price = 0
        
    