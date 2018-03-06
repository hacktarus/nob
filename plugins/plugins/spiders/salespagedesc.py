# -*- coding: utf-8 -*-
import csv
import scrapy

class SalespagedescSpider(scrapy.Spider):
    name = "salespagedesc"
    f = open("plugins.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close

    def parse(self, response):
        for desc in response.css('div.summary-container'):
            yield {
                'title': response.xpath('//*[@itemprop="name"][1]/text()').extract(),
                'price': response.xpath('//*[@class="price"]/ins/span/text()').extract_first(),
                'currency': response.xpath('//*[@class="price"]/ins/span/span/text()').extract_first(),
                'version': response.xpath('//*[@class="product_meta"]/p/text()[1]').re('[.0-9]+'),
                'author': response.xpath('//*[@class="summary entry-summary"]/div/li').re('(?<=distributed by )(.*)(?= \\(<a)'),
                'released': response.xpath('//*[@class="product_meta"]/p/text()[4]').re('[/0-9]+'),
                'category': response.xpath('//*[@class="posted_in"]/a/text()').extract(),
                'tags': response.xpath('//*[@class="tagged_as"]/a/text()').extract(),
                'official_sales_page': response.xpath('//*[@class="summary entry-summary"]/div/li[4]/a[1]/@href').extract(),
            }