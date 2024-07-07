import scrapy


class NaverShoppingSpider(scrapy.Spider):
    name = "naver_shopping"
    allowed_domains = ["shopping.naver.com"]
    start_urls = ["https://shopping.naver.com"]

    def parse(self, response):
        pass
