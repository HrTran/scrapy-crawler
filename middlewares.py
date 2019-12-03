import base64

class ProxyMiddleware(object):

   def process_request(self, request, spider):
       request.meta['proxy'] = "http://112.109.90.15:808"
       encoded_user_pass = base64.encodestring(proxy_user_pass)
       request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
