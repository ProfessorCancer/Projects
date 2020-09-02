import scrapy
from scrapy.crawler import CrawlerProcess
import re
import requests
from requests import *
######## TASK 5
#modded useragent
links = []
fakeuseragent = { 'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 AppleWebKit/537.36 (KHTML, like Gecko)"}
moduseragent = { 'user-Agent':"Mobile"}

#set target webpage
#test url
url = 'https://www.facebook.com/'
#url = 'http://172.18.58.238/headers.php'
link_list = []

##
def Task5():

    #GET
    r = requests.Session()
    request = r.get(url, headers=fakeuseragent)
    statusCode = request.status_code
    #header
    header = request.headers

    #to change header type to mobile
    header.update(moduseragent)
    new_request = r.get(url, headers=header)


    Task5File = open("task5.txt", "w")
    Task5File.write(f"{request.status_code}\n{header}\n$$$ Modded: \n{moduseragent}\n{new_request.headers}")

    if statusCode == 200:
        print("OK")
    else:
        print("Error status code: %s"%statusCode)
    print(header)
    print(new_request)

class parse(scrapy.Spider):

    name = 'task6'
    #test url
    start_urls = ['https://www.facebook.com/']
    #start_urls = ['http://172.18.58.238/index.php']
    def parse(self, response):
        Task6 = open("task6.json", 'w')
        for link in response.css('a'):
            link_results = link.css('a::attr(href)').get()
            link_list.append(link_results)
            Task6.write(str({'results': link_results})+"\n")
        Task6.close()
    print(link_list)

#image urls extractions
class images(scrapy.Spider):
    name = 'task7'
    start_urls = ['https://www.facebook.com/']
    #start_urls = ['http://172.18.58.238/index/php']
    def parse(self, response):
        xpath_selector='//img'
        for x in response.xpath(xpath_selector):
            newsel='@src'
            yield{
                'Image Link':x.xpath(newsel).extract_first(),
            }
        #to recurse next page
        Page_selector='.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
            response.urljoin(next_page),
            callback=self.parse
        )

Task5()
process = CrawlerProcess()
process.crawl(parse)
process.crawl(images)
process.start()

# this part isnt working yet. HAS TO DISPLAY LIST OF IMAGE LINKS
print("\n\nLinks: ")
print(links)