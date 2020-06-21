# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YimutianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    data_id=scrapy.Field()
    href=scrapy.Field()
    title=scrapy.Field()
    province_name=scrapy.Field()
    province_price=scrapy.Field()
    dataList=scrapy.Field()
    type_=scrapy.Field()
    pass

