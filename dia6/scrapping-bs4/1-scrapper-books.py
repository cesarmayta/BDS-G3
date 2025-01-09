from bs4 import BeautifulSoup
import requests

url = 'http://books.toscrape.com'

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')
    books = soup.find_all('article',class_='product_pod')
    
    for book in books:
        title = book.find('h3').find('a')['title']
        price = book.find('p',class_='price_color').get_text()
        image = book.find('img')['src']
        print(title)
        print(price)
        print(image)
        print('----------------------')
else:
    print(f'Error: {response.status_code}')
    