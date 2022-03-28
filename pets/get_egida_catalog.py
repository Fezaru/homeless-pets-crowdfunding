import logging

import requests
from bs4 import BeautifulSoup

logging.basicConfig(filename='get_egida_catalog.log', level=logging.INFO)
logger = logging.getLogger(__name__)

CHARACTERISTIC_FIELD_NAME_TO_DB_FIELD_NAME = {
    'Пол': 'sex',
    'Возраст': 'age',
    'Вет.особенности': 'vet_peculiarities',
    'Обработка от блох/клещей': 'flea_treatment',
    'Тип шерсти': 'fur_type',
    'Характер': 'character',
    'Кормление': 'feeding',
    'Приучена к лотку': 'litter_box_trained',
    'Приучен к лотку': 'litter_box_trained',
    'В каталоге': 'in_catalog_since',
    'Приют': 'shelter',
    'Телефон куратора': 'curator_info',
    # for dogs
    'Высота в холке': 'height',
    'Порода': 'breed',
}

PET_TYPES = ['dog', 'cat', 'puppy', 'kitten']

CATALOG_URL_TO_PET_TYPE = {
    '/catalog/cat': 'cat',
    '/catalog/kitten': 'kitten',
    '/catalog/dog': 'dog',
    '/catalog/puppy': 'puppy',
}


class EgidaClient:
    def __init__(self):
        self.base_url = 'https://egida.by/'
        self.catalog_url = self.base_url + 'catalog/'
        self.session = requests.Session()

    def get_html(self, url: str):
        response = self.session.get(url)
        if response.status_code >= 400:
            return response.text, False

        return response.text, True

    def get_pets_details_urls_for_page(self, url: str):
        html, success = self.get_html(url)
        if not success:
            logger.error(f'[{url}] could not be get')
            return None
        soup = BeautifulSoup(html, 'html.parser')

        all_entries_divs = soup.find_all('div', id='allEntries')
        assert len(all_entries_divs) == 1
        pets_per_page = all_entries_divs[0].find_all('div', {'class': 'entry__body'})
        return [tag.find('a')['href'] for tag in pets_per_page]

    def get_pet_details(self, url: str):
        html, success = self.get_html(url)
        if not success:
            logger.error(f'[{url}] could not be get')

        soup = BeautifulSoup(html, 'html.parser')
        images_urls = self.get_images_urls(soup)
        info = self.get_pet_info(soup)
        info.update({'original_url': url, 'external_id': url.split('/')[-1]})
        return info, images_urls

    def get_images_urls(self, soup: BeautifulSoup):
        images_lis = soup.find('div', {'class': 'single-entry__image'}).find_all('li')
        images_links = [li.find('a')['href'] for li in images_lis]
        return [self.base_url + tag[1:] for tag in images_links]

    def get_pet_info(self, soup: BeautifulSoup):
        characteristics_div = soup.find('div', {'class': 'single-entry__characteristics'})
        pet_type = CATALOG_URL_TO_PET_TYPE.get(soup.find('a', {'class': 'ecategory'})['href'], None)
        result = {'pet_type': pet_type}
        result.update({'name': soup.find('h3', {'class': 'single-entry__title'}).text})
        result.update({'description': soup.find('div', {'class': 'single-entry__body__description'}).text})
        characteristics_lines = characteristics_div.find_all('dl')
        for characteristic in characteristics_lines:
            k, v = characteristic.text.replace('\n', '').split(':')
            characteristic_name = CHARACTERISTIC_FIELD_NAME_TO_DB_FIELD_NAME.get(k, None)
            if characteristic_name is not None:
                if characteristic_name == 'curator_info':
                    v = v.replace('При обращении к куратору просьба ссылаться на каталог животных EGIDA.BY', '').strip()
                result.update({characteristic_name: v})
            else:
                logger.error(f'key [{k}] could not be converted')

        return result


def get_pets_data(historical: bool = False):
    client = EgidaClient()
    result = []
    if not historical:
        urls = [client.catalog_url + pet_type + '/' for pet_type in PET_TYPES]
    else:
        urls = [client.catalog_url]
    for catalog_url in urls:
        html, success = client.get_html(catalog_url)
        if success:
            soup = BeautifulSoup(html, 'html.parser')

            # take 3rd element because it contains last page
            # total_pages = int(soup.find_all('a', {'class': 'swchItem'})[3].find('span', recursive=False).text)
            page_numbers = []
            for tag in soup.find_all('a', {'class': 'swchItem'}):
                try:
                    page_numbers.append(int(tag.text))
                except ValueError:
                    pass
            total_pages = max(page_numbers) if page_numbers else 1

            for i in range(1, total_pages + 1):
                url = catalog_url + f'?page{i}'
                pets_details_urls = client.get_pets_details_urls_for_page(url)
                if pets_details_urls is None:
                    continue

                for details_url in pets_details_urls:
                    url = client.catalog_url + details_url.split('/')[-1]
                    data, images_urls = client.get_pet_details(url)
                    result.append((data, images_urls))

    return result


if __name__ == '__main__':
    get_pets_data()
