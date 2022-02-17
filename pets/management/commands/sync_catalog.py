import logging

import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand

from pets.get_egida_catalog import get_pets_data
from pets.models import Pet, Image

logging.basicConfig(filename='get_egida_catalog.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Scrapes catalog data from Egida.by and updates db'

    def add_arguments(self, parser):
        parser.add_argument('historical', nargs='?', default=False)

    def handle(self, *args, **options):
        s = requests.Session()
        pets_data = get_pets_data(historical=options['historical'])

        for data, images_urls in pets_data:
            pet, created = Pet.objects.update_or_create(external_id=data['external_id'], defaults=data)
            pet.images.all().delete()
            for image_url in images_urls:
                response = s.get(image_url)
                if response.status_code >= 400:
                    logger.error(f'Could not get [{image_url}]')

                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(response.content)
                img_temp.flush()

                Image.objects.create(image=File(img_temp), pet=pet)
