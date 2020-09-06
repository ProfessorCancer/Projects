import scrapy
from scrapy.crawler import CrawlerProcess
import re
import requests

######## TASK 5
# modded useragent
fakeuseragent = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 AppleWebKit/537.36 (KHTML, like Gecko)"}
moduseragent = {'user-Agent': "Mobile"}

# set target webpage
# test url
url = 'https://www.facebook.com/'


# url = 'http://172.18.58.238/headers.php'

##
def Task5():
    # GET
    r = requests.Session()
    request = r.get(url, headers=fakeuseragent)
    statusCode = request.status_code
    # header
    header = request.headers

    # to change header type to mobile
    header.update(moduseragent)
    new_request = r.get(url, headers=header)

    Task5File = open("task5.txt", "w")
    Task5File.write(f"{request.status_code}\n{header}\n$$$ Modded: \n{moduseragent}\n{new_request.headers}")

    if statusCode == 200:
        print("OK")
    else:
        print("Error status code: %s" % statusCode)
    print("\n$$$ Modded: \n", moduseragent)
    print(new_request.headers)


class parseTask6(scrapy.Spider):
    name = 'task6'
    # test url
    start_urls = ['https://www.facebook.com/']
    # start_urls = ['http://172.18.58.238/index.php']
    open("task6.json", 'w').close()

    def parse(self, response):
        Task6 = open("task6.json", 'a')
        for link in response.css('a'):
            link_results = link.css('a::attr(href)').get()
            Task6.write(str({'results': link_results}) + "\n")
        Task6.close()


# image urls extractions
class parseImages(scrapy.Spider):
    img_list = []
    name = 'task7'
    # allowed_domains = ['172.18.58.238']


 # allowed_domains = ['https://www.facebook.com/']
start_urls = ['https://www.facebook.com/']
# start_urls = ['http://172.18.58.238/index/php']
open('task7.txt', 'w').close()


def parse(self, response):
    url = response.url
    task7 = open('task7.txt', 'a')
    for i in response.css('img::attr(src)').extract():
        if bool(re.findall(r'.+\.jpg', i)):
            self.img_list.append(url + i)
            task7.write(url + i + 'n')
    for n in response.css('a::attr(href)').extract():
        if n is not None:
            yield response.follow(n, self.parse)
    task7.close()


Task5()
process = CrawlerProcess()
process.crawl(parseTask6)
process.crawl(parseImages)
process.start()