import scrapy


class VividscraperSpider(scrapy.Spider):
    name = "vividscraper"
    allowed_domains = ["www.vividseats.com"]
    start_urls = ["https://www.vividseats.com/"]

    def parse(self, response):
        pass
