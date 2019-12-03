# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class TutorialItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class BaomoiItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    source = scrapy.Field()
    createdAt = scrapy.Field()
    updatedAt = scrapy.Field()
    content = scrapy.Field()
        
class BaomoiIntro(scrapy.Item):
    fid = scrapy.Field()
    desc = scrapy.Field()