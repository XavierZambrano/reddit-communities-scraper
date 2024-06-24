import scrapy


class CommunitiesSpider(scrapy.Spider):
    name = "communities"
    allowed_domains = ["reddit.com"]
    start_urls = ["https://reddit.com"]

    def parse(self, response):
        pass
