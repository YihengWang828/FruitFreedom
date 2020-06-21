# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FruitItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    year = scrapy.Field()
    month = scrapy.Field()
    day = scrapy.Field()
    # 水果种类
    fruit_type = scrapy.Field()
    # 水果价格
    fruit_price = scrapy.Field()
    # 价格单位
    price_unit = scrapy.Field()
    # 涨跌
    ups_and_downs = scrapy.Field()

