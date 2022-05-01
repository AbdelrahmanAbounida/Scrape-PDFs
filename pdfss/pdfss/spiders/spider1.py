import csv

import scrapy

class Spider1(scrapy.Spider):
    name = 'bo'
    allowed_domains = ['toolspareparts.com.au']
    start_urls = ['https://www.toolspareparts.com.au']

    def parse(self,response):

        with open('tools.csv', 'r') as f:
            reader = csv.reader(f)
            c = 0
            for i in reader:
                if c ==0:
                    c = 1
                    continue
                yield scrapy.Request(i[0],callback=self.parse_tool)


    def parse_tool(self,response):
        pdfs = response.xpath('//span[@class="diagram__download"]/a/@href').getall()
        cleaning_urls = []
        for link in pdfs:
            cleaning_urls.append(link)

        yield {
            'file_urls': cleaning_urls
        }