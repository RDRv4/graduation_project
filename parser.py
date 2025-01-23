import logging
import collections
import csv

import requests
import bs4


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('almi')


ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'good_info',
        'price',
        'image',
        'url',
    ),
)

HEADERS = (
    'Good information',
    'Price',
    'Image',
    'Url',
)

class Spider:
    def __init__(self):
        self.session = requests.Session()
        self.session.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
            "Accept-Language": "ru",
        }
        self.result = []
    

    def load_page(self, page: int = None):
        url = "https://almi-dostavka.by/catalog/molochnye-produkty-syr-yaytsa/moloko-267/moloko-268/"
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text
    

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('div.catalog_item.main_item_wrapper.item_wrap')
        for block in container:
            self.parse_block(block=block)
    

    def parse_block(self, block):
        url_block = block.select_one('a.thumb')
        url = url_block.get('data-param-item_href')

        good_block = block.select_one('a.dark_link')
        good = good_block.select_one('span')

        good = good.text
        good = good.replace('/', '').strip()

        price_block = block.select_one('div.price')
        price = price_block.select_one('span.price_value')

        price = price.text.strip()

        photo_block = block.select_one('a.thumb')
        photo_url = photo_block.select_one('img')
        photo = photo_url.get('src')

        self.result.append(ParseResult(
            good_info=good,
            price=price,
            image=photo,
            url=url,
        ))


    def save_result(self):
        path = '/code/api/info.csv'
        with open(path, 'w') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(HEADERS)
            for item in self.result:
                writer.writerow(item)


    def run(self):
        text = self.load_page()
        self.parse_page(text=text)
        logger.info(f'Got {len(self.result)} elements')

        self.save_result()


if __name__ == "__main__":
    parser = Spider()
    parser.run()
