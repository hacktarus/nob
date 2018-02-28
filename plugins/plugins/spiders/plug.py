import scrapy


class NobPlugins(scrapy.Spider):
    name = "plugins"
    start_urls = [
        'https://www.nobuna.com/product-category/plugins/?product_count=20',
    ]

    def parse(self, response):
        for plugin in response.css('div.product-details'):
            yield {
                'text': plugin.css('h3.product-title::text').extract_first(),
            }