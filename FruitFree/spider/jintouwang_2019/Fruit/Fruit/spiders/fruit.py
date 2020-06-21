# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from Fruit.items import FruitItem


class FruitSpider(scrapy.Spider):
    name = "fruit"
    allowed_domains = ["jiage.cngold.org"]

    # 系统框架默认的起始请求设定，暂时只取榴莲
    start_urls = ['https://jiage.cngold.org/shuiguo/lizi/']

    # 也可以自己去定义起始的逻辑
    # def start_requests(self):
    #     for i in range(9):
    #         url = 'https://jiage.cngold.org/shuiguo/liulian/list_4066_{}.html'.format(i+2)
    #         yield  scrapy.Request(url=url,callback=self.parse)      # 回调函数，不用带参数

    # 第一步：取到 榴莲报价的所有分页链接
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find('div', class_='show_info_page')
        aa = div.find_all('a')
        for a in aa:
            print(a['href'])

        # 第一页
        yield  scrapy.Request(url='https://jiage.cngold.org/shuiguo/lizi/index.html'
                              ,callback=self.parse_link)

        # yield  scrapy.Request(url='https://jiage.cngold.org/shuiguo/liulian/list_4066_4.html'
        #                       ,callback=self.parse_link)

        # 对后面的每一页分页链接发起请求
        for a in aa:
           url = a['href']
           yield  scrapy.Request(url=url,callback=self.parse_link)      # 回调函数，不用带参数

    # 采集排行榜入口页面链接，并发起详情请求
    def parse_link(self,response):
        soup = BeautifulSoup(response.text, 'lxml')
        uls = soup.find('ul', class_='news_list news_list_lab')
        lis = uls.find_all('li')

        for li in lis:
            url = li.find('a')['href']
            # print('liulian:',url)
            yield  scrapy.Request(url=url,callback=self.parse_detail)

    # 采集价格详情
    def parse_detail(self,response):
        soup = BeautifulSoup(response.text, 'lxml')

        item = FruitItem()

        # title = 金投价格频道提供今日榴莲价格多少钱一斤,最新榴莲价格行情查询（2020年06月09日）。
        title = soup.find('div',class_='art_content').find('p')
        item['year'] = str(title)[str(title).index('（') + 1:str(title).index('年')].strip()

        # th = 06月09日榴莲价格多少钱一斤_今日榴莲价格行情查询
        th = soup.find('div',class_='art_content').find('th').string
        item['month'] = str(th)[:str(th).index('月')].strip()
        item['day'] = str(th)[str(th).index('月') + 1:str(th).index('日')].strip()

        tds = soup.find('div',class_='art_content').find_all('td')
        item['fruit_type'] = tds[0].string.strip()
        item['fruit_price'] = tds[1].string.strip()
        item['price_unit'] = tds[2].string.strip()
        item['ups_and_downs'] = tds[3].string.strip()

        # print(item)

        # 将数据回传，进入Pipeline中进行处理
        yield  item