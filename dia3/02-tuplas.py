# TUPLAS : IGUAL A LAS LISTAS PERO INMUTABLES
dias = ('lunes','martes','miercoles','jueves')
print(dias)
print(type(dias))
#PARA AGREGAR DATOS CONVERTIMOS LA TUPLA EN LISTA
dias = list(dias)
print(type(dias))
dias.append("viernes")
dias = tuple(dias)
print(type(dias))


#recorrer una lista
for dia in dias:
    print(dia)

