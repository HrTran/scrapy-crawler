# -*- coding: utf-8 -*-
"""
"""
import scrapy
from tutorial.items import DmozItem
        

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = [
        'http://www.dmoz-odp.org/Computers/Programming/Languages/Python/',
    ]

    def parse(self, response):
        for href in response.xpath('//div[@class="cat-item"]/a/@href'):
            url = response.urljoin(href.extract())
            request = scrapy.Request(url=url, callback=self.parse_page2, dont_filter=True)
            print("url : " + url)
            yield request

        # for sel in response.css('.site-item'):
        #     item = DmozItem()
        #     item['title'] = sel.xpath('div[@class="title-and-desc"]/a/div[@class="site-title"]/text()') \
        #         .extract_first().strip()
        #     item['link'] = sel.xpath('div[@class="title-and-desc"]/a/@href').extract_first().strip()
        #     item['desc'] =  sel.css('.site-descr ::text').extract_first().strip()
        #     yield item

    def parse_page2(self, response):
        for sel in response.css('.site-item '):            
            item = DmozItem()
            item['title'] = sel.xpath('//*[@class="title-and-desc"]/a/div[@class="site-title"]/text()') \
                .extract_first().strip()
            item['link'] = sel.xpath('//*[@class="title-and-desc"]/a/@href').extract_first().strip()
            item['desc'] =  sel.css('.site-descr ::text').extract_first().strip()
            yield item

   

    # def parse(self, response):
    #     for href in response.xpath('//div[@class="cat-item"]/a/@href'):
    #         url = response.urljoin(href.extract())
    #         yield scrapy.Request(url)

    #     for sel in response.css('.site-item'):
    #         item = DmozItem()
    #         item['title'] = sel.xpath('div[@class="title-and-desc"]/a/div[@class="site-title"]/text()') \
    #             .extract_first().strip()
    #         item['link'] = sel.xpath('div[@class="title-and-desc"]/a/@href').extract_first().strip()
    #         item['desc'] =  sel.css('.site-descr ::text').extract_first().strip()
    #         yield item