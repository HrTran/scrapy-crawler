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
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = [t.strip() for t in sel.xpath('a/text()').extract()]
            item['link'] = [t.strip() for t in sel.xpath('a/@href').extract()]
            item['desc'] = [t.strip() for t in sel.xpath('text()').extract()]
            yield item
