import os
from time import sleep
# PROGRAMA PARA CONVERTIR MONEDAS DE SOLES A DOLARES Y DOLARES A SOLES
#ENTRADA
TIPO_CAMBIO_COMPRA = 3.7
TIPO_CAMBIO_VENTA = 3.8
bandera = True
#PROCESO
while(bandera):
    print("""
           =============================================
                    CONVERTIDOR DE MONEDAS
           =============================================
                [1] CONVERTIR SOLES A DOLARES
                [2] CONVERTIR DOLARES A SOLES
                [3] SALIR
           =============================================
            """)
    opcion = int(input("ELIJA UNA OPCIÓN : "))
    os.system("clear")
    if(opcion == 1):
        print("""
              =============================================
                    CONVIRTIENDO SOLES A DOLARES
              =============================================""")
        monto_origen = float(input("INGRESE MONTO EN SOLES : "))
        monto_destino = monto_origen / TIPO_CAMBIO_VENTA
        print(f"EL MONTO EN DOLARES ES {monto_destino}")
    elif(opcion == 2):
        print("""
              =============================================
                    CONVIRTIENDO DOLARES A SOLES
              =============================================""")
        monto_origen = float(input("INGRESE MONTO EN DOLARES : "))
        monto_destino = monto_origen * TIPO_CAMBIO_COMPRA
        print(f"EL MONTO EN SOLES ES {monto_destino}")
    elif(opcion == 3):
        bandera = False
        print("SALIENDO DEL PROGRAMA...")
    else:
        print("OPCIÓN NO VALIDA!!!")
        break
    sleep(2)
    os.system("clear")
    