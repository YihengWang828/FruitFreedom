
import csv, pandas,os



class JintouwangPipeline(object):


    def __init__(self):
        path='../../resource/jintouwang_2018/'
        if not os.path.exists(path):
            os.mkdir(path)
        self.filename=path+'jintouwang_2019.csv'
        if not os.path.exists(self.filename):
            header=['type','price','date']
            with open(self.filename,'a',newline='',encoding='utf-8') as f:
                writter=csv.writer(f)
                writter.writerow(header)

    def process_item(self, item, spider):
        with open(self.filename,'a',newline='',encoding='utf-8') as f:
            writter=csv.writer(f)
            writter.writerow([item['type_'], item['price'], item['date']])

        return item
