# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=3
RANDOMIZE_DOWNLOAD_DELAY = True
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN=8
CONCURRENT_REQUESTS_PER_IP=8

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'tutorial.middlewares.ProxyMiddleware': 543,
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
   # 'scrapy_rabbitmq_link.middleware.RabbitMQMiddleware': 999
   #'tutorial.middlewares.DedupMiddleware': 0
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
	'tutorial.pipelines.DuplicatesPipeline': 100,
	# 'tutorial.pipelines.CleanerPipeline': 300,
   	# 'tutorial.pipelines.MongoPipeline': 500,
   	#'tutorial.pipelines.DedupPipeline': 0
}

MONGO_URI = 'mongodb://127.0.0.1:27017'
MONGO_DATABASE = 'scrapyitems'
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED=True
# HTTPCACHE_EXPIRATION_SECS=0
# HTTPCACHE_GZIP = True
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

# # Enables scheduling storing requests queue in rabbitmq.
# SCHEDULER = "scrapy_rabbitmq_link.scheduler.Scheduler"
# # Don't cleanup rabbitmq queues, allows to pause/resume crawls.
# SCHEDULER_PERSIST = True
# # Schedule requests using a priority queue. (default)
# SCHEDULER_QUEUE_CLASS = 'scrapy_rabbitmq_link.queue.SpiderQueue'
# # Set expression for RabbitMQ URLs queue key
# SCHEDULER_QUEUE_KEY = '%(spider)s'
# # Provide host and port to RabbitMQ daemon
# RABBITMQ_CONNECTION_PARAMETERS = 'amqp://admin:admin@127.0.0.1:5672/'
# # Response status to mark message as acknowledged and remove from queue
# RABBITMQ_ACKNOWLEDGE_ON_RESPONSE_STATUS = [200, 404]

# Write as utf-8 to json
FEED_EXPORT_ENCODING = 'utf-8'