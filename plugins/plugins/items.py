from scrapy.item import Item, Field


class PluginsItem(Item):
        # Primary fields
        title = Field()
        version = Field()
        sales_page_url = Field()

        # Housekeeping fields
        url = Field()
        project = Field()
        spider = Field()
        server = Field()
        date = Field()

class SalespageItem(Item):
        # Primary fields
        product_title = Field()
        version = Field()
        price = Field()
        developer = Field()
        official_sales_page = Field()
        released = Field()
        category = Field()
        tags = Field()
        