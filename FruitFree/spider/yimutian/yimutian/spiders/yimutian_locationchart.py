import scrapy
import re
import json
from bs4 import BeautifulSoup
from copy import deepcopy
import os
import csv
import time
from yimutian.items import YimutianItem
#from products.items import ProductsItem
class yimutianSpider(scrapy.Spider):
    name='yimutian'
    allowed_domains = ['hangqing.ymt.com']
    def start_requests(self):
        headers={
            "Referer": "http://hangqing.ymt.com/chandi_8426_0_-1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        }
        url='http://hangqing.ymt.com/chandi/'
        yield scrapy.Request(url=url,callback=self.parse,headers=headers,dont_filter=True)

    def parse(self,res):
        #print(res.text)
        soup=BeautifulSoup(res.text,'lxml')
        wrapper=soup.find(id='purchase_wrapper')
        a_shuiguo=wrapper.find_all('a')
        #print(a_shuiguo[1])
        headers={
            #"Referer": "http://hangqing.ymt.com/chandi_8426_0_-1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        }
        yield scrapy.Request(url='http://hangqing.ymt.com/common/nav_chandi_'+a_shuiguo[1]['data-id'],callback=self.parse_1,headers=headers,dont_filter=True)

        

    def parse_1(self,res):
        soup=BeautifulSoup(res.text,'lxml')
        cate_detail_all=soup.find_all(class_=re.compile('cate_detail_con'))
        headers={
            "Referer": "http://hangqing.ymt.com/chandi_8426_0_-1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "Cache-Control": "no-cache"
        }
        as_=[]
        for i in range(1,7):
            print(3)
            cate_detail_one=cate_detail_all[i]
            lis=cate_detail_one.find_all('li')
            #print(len(lis))
            for li in lis:
                a=li.find(href=re.compile('http'))
                #print(a)
                as_.append(a)
        print(len(as_))
        for a in as_:
            item=YimutianItem()
            item['name']=a.string
            item['data_id']=a['data-id']
            item['href']=a['href']
            #yield scrapy.Request(item['href'],callback=self.parse_2,meta={"item":deepcopy(item)})
            
            form_data={
                "locationId":"0",
                "productId":item["data_id"],
                "breedId":"0"
            }
            print(1)
            #print(form_data)
            yield scrapy.FormRequest(
                            "http://hangqing.ymt.com/chandi/location_charts",
                            formdata=form_data,
                            callback=self.parse_3,
                            meta=item,
                            dont_filter=True
                        )
    def parse_3(self,res):
        print(2)
        items=res.meta
        print(items)
        item=YimutianItem()
        item['name']=items['name']
        item['href']=items['href']
        item['data_id']=items['data_id']
        html_str=json.loads(res.text)
        status=html_str['status']
        if status==0:
            dataList=html_str["data"]["dataList"]
            item['title']=html_str["data"]["title"]
            item['type_']=0
            for data in dataList:
                if type(data)==type([]):
                    item["province_name"]=data[0]
                    item["province_price"]=data[1]
                elif type(data)==type({}):
                    item["province_name"]=data["name"]
                    item["province_price"]=data["y"]
                yield item
