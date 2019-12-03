# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import pymongo
import re
from scrapy.exceptions import DropItem
# from tutorial.utils import connect_url_database

# Duplicate filter
class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['fid'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['fid'])
            return item

# Avoid scrapy revisit on a different run
class DedupPipeline(object):

    def __init__(self):
        self.db = connect_url_database()

    def process_item(self, item, spider):
        url = item['link']
        self.db.insert(url)
        yield item

# cleans whitespace & HTML
class CleanerPipeline(object):
   def process_item(self, item, spider):
       # general tidying up
       for (name, val) in item.items():
           # utils.devlog("Working on %s [%s]" % (name, val))
           print("Working on %s [%s]" % (name, val))
           if val is None:
               item[name] = ""
               continue
           item[name] = re.sub('\s+', ' ', val).strip() # remove whitespace           
           #item['blurb'] = re.sub('<[^<]+?>', '', item['blurb']).strip() # remove HTML tags

       # spider specific
       if spider.name == "techmeme":
           item['blurb'] = item['blurb'].replace('&nbsp; &mdash;&nbsp;', '').strip()

       return item


class MongoPipeline(object):

    collection_name = 'baomoi'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        logging.debug("Post added to MongoDB")
        return item
