bandera = "si"
while(bandera == "si"):
    print("================ CALCULADORA CON PYTHON ============")
    numero1 = int(input("Número 1 : "))
    numero2 = int(input("Número 2 : "))
    operacion = int(input("""Ingrese el tipo de operacion
                      1) SUMA
                      2) RESTA
                      3) MULTIPLICACION
                      4) DIVISION
                      INGRESE OPCION :   """))
    if(operacion == 1):
        resultado = numero1 + numero2
        print(f'la suma de {numero1} + {numero2} es {resultado}')
    elif(operacion == 2):
        resultado = numero1 - numero2
        print(f'la resta de {numero1} - {numero2} es {resultado}')
    elif(operacion == 3):
        resultado = numero1 * numero2
        print(f'la multiplicacion de {numero1} X {numero2} es {resultado}')
    elif(operacion == 4):
        resultado = numero1 / numero2
        print(f'la division de {numero1} / {numero2} es {resultado}')
    else:
        print("La operacon no existe")

    bandera = input("¿desea continuar...?(si,no) : ")
