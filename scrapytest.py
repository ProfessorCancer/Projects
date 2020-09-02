import scrapy
from scrapy.crawler import CrawlerProcess
link_list = []

class parse(scrapy.Spider):

    name = 'task6'
    start_urls = ['http://192.168.1.1/sets/1']
    #test purpose link http://172.18.58.238/index.html
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
    start_urls = ['http://192.168.1.1/index.html']
    #test purpose link http://172.18.58.238/index/php
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

process = CrawlerProcess()
process.crawl(parse)
process.crawl(images)
process.start()