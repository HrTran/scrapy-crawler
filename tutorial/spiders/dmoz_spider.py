# -*- coding: utf-8 -*-
"""
Created on 2015-12-29 01:34:00

@author: Cuong Tran <tranhuucuong91@gmail.com>

"""
import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = [
        'http://www.dmoz.org/Computers/Programming/Languages/Python/',
    ]

    def parse(self, response):
        for href in response.xpath('//div[@class="cat-item"]/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url)

        for sel in response.css('.site-item'):
            item = DmozItem()
            item['title'] = sel.xpath('div[@class="title-and-desc"]/a/div[@class="site-title"]/text()') \
                .extract_first().strip()
            item['link'] = sel.xpath('div[@class="title-and-desc"]/a/@href').extract_first().strip()
            item['desc'] =  sel.css('.site-descr ::text').extract_first().strip()
            yield item

