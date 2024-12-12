
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

def actualizar(ANCHO):
    pass

def eliminar(ANCHO):
    pass