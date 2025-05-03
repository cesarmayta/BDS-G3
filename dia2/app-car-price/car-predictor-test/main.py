from car_predictor import CarPricePredictor

predictor = CarPricePredictor()
cylinders = float(input("Enter the number of cylinders: "))
year = int(input("Enter the year of the car: "))

price = predictor.predict(cylinders, year)
print(f"The predicted price of the car is: ${price:.2f}")   