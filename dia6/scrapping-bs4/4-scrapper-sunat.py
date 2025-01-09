from bs4 import BeautifulSoup
import requests

url = 'https://www.sunat.gob.pe/'

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')
    sell_rate = soup.find('strong', id='sell-rate').get_text()
    print(f'Tipo de cambio venta: {sell_rate}')
else:
    print(f'Error: {response.status_code} {response.reason}')
    