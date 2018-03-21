# -*- coding: utf-8 -*-
import csv
import scrapy
import pandas as pd

class SalespagedescSpider(scrapy.Spider):
    name = "salespagedesc"
    download_delay = 1
    colnames =['title-version','title','title_zip','Sales_page_url']
    try:
        lines = pd.read_csv('..\\..\\..\\csv\\plugin_title.csv', names=colnames)
        titles = lines.Sales_page_url.tolist()
        titles.reverse()
        titles.pop()
        titles.reverse()
        start_urls = titles
    except FileNotFoundError:
        print("the file plugin_title.csv does not exist and we don't care !")

    #print (titles)

    def parse(self, response):
            cat = response.xpath('//head').re('(?<="content_category":")(.*)(?=","tags)')
            category = cat[0]
            tag = response.xpath('//head').re('(?<="tags":")(.*)(?=","domain)')
            tags = tag[0]
            yield {
                'title': response.xpath('//*[@itemprop="name"][1]/text()').extract(),
                'price': response.xpath('//*[@class="price"]/ins/span/text()').extract_first(),
                'currency': response.xpath('//*[@class="price"]/ins/span/span/text()').extract_first(),
                'version': response.xpath('//*[@class="tab-editor-container ywtm_content_tab"]/p').re('(?<=Version:</b> )(.*)(?=</p>)'),
                'author': response.xpath('//*[@class="tab-editor-container ywtm_content_tab"]/p').re('(?<=Developer:</b> )(.*)(?=</p>)'),
                'released': response.xpath('//*[@class="tab-editor-container ywtm_content_tab"]/p').re('(?<=Released:</b> )(.*)(?=</p>)'),
                'license': response.xpath('//*[@class="tab-editor-container ywtm_content_tab"]/p').re('(?<=License:</b> )(.*)(?=</p>)'), 
                'category': category,
                'tags': tags,
                'official_sales_page': response.xpath('//*[@class="tab-editor-container ywtm_content_tab"]/p').re('(?<=Sales Page:</b> )(.*)(?=</p>)'),
            }