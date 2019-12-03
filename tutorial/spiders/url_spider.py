#!/usr/bin/env python
import scrapy
from tutorial.items import BaomoiItem
from datetime import datetime
import time
import pika
import tutorial.settings

connection = pika.BlockingConnection(pika.URLParameters(tutorial.settings.RABBITMQ_CONNECTION_PARAMETERS))
channel = connection.channel()

# set queue name
queue = '%(spider)s' % {'spider': 'custom'}

class UrlSpider(scrapy.Spider):
    name = 'url'
    allowed_domains = ['baomoi.com']
    start_urls = [
        'https://baomoi.com/the-gioi.epi',
    ]
    global page_num
    page_num = 0

    def start_requests(self):
        global page_num
        # use scrapy.Request to get pages and parse it data

        connection.close()

    def parse(self, response):
        xpath_story = ''
        for href in response.xpath(xpath_story):
            url = response.urljoin(href.extract())
            url = url.strip(' \n\r')
            channel.basic_publish(
                exchange='',
                routing_key=queue,
                body=url,
                properties=pika.BasicProperties(
                    content_type='text/plain',
                    delivery_mode=1)
            )
            print("url : " + url)
