import scrapy
from ..items import CurrencyItem


class CountrySpider(scrapy.Spider):
    name = "currency"
    allowed_domains = ["www.currencyremitapp.com"]
    start_urls = [
        "https://www.currencyremitapp.com/world-currency-symbols",
    ]

    def parse(self, response):
        rows = response.css('.table-bordered tbody tr')
        for row in rows:
            item = CurrencyItem()
            item['flag_image'] = row.css('td img::attr(src)').get()
            item['country'] = row.css('td:nth-child(2)::text').get()
            item['currency'] = row.css('td:nth-child(3)::text').get()
            item['code'] = row.css('td:nth-child(4)::text').get()
            item['symbol'] = row.css('td:nth-child(5)::text').get()

            yield item
