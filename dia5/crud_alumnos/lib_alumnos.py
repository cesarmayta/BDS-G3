from tabulate import tabulate
from colorama import Fore, Back, Style

ANCHO = 20
TABLE_STYLE = 'simple_grid'


dic_alumnos = {}

def cargar_alumnos(file_name):
    file = open(file_name,'r')
    str_alumnos = file.read()
    file.close()
    lista_alumnos = str_alumnos.splitlines()
    for str_fila in lista_alumnos:
        lista_fila = str_fila.split(',')
        dic_fila = {
            'nombre':lista_fila[1],
            'email':lista_fila[2]
        }
        dic_nuevo_alumno = {
            lista_fila[0]: dic_fila
        }
        dic_alumnos.update(dic_nuevo_alumno)

def grabar_alumnos(file_name):
    str_alumnos = ""
    for alumno_clave,alumno_valor in dic_alumnos.items():
        str_alumnos += alumno_clave + ","
        for registro_clave,registro_valor in alumno_valor.items():
            str_alumnos += registro_valor
            if registro_clave != 'email':
                str_alumnos += ','
            else:
                str_alumnos += '\n'
    
    fsalida = open(file_name,'w')
    fsalida.write(str_alumnos)
    fsalida.close()
    



def mostrar_mensaje(texto):
    tabla = [[f'{Fore.GREEN}{texto}{Style.RESET_ALL}']]
    print(tabulate(tabla,tablefmt=TABLE_STYLE,stralign="center"))

def menu():
    menu_principal = [[f"{Fore.GREEN}[1] REGISTRAR ALUMNO{Style.RESET_ALL}"],
                      [f"{Fore.GREEN}[2] MOSTRAR ALUMNOS{Style.RESET_ALL}"],
                      [f"{Fore.GREEN}[3] ACTUALIZAR ALUMNO{Style.RESET_ALL}"],
                      [f"{Fore.GREEN}[4] ELIMINAR ALUMNO{Style.RESET_ALL}"],
                      [f"{Fore.GREEN}[5] SALIR{Style.RESET_ALL}"]]
    print(tabulate(menu_principal,headers=[f"{Fore.BLUE}GESTIÓN DE ALUMNOS{Style.RESET_ALL}"],tablefmt=TABLE_STYLE))
    
    

def registrar():
    mostrar_mensaje("[1] REGISTRAR ALUMNO")
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

def mostrar():
    mostrar_mensaje("[2] MOSTRAR ALUMNOS")
    data = []
    for dni,datos in dic_alumnos.items():
        alumno_fila = [dni,datos['nombre'],datos['email']]
        data.append(alumno_fila)
    print(tabulate(data,headers=['DNI','NOMBRE','EMAIL'],tablefmt=TABLE_STYLE))
        

def actualizar():
    mostrar_mensaje("[3] ACTUALIZAR ALUMNO")
    dni = input("INGRESE DNI DEL ALUMNO A ACTUALIZAR")
    if dni in dic_alumnos:
        print(f"ALUMNO A ACTUALIZAR  {dic_alumnos[dni]['nombre']}")
        nuevo_nombre = input('NOMBRE : ')
        nuevo_email = input('EMAIL :')
        dic_act_alumno = {
            dni : {
                'nombre':nuevo_nombre,
                'email':nuevo_email
            }
        }
        dic_alumnos.update(dic_act_alumno)
        print("ALUMNO ACTUALIZADO CON EXITO")

def eliminar():
    mostrar_mensaje("[4] ELIMINAR ALUMNO")
    dni = input("INGRES EL DNI DEL ALUMNO A ELIMINAR : ")
    if dni in dic_alumnos:
        dic_alumnos.pop(dni)
        print("ALUMNO ELIMINADO")
    else:
        print("NO SE ENCONTRO EL ALUMNO")