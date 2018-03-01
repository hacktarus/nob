# -*- coding: utf-8 -*-
from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from plugins.items import PluginsItem
import datetime
from urllib.parse import urlparse
import socket
import scrapy



class NobPlugins(scrapy.Spider):
    name = "plugins"
    allowed_domains = ["nobuna.com"]
    start_urls = (
        'https://www.nobuna.com/product-category/plugins/?product_count=20',
    )


    def parse(self, response):
        for plugin in response.css('div.product-details-container'):
            yield {
                'Sales_page_url': plugin.css('h3.product-title a::attr(href)').extract_first(),
                'title': plugin.css('h3.product-title a::text').extract_first().strip(), 
            }