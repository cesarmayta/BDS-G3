import joblib
import pandas as pd
import os

class DiabetesClassifier:
    def __init__(self):
        model_dir = os.path.join(os.path.dirname(__file__), 'ml-model')
        self.model = joblib.load(os.path.join(model_dir, 'model.pkl'))
        self.scaler = joblib.load(os.path.join(model_dir, 'scaler.pkl'))

    def predict(self,glucose, bmi, age):
        new_data = pd.DataFrame([[glucose, bmi, age]], columns=['glucose', 'bmi', 'age'])

        new_data_scaled = self.scaler.transform(new_data)

        prediction = self.model.predict(new_data_scaled)
        
        return prediction[0]