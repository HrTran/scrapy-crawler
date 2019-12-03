import scrapy
from tutorial.items import BaomoiItem
from datetime import datetime
import time


class CustomSpider(scrapy.Spider):
    """ Make requests using urls from RabbitMQ queue named same as spider"""
    name = 'custom'
    allowed_domains = ['baomoi.com']
    start_urls = [
        'https://baomoi.com/the-gioi.epi',
    ]

    # modify a request before firing. request already contains url
    # received from RabbitMQ
    def _modify_request(self, request):
        request.meta['time'] = time()
        return request

    # callback to the response received
    def _callback(self, response):
        return self.parse(response)

    def parse(self, response):
        for sel in response.css('.story'):
            item = BaomoiItem()
            item['title'] = sel.xpath().extract_first().strip()
            item['link'] = ''
            item['desc'] = ''
            item['source'] = ''
            item['createdAt'] = ''
            item['updatedAt'] = ''
            item['content'] = ''
            yield item
