from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import pandas as pd
import os
import sys


'''
path_yimutian = '/home/huasiyu/yimutian'
dir_yimutian_list = os.listdir(path_yimutian)

path_jintouwang = '/home/huasiyu/jintouwang_2019'
dir_jintouwang_list = os.listdir(path_jintouwang)
'''

print(sys.path[0])
indexx = str(sys.path[0]).index('compute')
path_d = str(sys.path[0])[:42]      # 获取上一层路径
print(path_d)
path_yimutian = path_d + 'resource/yimutian/first'
dir_yimutian_list = os.listdir(path_yimutian)

path_jintouwang = path_d + 'resource/jintouwang_2019'
dir_jintouwang_list = os.listdir(path_jintouwang)

def part_yimutian(line):
    lst = line.split(',')
    new_lst = []
    new_lst.append(lst[2])
    new_lst.append(float(lst[3]))
    tup = (lst[0],new_lst)
    return tup

def part_jintouwang(line):
    lst = line.split(',')
    new_lst = []
    new_lst.append(lst[0].strip('报价'))
    date = lst[2]
    month = date.split('-')[1]
    #day = date.split('-')[2]
    new_lst.append(int(month))
    #new_lst.append(int(day))
    #new_lst.append(float(lst[1].strip('.')))

    tup = tuple(new_lst)
    rdd = (tup,float(lst[1].strip('.')))
    return rdd
conf = SparkConf().setAppName('recommend.py').setMaster('local[*]')
spark = SparkSession.builder.config(conf=conf).getOrCreate()
sc = spark.sparkContext

for dir in dir_yimutian_list:
    csv_path = 'file:///{}/{}'.format(path_yimutian, dir)
    #df = spark.read.format('csv').option("header", "true").schema(schema).load(csv_path)
    RDD1 = sc.textFile(csv_path)
    header = RDD1.first()
    RDD1 = RDD1.filter(lambda line : line != header)
    mappedRDD1 = RDD1.map(part_yimutian)
    mappedRDD1 = mappedRDD1.reduceByKey(lambda x,y :y if x[1]>y[1] else x)
    mappedRDD1 = mappedRDD1.map(lambda x: (x[0],x[1][0],x[1][1]))
    df1 = spark.createDataFrame(mappedRDD1,['category','province','average_price'])
    df1.show(10)

for dir in dir_jintouwang_list:
    csv_path = 'file:///{}/{}'.format(path_jintouwang, dir)
    #df = spark.read.format('csv').option("header", "true").schema(schema).load(csv_path)
    RDD2 = sc.textFile(csv_path)
    header = RDD2.first()
    RDD2 = RDD2.filter(lambda line : line != header)
    mappedRDD2 = RDD2.map(part_jintouwang)
    mappedRDD2 = mappedRDD2.reduceByKey(lambda x, y: float('%.3f'%((x+y)/2)))
    mappedRDD2 = mappedRDD2.map(lambda x: (x[0][0],(x[0][1],x[1])))
    mappedRDD2 = mappedRDD2.reduceByKey(lambda x,y :y if x[1] >y[1] else x)
    mappedRDD2 = mappedRDD2.map(lambda x: (x[0],x[1][0]))
    df2 = spark.createDataFrame(mappedRDD2,['category','month'])
    df2.show(10)

df = df1.join(df2,'category')
df.show(10)
#df.repartition(1).write.csv('file:///home/huasiyu/recommend')
    
prop = {}
prop['user'] = 'hadoop'  # 表示用户名是root
prop['password'] = '123456'  # 表示密码是123
prop['driver'] = "com.mysql.jdbc.Driver"  # 表示驱动程序是com.mysql.jdbc.Driver

# 下面就可以连接数据库
df.write.jdbc("jdbc:mysql://localhost:3306/ffdbs?useUnicode=true&characterEncoding=utf-8"
              , 'recommend'
              , 'append'
              , prop)