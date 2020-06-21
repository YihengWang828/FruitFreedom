# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv,os
class YimutianPipeline(object):
    def __init__(self):
        self.path='../../resource/yimutian/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        
    def process_item(self, item, spider):
        file_name=self.path+'yimutian_pricechart.csv'
        if(item['type_']==1):
            L=[item['name'],item['dataList']]
            with open(file_name, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(L)
            return item
        elif(item['type_']==0):
            file_name=self.path+'yimutian_locationchart.csv'
            L=[item['name'],item['title'],item['province_name'],item['province_price']]
            with open(file_name, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(L)
            return item