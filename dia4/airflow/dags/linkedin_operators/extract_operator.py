from airflow.models import BaseOperator
from airflow.utils.context import Context
import requests
from bs4 import BeautifulSoup

class LinkedinExtractOperator(BaseOperator):

    def __init__(self, skill: str,**kwargs):
        super().__init__(**kwargs)
        self.skill = skill
        self.base_url = "https://www.linkedin.com/jobs/search/?currentJobId=809309445&keywords="

    def execute(self, context: Context):
        offer_list = []
        source_url = self.base_url + self.skill
        self.log.info(f"URL: {source_url}")
        
        response = requests.get(source_url)
        if response.status_code != 200:
            self.log.error(f"Error al acceder a {source_url}, status code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        ul_offers = soup.find('ul', {'class': 'jobs-search__results-list'})

        if not ul_offers:
            self.log.warning("No se encontraron ofertas en la página.")
            return []

        li_offers = ul_offers.find_all('li')
        for offer in li_offers:
            offer_title = offer.find('h3', {'class': 'base-search-card__title'})
            offer_location = offer.find('span', {'class': 'job-search-card__location'})
            offer_url = offer.find('a')
            offer_company = offer.find('a', {'class': 'hidden-nested-link'})
            offer_date = offer.find('time', {'class': 'job-search-card__listdate'})

            title = offer_title.get_text().strip() if offer_title else ''
            location = offer_location.get_text().strip() if offer_location else ''
            company = offer_company.get_text().strip() if offer_company else ''
            date_value = offer_date['datetime'].strip() if offer_date else None
            url_value = offer_url['href'].strip() if offer_url else ''
            code = url_value.split('?')[0].split('-')[-1] if url_value else 'NN'

            offer_list.append({
                "codigo": code,
                "titulo": title,
                "ubicacion": location,
                "empresa": company,
                "fecha": date_value,
                "url": url_value,
                "skill": self.skill
            })

        # Push al XCom
        context['ti'].xcom_push(key="linkedin_offers", value=offer_list)
        self.log.info(f"Se extrajeron {len(offer_list)} ofertas.")
        return offer_list  # opcional: también puedes retornar la lista
