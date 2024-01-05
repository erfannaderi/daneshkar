# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CurrencyItem(scrapy.Item):
    flag_image = scrapy.Field()
    country = scrapy.Field()
    currency = scrapy.Field()
    code = scrapy.Field()
    symbol = scrapy.Field()
