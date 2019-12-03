# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64
from scrapy import log
from scrapy.exceptions import IgnoreRequest
# from tutorial.utils import connect_url_database

# Start your middleware class
class ProxyMiddleware(object):
   # overwrite process request

   def process_request(self, request, spider):
       # Set the location of the proxy
       request.meta['proxy'] = "http://113.161.65.201:8080"
       # Use the following lines if your proxy requires authentication
       #proxy_user_pass = "USERNAME:PASSWORD"
       # setup basic authentication for the proxy
       #encoded_user_pass = base64.encodestring(proxy_user_pass)
       #request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

# class DedupMiddleware(object):

#     def __init__(self):
#         self.db = connect_url_database()

#     def process_request(self, request, spider):
#         url = request.url
#         if self.db.has(url):
#             log.msg('ignore duplicated url: <%s>'%url, level=log.DEBUG)
#             raise IgnoreRequest()