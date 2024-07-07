import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["shopping.naver.com"]
    start_urls = ["https://shopping.naver.com"]

    def parse(self, response):
        pass
