from utils.db import db
from car_predictor import CarPricePredictor

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
        
    @staticmethod
    def get_all():
        return Car.query.all()

    @staticmethod
    def get_by_id(id):
        return Car.query.get(id)
    
    def save(self):
        ml_car = CarPricePredictor()
        self.price = ml_car.predict(self.cylinders, self.year)
        
        if not self.id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    