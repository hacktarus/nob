# -*- coding: utf-8 -*-
import csv
import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from plugins.items import SalespageItem


class SalespagedescSpider(scrapy.Spider):
    name = "salespagedesc"

    def start_requests(self):
        return [scrapy.http.Request(url=start_url) for start_url in get_urls_from_csv()]

def get_urls_from_csv():
    with open('plugins.csv', 'rbU') as csv_file:
        data = csv.reader(csv_file)
        scrapurls = []
        for row in data:
            scrapurls.append(row)
        return scrapurls

def parse(self, response):
    item = SalespageItem()
    item['product_title'] = response.xpath('//*[@itemprop="name"][1]/text()').extract()
    return item

