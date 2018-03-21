# -*- coding: utf-8 -*-
from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from plugins.items import PluginsItem
import datetime
from urllib.parse import urlparse
import socket
import scrapy
import re



class NobPlugins(scrapy.Spider):
    name = "plugins"
    allowed_domains = ["nobuna.com"]
    download_delay = 1
    start_urls = (
        'https://www.nobuna.com/product-category/plugins/?product_count=2000',
    )


    def parse(self, response):
        for plugin in response.css('div.product-details-container'):
            title = plugin.css('h3.product-title a::text').extract_first().strip()
            title = title.replace('/', ' ')
            title_version = title
            list_title_version =  title.split()
            title_space_zip = ' '.join(list_title_version)+'.zip'
            list_title_version.pop()
            title_space = ' '.join(list_title_version)
            
            #title_slug = '-'.join(list_title_version)

            yield {
                'title-version': title_version,
                'title' : title_space,
                #'title-slug' : title_slug,
                #'version' : version,
                #'title-slug-version' : title_slug+"-"+version,
                'title_zip' : title_space_zip,
                'Sales_page_url': plugin.css('h3.product-title a::attr(href)').extract_first(),
            }