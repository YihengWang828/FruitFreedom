from bs4 import BeautifulSoup
import requests
import csv

headers = {
    'Connection':'keep-alive',
    # 模拟浏览器操作
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.142 Safari/537.36'
}
# 起始页
response = requests.get('https://www.qqsgjy.com/hangqing/list.php?catid=20938',headers=headers)

# 获取每一个链接中的详细信息
def detail(response):
    soup = BeautifulSoup(response.text, 'lxml')
    item = {}

    div = soup.find('div',class_='content',id = 'article')
    if div == None:
        pass
    else:
        trs = div.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            if tds == []:
                pass
            if tr.find('span') == None:
                pass
            else:
                #print('yes')

                item['fruit_type'] = tds[0].string.strip()
                item['specification'] = tds[1].string.strip()

                span_1 = tds[2].find('span')
                if span_1 != None:
                    item['maximum_price'] = span_1.string
                else:
                    item['maximum_price'] = ''

                span_2 = tds[3].find('span')
                if span_2 != None:
                    item['minimum_price'] = span_2.string
                else:
                    item['minimum_price'] = ''

                span_3 = tds[4].find('span')
                if span_3 != None:
                    item['average_price'] = span_3.string
                else:
                    item['average_price'] = ''

                span_4 = tds[5].find('span')
                if span_4 != None:
                    item['market_name'] = span_4.string
                else:
                    item['market_name'] = tds[5].string.strip()
                # item['market_name'] = tds[5].string.strip()

                i = 0
                for td in tds:
                    if i == 6:
                        span_5 = tds[6].find('span')
                        if span_5 != None:
                            item['datetime'] = span_5.string
                        else:
                            item['datetime'] = ''
                        #item['datetime'] = tds[6].find('span').string
                    i = i+1

                print(item)

        # 存储三个字段
        if item != {}:
            writer = csv.writer(file)
            writer.writerow(
                [item['fruit_type'], item['specification'],item['maximum_price'],
                 item['minimum_price'],item['average_price'],item['market_name'], item['datetime']])

# 每一页的所有链接
def parse_link(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    div = soup.find('div',class_='catlist')
    lis = div.find_all('li')
    for li in lis:
        a = li.find('a')
        if a == None:
            pass
        else:
            url_new = a['href']
            response_new = requests.get(url_new)
            detail(response_new)        # 获取每一个链接中的详细信息


# 取到 首页 的所有水果种类链接
def parse(response):
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find('div', class_='m1r side')
    lis = div.find_all('li')

    for li in lis:
        a = li.find('a')
        b = li.find('em')
        url = a['href']
        nums = int(str(b)[str(b).index('(') + 1:str(b).index(')')].strip())
        # print(url,nums)

        if nums < 21:     # 如果不满一页，对当页的所有链接进行获取
            print("不满一页")
            parse_link(url)   # 获取该页的所有链接

        else:             # 如果满一页，获取页数，再对每一页的所有链接进行获取
            r = requests.get(url)
            soup_new = BeautifulSoup(r.text, 'lxml')
            cite = soup_new.find('cite')
            pages = int(str(cite)[str(cite).index('/') + 1:str(cite).index('页')].strip())
            # print(pages)

            # 取得每一页的url
            for p in range(1,pages+1):
                url_new = url + '&' + 'page=' + str(pages)
                parse_link(url)   # 获取该页的所有链接

# 调用

file = open('../../resource/fruit_trade/fruit_trade_01.csv', 'a+', encoding='utf-8', newline='')   # 打开文件
parse(response)
file.close()    # 关闭文件



# def detail_1(response):
#     soup = BeautifulSoup(response.text, 'lxml')
#     item = {}
#
#     div = soup.find('div',class_='content',id = 'article')
#     if div == None:
#         pass
#     else:
#         trs = div.find_all('tr')
#         for tr in trs:
#             tds = tr.find_all('td')
#             if tds == []:
#                 pass
#             if tr.find('span') == None:
#                 pass
#             else:
#                 #print('yes')
#
#                 item['fruit_type'] = tds[0].string.strip()
#                 item['specification'] = tds[1].string.strip()
#
#                 span_1 = tds[2].find('span')
#                 if span_1 != None:
#                     item['maximum_price'] = span_1.string
#                 else:
#                     item['maximum_price'] = ''
#
#                 span_2 = tds[3].find('span')
#                 if span_2 != None:
#                     item['minimum_price'] = span_2.string
#                 else:
#                     item['minimum_price'] = ''
#
#                 span_3 = tds[4].find('span')
#                 if span_3 != None:
#                     item['average_price'] = span_3.string
#                 else:
#                     item['average_price'] = ''
#
#                 span_4 = tds[5].find('span')
#                 if span_4 != None:
#                     item['market_name'] = span_4.string
#                 else:
#                     item['market_name'] = tds[5].string.strip()
#                 # item['market_name'] = tds[5].string.strip()
#
#                 i = 0
#                 for td in tds:
#                     if i == 6:
#                         span_5 = tds[6].find('span')
#                         if span_5 != None:
#                             item['datetime'] = span_5.string
#                         else:
#                             item['datetime'] = ''
#                         #item['datetime'] = tds[6].find('span').string
#                     i = i+1
#
#
#                 print(item)
#
# response = requests.get('https://www.qqsgjy.com/hangqing/show.php?itemid=2574')
# detail_1(response)



