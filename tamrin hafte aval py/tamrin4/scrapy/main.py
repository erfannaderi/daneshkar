import scrapy


class CountrySpider(scrapy.Spider):
    name = "countries"
    start_urls = [
        'https://www.currencyremitapp.com/world-currency-symbols',
    ]

    def parse(self, response, **kwargs):
        countries = response.css('div.country')
        for country in countries:
            name = country.css('div.name::text').get()
            flag_link = country.css('div.flag img::attr(src)').get()
            # Add more fields as needed
            print(f"Name: {name}, Flag Link: {flag_link}")


if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess()
    process.crawl(CountrySpider)
    process.start()
