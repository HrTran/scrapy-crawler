import scrapy
from tutorial.items import BaomoiIntro,BaomoiItem
from datetime import datetime
import time


class BaomoiSpider(scrapy.Spider):
    name = 'baomoi'
    allowed_domains = ['baomoi.com']
    global page_num
    page_num = 0

    def start_requests(self):
        global page_num
        NUM = 14

        file = open("url_" + str(NUM) + ".txt", "r")
        lines = file.read().split("\n")
        for line in lines:
            item = BaomoiIntro()
            fields = line.split(" ")
            # print(fields)
            item['fid'] = fields[0]
            url = fields[1]

            request = scrapy.Request(url=url, callback=self.parse_page,
                                     dont_filter=True)
            request.meta['item'] = item
            yield request

    def parse(self, response):
        xpath_story = ''
        for href in response.xpath(xpath_story):
            url = response.urljoin(href.extract())
            request = scrapy.Request(url=url, callback=self.parse_page,
                                     dont_filter=True)
            print("url : " + url)
            yield request

    def parse_page(self, response):
        item = response.meta['item']
        xpath_item = ''
        item['desc'] = response.xpath(xpath_item).extract_first().strip()
        yield item
