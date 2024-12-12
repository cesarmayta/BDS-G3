
dic_empresas = {}
def cargar_empresas(nombre_archivo):
    archivo = open(nombre_archivo,'r')
    str_empresas = archivo.read()
    print(str_empresas)
    archivo.close()

    lista_empresas = str_empresas.splitlines()
    print(lista_empresas)
    for str_fila in lista_empresas:
        lista_fila = str_fila.split(',')
        print(lista_fila)
        dic_registro = {
           'razon_social':lista_fila[1],
           'direccion' :lista_fila[2]
        }
        dic_nueva_empresa = {
            lista_fila[0] : dic_registro
        }
        dic_empresas.update(dic_nueva_empresa)


cargar_empresas('empresas.txt')
print(dic_empresas)

dic_empresas = {
    '1010' : {
        'razon_social':'pepito sac',
        'direccion':'calle peru'
    },
    '2020' : {
        'razon_social':'pepito sac',
        'direccion':'calle peru'
    }
}