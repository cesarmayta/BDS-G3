from utils.db import db
from diabetes_classifier import DiabetesClassifier

class Diabetes(db.Model):
    __tablename__ = 'diabetes'
    id = db.Column(db.Integer, primary_key=True)
    glucose = db.Column(db.Double, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    bmi = db.Column(db.Double, nullable=False)
    is_diabetic = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, glucose, age, bmi):
        self.glucose = glucose
        self.age = age
        self.bmi = bmi
        
    def save(self):
        ml_diabetes = DiabetesClassifier()
        self.is_diabetic = ml_diabetes.predict(self.glucose, self.age, self.bmi)
        db.session.add(self)
        db.session.commit()
        