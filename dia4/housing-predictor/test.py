from housing_predictor import HousingPricePredictor

predictor = HousingPricePredictor()
rooms = int(input("Ingrese nro de habitaciones: "))
price = predictor.predict_price(rooms)
print(f'El precio de un departamento con {rooms} habitaciones es: $ {price:.2f}')

