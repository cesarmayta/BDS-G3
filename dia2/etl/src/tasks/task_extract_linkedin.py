from prefect import task
import requests
from bs4 import BeautifulSoup

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?currentJobId=809309445&keywords="

@task(name="Extraer data de linkedin")
def task_extract_linkedin(skill):
    offer_list = []
    source_url = LINKEDIN_URL+skill
    print(source_url)
    url = requests.get(source_url)
    if(url.status_code == 200):
        html = BeautifulSoup(url.text,'html.parser')
        ul_offers = html.find('ul',{'class':'jobs-search__results-list'})
        li_offers = ul_offers.find_all('li')
        for offer in li_offers:
            offer_title = offer.find('h3',{'class':'base-search-card__title'})
            offer_location = offer.find('span',{'class':'job-search-card__location'})
            offer_url = offer.find('a')
            offer_company = offer.find('a',{'class':'hidden-nested-link'})
            offer_date = offer.find('time',{'class':'job-search-card__listdate'})
            title = offer_title.get_text().strip() if offer_title else ''
            location = offer_location.get_text().strip() if offer_location else ''
            company = offer_company.get_text().strip() if offer_company else ''
            date_value = offer_date['datetime'].strip() if offer_date else None
            url_value = offer_url['href'].strip() if offer_url else ''
            if url_value != '':
                code = url_value.split('?')[0].split('-')[-1]
            else:
                code = 'NN'
            offer_list.append((code,title,location,company,date_value,url_value,skill))
            
        return offer_list
    else:
        print(f"error : {url.status_code}")