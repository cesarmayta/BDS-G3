
def menu(ANCHO):
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

def registrar(ANCHO):
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
    return dic_nuevo_alumno

def mostrar(ANCHO,dic_alumnos):
    print("=" * ANCHO)
    print(" " * 10 + "[2] MOSTRAR ALUMNOS")
    print("=" * ANCHO)
    for dni,datos in dic_alumnos.items():
        print(f"DNI : {dni}")
        print(f"Nombre : {datos['nombre']}")
        print(f"EMAIL : {datos['email']}")
        print("*"*ANCHO)

def actualizar(ANCHO,dic_alumnos):
    print("=" * ANCHO)
    print(" " * 10 + "[3] ACTUALIZAR ALUMNO")
    print("=" * ANCHO)
    dni = input("INGRESE DNI DEL ALUMNO A ACTUALIZAR")
    if dni in dic_alumnos:
        print(f"ALUMNO A ACTUALIZAR {dic_alumnos[dni]['nombre']}")
        nuevo_nombre = input('NOMBRE : ')
        nuevo_dni = input('DNI  :')
        nuevo_email = input('EMAIL')
        dic_act_alumno = {
            dni : {
                'nombre':nuevo_nombre,
                'email':nuevo_email
            }
        }
        dic_alumnos.update(dic_act_alumno)
        print("ALUMNO ACTUALIZADO CON EXITO")

def eliminar(ANCHO,dic_alumnos):
    print("=" * ANCHO)
    print(" " * 10 + "[4] ELIMINAR ALUMNO")
    print("=" * ANCHO)
    dni = input("INGRES EL DNI DEL ALUMNO A ELIMINAR : ")
    if dni in dic_alumnos:
        dic_alumnos.pop(dni)
        print("ALUMNO ELIMINADO")
    else:
        print("NO SE ENCONTRO EL ALUMNO")

def salir(ANCHO):
    print("=" * ANCHO)
    print(" " * 10 + "[5] SALIR")
    print("=" * ANCHO)

def mostrar_mensaje_invalida(ANCHO):
    print("=" * ANCHO)
    print(" " * 10 + "OPCIÓN INVÁLIDA!!!")
    print("=" * ANCHO)