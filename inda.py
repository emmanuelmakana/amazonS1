import scrapy
from ..items import BooksItem


class tnScrapper(scrapy.Spider):
    name = 'yut_score'
    start_url = ['https://www.predictz.com/predictions/']

    def parse(self, response):
        items = BooksItem()
        data = response.css(".ptgame a::text").extract()
        items['data'] = data
        yield items
