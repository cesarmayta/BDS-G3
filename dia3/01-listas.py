dias = ['lunes','martes','miercoles']
print(dias)
print(dias[-2])
print(dias[1:3])

#agregar valores a la lista
dias.append('jueves')
dias.append('viernes')
print(dias)

#eliminar un valor de la lista
dias.pop(3)
print(dias)
del dias[2:4]
print(dias)
dias.append('miercoles')
dias.append('jueves')
#actualizar un valor
dias[2] = 'miercoles'
print(dias)
dias.append('viernes')
#recorrer una lista
for contador in range(len(dias)):
    print(dias[contador])
print("=================")
for dia in dias:
    print(dia)