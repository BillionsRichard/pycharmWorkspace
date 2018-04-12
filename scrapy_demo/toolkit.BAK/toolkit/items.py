# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ToolkitItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tool_name_en = scrapy.Field()
    tool_name_cn = scrapy.Field()
    tool_size = scrapy.Field()
    release_date = scrapy.Field()
    download_cnt = scrapy.Field()
    download_url = scrapy.Field()

