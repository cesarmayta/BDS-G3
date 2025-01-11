import requests
from bs4 import BeautifulSoup
from prefect import task

URL = 'https://neoauto.com/venta-de-autos-usados--camionetas-suv'

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

@task(name='Extraer data de Neoauto')
def task_extra_total_pages():
    response = requests.get(URL, headers=HEADERS)
    total_pages = 1
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
       
        link_final_page = soup.find('a',class_='c-pagination-content__last-page')['href']
        pages = link_final_page.split("page=")[-1]
        total_pages = int(pages)
    else:
        print(f'Error {response.status_code} {response.reason}')
        
    return total_pages