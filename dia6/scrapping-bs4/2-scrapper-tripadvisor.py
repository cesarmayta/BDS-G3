import requests
from bs4 import BeautifulSoup

url = 'https://www.tripadvisor.com.pe/Restaurants-g294316-Lima_Lima_Region.html'

# Encabezados para simular un navegador
fake_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url,headers=fake_headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    restaurantes = []
    div_restaurantes = soup.find_all('a', class_='BMQDV _F Gv wSSLS SwZTJ FGwzt ukgoS')
    
    for restaurante in div_restaurantes:
        nombre = restaurante.get_text()
        url = "https://www.tripadvisor.com.pe/"  + restaurante['href']
        
        print(f'Nombre: {nombre}')
        print(f'URL: {url}')
        print('---')
        restaurantes.append({"nombre": nombre, "url": url})
else:
    print(f'Error {response.status_code} {response.reason}')