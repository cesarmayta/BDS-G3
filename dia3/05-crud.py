import os
from time import sleep

"""
CRUD
 - CREATE
 - READ
 - UPDATE
 - DELETE
"""
dic_alumnos = {
    '12345678':{
        'nombre':'CESAR',
        'email':'cesar@gmail.com'
    }
}

ANCHO = 50
opcion = 0

while(opcion < 5):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "GESTIÓN DE ALUMNOS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR ALUMNO
         [2] MOSTRAR ALUMNOS
         [3] ACTUALIZAR ALUMNO
         [4] ELIMINAR ALUMNO
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")

    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "[1] REGISTRAR ALUMNO")
        print("=" * ANCHO)
        dni = input("DNI    :")
        nombre = input("NOMBRE  :")
        email = input("EMAIL    :")
        dic_nuevo_alumno = {
            dni : {
                   'nombre':nombre,
                   'email': email
                  }
        }
        dic_alumnos.update(dic_nuevo_alumno)
    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "[2] MOSTRAR ALUMNOS")
        print("=" * ANCHO)
        for dni,datos in dic_alumnos.items():
            print(f"DNI : {dni}")
            print(f"Nombre : {datos['nombre']}")
            print(f"EMAIL : {datos['email']}")
            print("*"*ANCHO)
        input("Presion ENTER para continuar...")
    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR ALUMNO")
        print("=" * ANCHO)
    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "[4] ELIMINAR ALUMNO")
        print("=" * ANCHO)
    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "[5] SALIR")
        print("=" * ANCHO)
    else:
        print("=" * ANCHO)
        print(" " * 10 + "OPCIÓN INVÁLIDA!!!")
        print("=" * ANCHO)

    sleep(1)