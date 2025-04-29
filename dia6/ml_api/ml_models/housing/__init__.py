import joblib
import numpy as np
import sklearn
import os


class HousingModel:
    
    def __init__(self):
        model_path = os.path.dirname(__file__)
        
        self.model = joblib.load(os.path.join(model_path, 'housing-ml.pkl'))
        self.scaler_x = joblib.load(os.path.join(model_path, 'scaler_x.pkl'))
        self.scaler_y = joblib.load(os.path.join(model_path, 'scaler_y.pkl'))
        
    def predict(self, rooms):
        rooms_sc = self.scaler_x.transform(np.array([[rooms]]))
        prediction = self.model.predict(rooms_sc)
        prediction_sc = self.scaler_y.inverse_transform(prediction)
        prediction_result = round(prediction_sc[0][0], 2) * 1000
        return prediction_result