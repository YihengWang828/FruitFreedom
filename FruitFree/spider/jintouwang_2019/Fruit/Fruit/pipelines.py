# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import pandas

# 讲fruit采集到的数据存储到csv中
class FruitPipeline(object):

    # 对象初始化函数
    def __init__(self):
        self.file = open('lizi.csv','a+',encoding='utf-8',newline='')
        self.writer = csv.writer(self.file)

    # 对spider传过来的item对象进行处理
    def process_item(self, item, spider):
        # 数据处理：比如缺失数据整理、删除；重复数据清理；不合理数据的整理
        if item['fruit_type'] == '李子报价':
            item['fruit_type'] = '李子'
        # elif item['fruit_type'] != '桃子':
        #     return item

        if item['year'] != '2019':
            return item

        # 数据存储
        self.writer.writerow([item['month'],item['day'],item['fruit_type'],
                              item['fruit_price'],item['price_unit'],item['ups_and_downs']])
        return item

    def close_spider(self,spider):
        self.file.close()

        # df = pandas.read_csv('liulian.csv',delimiter=',',
        #                      names=['year','month','day','fruit_type',
        #                             'fruit_price','price_unit','ups_and_downs'])
        # df.sort_values(['year','month','day'],axis=1)
        # df.to_csv('liulian_sorted.csv')