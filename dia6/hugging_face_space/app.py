import joblib
import gradio as gr
import numpy as np


model_car_price = joblib.load('mejor_modelo.pkl')
scaler_x = joblib.load('scaler_X.pkl')
scaler_y = joblib.load('scaler_y.pkl')


def car_price_predict(cylinders,year):
  data = np.array([[float(cylinders),int(year)]])
  data_scaled = scaler_x.transform(data)
  prediction_scaled = model_car_price.predict(data_scaled)
  price_predicted = scaler_y.inverse_transform(prediction_scaled.reshape(-1,1))
  return round(price_predicted[0][0])

demo = gr.Interface(
    fn=car_price_predict,
    inputs=[
        gr.Textbox(label='cylinders'),
        gr.Textbox(label='year')
    ],
    outputs=gr.Textbox(label="Price")
)

demo.launch()