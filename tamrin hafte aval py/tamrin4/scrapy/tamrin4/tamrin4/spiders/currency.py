import scrapy


class CountrySpider(scrapy.Spider):
    name = "currency"
    allowed_domains = ["https://www.currencyremitapp.com"]
    start_urls = [
        "https://www.currencyremitapp.com/world-currency-symbols",
    ]

    def parse(self, response):
        rows = response.css('.table-bordered tbody tr')
        for row in rows:
            flag_image = row.css('td img::attr(src)').get()
            country = row.css('td:nth-child(2)::text').get()
            currency = row.css('td:nth-child(3)::text').get()
            code = row.css('td:nth-child(4)::text').get()
            symbol = row.css('td:nth-child(5)::text').get()

            yield {
                'flag_image': flag_image,
                'country': country,
                'currency': currency,
                'code': code,
                'symbol': symbol
            }
