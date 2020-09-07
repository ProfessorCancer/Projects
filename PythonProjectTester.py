import scrapy
from scrapy.crawler import CrawlerProcess
import requests
import re
#modded useragent
links = []
fakeuseragent = { 'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 AppleWebKit/537.36 (KHTML, like Gecko)"}
moduseragent = { 'user-Agent':"Mobile"}

#set target webpage
#test url
#url = 'https://www.facebook.com/'
url = 'http://172.18.58.238/headers.php'
link_list = []
##
def start():
    def Req():
        #GET
        r = requests.Session()
        request = r.get(url, headers=fakeuseragent)
        statusCode = request.status_code
        #header
        header = request.headers

        #to change header type to mobile
        header.update(moduseragent)
        new_request = r.get(url, headers=header)
        ReqFile = open("Req.txt", "w")
        ReqFile.write(f"{request.status_code}\n{header}\n$$$ Modded: \n{moduseragent}\n{new_request.headers}")
        if statusCode == 200:
            print("OK")
        else:
            print("Error status code: %s"%statusCode)
        print(header)
        print(new_request)

    class parseURL(scrapy.Spider):

        name = 'Result'
        #test url
        #start_urls = ['https://www.facebook.com/']
        start_urls = ['http://172.18.58.238/index.php']
        def parse(self, response):
            Result = open("Result.json", 'w')
            for link in response.css('a'):
                link_results = link.css('a::attr(href)').get()
                link_list.append(link_results)
                Result.write(str({'results': url + link_results}) + "\n")
            Result.close()
        print(link_list)

    #image urls extractions
    class imgspider(scrapy.Spider):
        img_list = []
        name = "new_spider"
        start_urls = ['http://172.18.58.238/index.php']
        #start_url = 'https://www.facebook.com/'
        allowed_domains = ['172.18.58.238']
        #allowed_domains = ['https://www.facebook.com/']
        def parse(self, response):
            f = open('new_spider.txt', 'a')
            url = response.url
            for e in response.css('img::attr(src)').extract():
                if bool(re.findall(r'.+\.jpg', e)):
                    self.img_list.append(url + e)
                    f.write(url + e + '\n')
            for v in response.css('a::attr(href)').extract():
                if v is not None:
                    yield response.follow(v, self.parse)
            f.close()



    Req()
    process = CrawlerProcess()
    process.crawl(parseURL)
    process.crawl(imgspider)
    process.start()
    #test
