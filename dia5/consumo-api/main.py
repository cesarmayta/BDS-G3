from lib_randomuser import RandomUserApi

if __name__ == "__main__":
    api = RandomUserApi()
    results = int(input("Cuantos usuarios quieres obtener? "))
    usuarios = api.get_users(results)
    for usuario in usuarios:
        print(f"Nombre : {usuario['name']['first']} {usuario['name']['last']}")
        print(f"Pais : {usuario['location']['country']}")
        print(f"Correo : {usuario['email']}")
        print(f"Telefono : {usuario['phone']}")
        print(f"Foto : {usuario['picture']['large']}")
        print("="*50)
        
    respuesta = input("Desea guardar los datos en la base de datos? (s/n): ")
    if respuesta.lower() == 's':
        api.insert_users_to_db(usuarios)
        print("Datos guardados en la base de datos.")
    else:
        print("Datos no guardados.")