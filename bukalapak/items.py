# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from w3lib.html import remove_tags

from scrapy.loader.processors import TakeFirst,MapCompose

def clean_html(description):
    cleaned_description = ''

    try:
        cleaned_description =  remove_tags(description)
    except TypeError:
        cleaned_description = "No description"

    return cleaned_description


class BukalapakItem(scrapy.Item):
    # define the fields for your item here like:
    product_id = scrapy.Field(
        output_processor = TakeFirst()
    )
    product_title = scrapy.Field(
        output_processor = TakeFirst()
    )
    product_description = scrapy.Field(
        input_processor=MapCompose(clean_html),
        output_processor=TakeFirst()
    )
    seller_address = scrapy.Field(
        output_processor = TakeFirst()
    )
    images_urls = scrapy.Field(
        output_processor = TakeFirst()
    )
    images = scrapy.Field()
    product_price = scrapy.Field(
        output_processor = TakeFirst()
    )
    product_discount_price = scrapy.Field(
        output_processor = TakeFirst()
    )
    product_stock = scrapy.Field(
        output_processor = TakeFirst()
    )
    product_url = scrapy.Field(
        output_processor = TakeFirst()
    )
    