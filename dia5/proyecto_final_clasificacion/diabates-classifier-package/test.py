from diabetes_classifier import DiabetesClassifier


classifier = DiabetesClassifier()
age = 50
glucose = 150
bmi = 35.7
prediction = classifier.predict(glucose, bmi, age)
print(f"Prediction: {prediction}")