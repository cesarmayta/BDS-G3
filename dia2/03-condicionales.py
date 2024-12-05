print("MI CALCULADORA")
# ENTRADA
numero1 = input("Número 1 : ")
numero2 = input("Número 2 : ")
operacion = input("Que operación matematica desea hacer(suma | resta | multiplicacion | division) :")
# PROCESO
if(operacion == "suma"):
    resultado = int(numero1) + int(numero2)
elif(operacion == "resta"):
    resultado = int(numero1) - int(numero2)
elif(operacion == "multiplicacion"):
    resultado = int(numero1) * int(numero2)
elif(operacion == "division"):
    resultado = int(numero1) / int(numero2)
else:
    print("LA OPERACION NO EXISTE !!!")
    exit()
# SALIDA
print(f"la {operacion} de {numero1} y {numero2} es {resultado}")