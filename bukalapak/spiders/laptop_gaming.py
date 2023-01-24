import scrapy
from ..utils import URL,parse_new_url
from ..items import BukalapakItem
from scrapy.loader import ItemLoader
import json


class LaptopGamingSpider(scrapy.Spider):
    name = 'laptop_gaming'
    allowed_domains = ['api.bukalapak.com']
    start_urls = [URL]

    handle_httpstatus_list = [401]

    current_page = {
        'page':1,
        'limit':0
    }

    def start_requests(self):
        yield scrapy.Request(
            url=URL,
            headers={
                'accept': 'application/json',
                'x-device-ad-id': 'a853b1ef98eb9b6da81135596b2a407b'
            },
            callback=self.parse
        )

    def parse(self, response):
        json_resp = json.loads(response.body)
        meta = json_resp.get('meta')
        data_laptops = json_resp.get('data')

        for laptop in data_laptops:
            loader = ItemLoader(item=BukalapakItem())

            laptop_city = laptop.get('store').get('address').get('city')
            laptop_province = laptop.get('store').get(
                'address').get('province')
            laptop_adress = [laptop_city, laptop_province]

            loader.add_value('product_id', laptop.get('id'))
            loader.add_value('product_title', laptop.get('name'))
            loader.add_value('product_description', laptop.get('description'))
            loader.add_value('seller_address', ','.join(laptop_adress))
            loader.add_value('images_urls', laptop.get(
                'images').get('large_urls'))
            loader.add_value('product_price', laptop.get('original_price'))
            loader.add_value('product_discount_price', laptop.get('price'))
            loader.add_value('product_stock', laptop.get('stock'))
            loader.add_value('product_url', laptop.get('url'))

            yield loader.load_item()

        total_page = meta.get('total_pages')
        print(total_page)

        if self.current_page['page'] <= total_page:
            self.current_page['page'] += 1
            self.current_page['limit'] += 30

            print(self.current_page['page'])
            yield scrapy.Request(
                parse_new_url(url=URL, next_page_number=self.current_page['page'],offset_page_increment=self.current_page['limit']),
                headers={
                    'accept': 'application/json',
                    'x-device-ad-id': 'a853b1ef98eb9b6da81135596b2a407b'
                },
                callback=self.parse
            )

        # with open('initial_response.json','wb') as file:
        #     file.write(response.body)
