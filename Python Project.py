import requests
import scrapy
import unittest

# accessing website
url = 'URL'
r = requests.get(url)
print(r.text)
print("Status code:")
print("\t *", r.status_code)

# website info
h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

# change website name
headers = {
    'User-Agent' : 'Iphone 8'
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)

# getting images
class NewSpider(scrapy.Spider):
 name = "new_spider"
 start_urls = ['URL']
 class NewSpider(scrapy.Spider):
   name = "new_spider"
   start_urls = ['HEADER URL']
   def parse(self, response):
     css_selector = 'img'
     for x in response.css(css_selector):
       newsel = '@src'
       yield {
              'Image Link': x.xpath(newsel).extract_first(),
       }

