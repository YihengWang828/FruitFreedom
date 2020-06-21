import scrapy
import re
from bs4 import BeautifulSoup
from jintouwang.items import JintouwangItem
#from spider.jintouwang_2019.jintouwang.jintouwang.items import JintouwangItem
class PricesSpider(scrapy.Spider):
    name='jintou'
    def start_requests(self):
        url='https://jiage.cngold.org/shuiguo/list_3103_all.html'
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,res):
        soup=BeautifulSoup(res.text,'lxml')
        history_news=soup.find_all(class_='history_news')
        '''
        for i in history_news:
            for a in i.find_all('a'):
                item=ProductsItem()
                item['date']=a.text
                print(item['date'],1)
                yield scrapy.Request(a['href'],callback=self.parse_1)
        '''
        for a in history_news[1].find_all('a'):
            yield scrapy.Request(a['href'],callback=self.parse_1)

    def parse_1(self,res):
        
        soup=BeautifulSoup(res.text,'lxml')
        show_info_page=soup.find_all(class_='show_info_page')
        if(len(show_info_page)!=0):
            a=show_info_page.find('a')
            url=a['href']
            yield scrapy.Request(url,callback=self.parse_1)
        div=soup.find(class_=re.compile('border_top|main_left'))
        #print(div)
        as_=div.find_all('a')
        for a in as_:
            yield scrapy.Request(a['href'],callback=self.parse_2)
        

        

    def parse_2(self,res):
        soup=BeautifulSoup(res.text,'lxml')
        div=soup.find(id='zoom')
        div_=soup.find(class_='art_tit clearfix')
        date=str(div_.find_all('p')[1].find('span').text).split()[0]
        trs=div.find_all('tr')
        tr=trs[-1]
        tds=tr.find_all('td')
        type=tds[0].text
        price=tds[1].text
        print(type,price)
        item=JintouwangItem()
        item['date']=date.strip()
        item['type_']=type.strip()
        item['price']=price.strip()
        yield item
        
