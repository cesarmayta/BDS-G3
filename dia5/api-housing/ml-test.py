from model import HousingModel

if __name__ == '__main__':
    # Cargamos el modelo y hacemos una predicción
    # rooms = 5
    # model = HousingModel()
    # predict = model.predict(rooms)
    # print(f'El precio de una vivienda con {rooms} habitaciones es: {predict}')
    
    # Ejemplo de uso
    rooms = int(input("Ingrese el número de habitaciones: "))
    model = HousingModel()
    predict = model.predict(rooms)
    print(f'El precio de una vivienda con {rooms} habitaciones es: {predict}')