import joblib
import numpy as np
import os

class HousingPricePredictor:
    def __init__(self, model_dir=None):
        if model_dir is None:
            model_dir = os.path.join(os.path.dirname(__file__), 'model')
        
        self.model = joblib.load(os.path.join(model_dir, 'housing-ml.pkl'))
        self.sc_x = joblib.load(os.path.join(model_dir, 'scaler_x.pkl'))
        self.sc_y = joblib.load(os.path.join(model_dir, 'scaler_y.pkl'))

    def predict_price(self, rooms: int) -> float:
        rooms_array = np.array([[rooms]])
        rooms_scaled = self.sc_x.transform(rooms_array)
        prediction_scaled = self.model.predict(rooms_scaled)
        prediction = self.sc_y.inverse_transform(prediction_scaled) * 1000
        return float(prediction[0][0])
