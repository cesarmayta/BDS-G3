import requests

URL =  'https://randomuser.me/api?results=10&nat=es&noinfo'

response = requests.get(URL)

# print(f" respuesta del servidor : {response.status_code}")
# print(f" cabeceras : {response.headers}")
# print(f" contendido : {response.json()}")

if response.status_code == 200:
    data = response.json()
    #usuario = data['results'][0]
    for usuario in data['results']:
        print(f"Nombre : {usuario['name']['first']} {usuario['name']['last']}")
        print(f"Pais : {usuario['location']['country']}")
        print(f"Correo : {usuario['email']}")
        print(f"Telefono : {usuario['phone']}")
        print(f"Foto : {usuario['picture']['large']}")
        print("="*50)
else:
    print(f"algo salio mal {response.status_code}")
