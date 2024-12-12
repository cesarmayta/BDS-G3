import os
from time import sleep
from matriculas.lib_alumnos import *

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
    menu(ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if opcion == 1:
        dic_nuevo_alumno = registrar(ANCHO) 
        dic_alumnos.update(dic_nuevo_alumno)
    elif opcion == 2:
        mostrar(ANCHO,dic_alumnos)
        input("Presion ENTER para continuar...")
    elif opcion == 3:
        actualizar(ANCHO,dic_alumnos)
    elif opcion == 4:
        eliminar(ANCHO,dic_alumnos)
    elif opcion == 5:
        salir(ANCHO)
    else:
        mostrar_mensaje_invalida()
    sleep(1)