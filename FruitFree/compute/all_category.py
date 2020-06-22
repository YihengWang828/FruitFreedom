from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

import pandas as pd
import os
import sys
import json

# path = '/home/huasiyu/taobao'
indexx = str(sys.path[0]).index('compute')
path_d = str(sys.path[0])[:42]      # 获取上一层路径
print(path_d)
path = path_d + 'resource/taobao'
dir_list = os.listdir(path)


def remove(line):
    lst = line.split(',')
    if lst[0] == 'dsrDeliver':
        return False
    if lst[0] == '':
        return  False
    if lst[2] == '':
        return  False
    if lst[4] == '':
        return  False
    return True


def map1(line):
    lst = line.split(',')
    new_lst = []
    new_lst.append(float(lst[0]))
    new_lst.append(float(lst[2]))
    new_lst.append(float(lst[4]))
    new_lst.append(int(lst[13]))
    return new_lst



def map2(line,avg0,avg1,avg2):
    lst = line.split(',')
    new_lst = []
    if float(lst[0])==0:
        lst[0]=avg0
    if float(lst[2])==0:
        lst[2]=avg1
    if float(lst[4])==0:
        lst[4]=avg2
    new_lst.append(float(lst[0]))
    new_lst.append(float(lst[2]))
    new_lst.append(float(lst[4]))
    new_lst.append(int(lst[13]))
    new_lst.append(lst[17].replace("\"",''))
    if lst[11]!='':
        new_lst.append(float(lst[11]))
    else:
        new_lst.append(float(lst[10]))
    new_lst.append(lst[6])
    return new_lst

def map3(line, delta0, delta1, delta2, delta3, min0, min1, min2, min3):
    marks = ((line[0]-min0)/delta0)*1+((line[1]-min1)/delta1)*4+\
            ((line[2]-min2)/delta2)*1+((line[3]-min3)/delta3)*4
    marks = float('%0.3f'%marks)
    line.append(marks)
    return line

def map4(line,fruit):
    lst = []
    lst.append(fruit)
    lst.append(line[4])
    lst.append(line[5])
    lst.append(line[3])
    lst.append(line[0])
    lst.append(line[1])
    lst.append(line[2])
    lst.append(line[7])
    lst.append(line[6])
    return lst

conf = SparkConf().setAppName('all_category.py').setMaster('local[*]')
spark = SparkSession.builder.config(conf=conf).getOrCreate()
sc = spark.sparkContext
schema = StructType([StructField("type", StringType(), False),StructField("brand", StringType(), False),
                     StructField("price", FloatType(), False),StructField("sales", LongType(), False),
                     StructField("delivermark", FloatType(), False),StructField("describemark", FloatType(), False),
                     StructField("servermark", FloatType(), False), StructField("marks", FloatType(), False),
                     StructField("picture", StringType(), False)])
all_category_df = spark.createDataFrame(sc.emptyRDD(),schema)

for dir in dir_list:
    csv_path = 'file:///{}/{}'.format(path, dir)
    #df = spark.read.format('csv').option("header", "true").schema(schema).load(csv_path)
    RDD = sc.textFile(csv_path)
    RDD = RDD.filter(remove)
    RDD_for_compute = RDD.map(map1)

    max0 = RDD_for_compute.reduce(lambda x,y : x if x[0]>y[0] else y)[0]
    min0 = RDD_for_compute.reduce(lambda x,y : y if (x[0]>y[0] and y[0]!= 0 ) else x)[0]
    rdd_avg0 = RDD_for_compute.filter(lambda x: x[0]!= 0)
    rdd_avg0 = rdd_avg0.map(lambda x: (x[0],1))
    tup_for_avg = rdd_avg0.reduce(lambda x,y: (x[0]+y[0],x[1]+y[1]))
    avg0 = float('%0.3f'%(tup_for_avg[0]/tup_for_avg[1]))

    max1 = RDD_for_compute.reduce(lambda x, y: x if x[1] > y[1] else y)[1]
    min1 = RDD_for_compute.reduce(lambda x, y: y if (x[1] > y[1] and y[1] != 0) else x)[1]
    rdd_avg1 = RDD_for_compute.filter(lambda x: x[1] != 0)
    rdd_avg1 = rdd_avg1.map(lambda x: (x[1], 1))
    tup_for_avg = rdd_avg1.reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]))
    avg1 = float('%0.3f' % (tup_for_avg[0] / tup_for_avg[1]))

    max2 = RDD_for_compute.reduce(lambda x, y: x if x[2] > y[2] else y)[2]
    min2 = RDD_for_compute.reduce(lambda x, y: y if (x[2] > y[2] and y[2] != 0) else x)[2]
    rdd_avg2 = RDD_for_compute.filter(lambda x: x[2] != 0)
    rdd_avg2 = rdd_avg2.map(lambda x: (x[2], 1))
    tup_for_avg = rdd_avg2.reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]))
    avg2 = float('%0.3f' % (tup_for_avg[0] / tup_for_avg[1]))

    max3 = RDD_for_compute.reduce(lambda x, y: x if x[3] > y[3] else y)[3]
    min3 = RDD_for_compute.reduce(lambda x, y: y if (x[3] > y[3] and y[3] != 0) else x)[3]

    RDD_to_complement = RDD.map(lambda x: map2(x,avg0,avg1,avg2))
    mappedRDD = RDD_to_complement.map(lambda x: map3(x,max0-min0,max1-min1,max2-min2,max3-min3,min0,min1,min2,min3))
    fruit = RDD.first().split(',')[12].strip('[\'').strip('\']')
    mappedRDD = mappedRDD.map(lambda x: map4(x,fruit))
    df = spark.createDataFrame(mappedRDD, schema)
    # df = df.sort('marks', ascending=False).limit(10)
    df = df.sort('marks', ascending=False)
    all_category_df = all_category_df.union(df)
    df.show(3)

all_category_df.show(10)
#all_category_df.repartition(1).write.csv('file:///home/huasiyu/all_category')
'''
    prop = {}
    prop['user'] = 'root'  # 表示用户名是root
    prop['password'] = '123'  # 表示密码是123
    prop['driver'] = "com.mysql.jdbc.Driver"  # 表示驱动程序是com.mysql.jdbc.Driver

    # 下面就可以连接数据库，采用append模式，表示追加记录到数据库dbtaobao的rebuy表中
    all_category_df.show.write.jdbc("jdbc:mysql://localhost:3306/datebase", 'all_category', 'append', prop)
'''
prop = {}
prop['user'] = 'hadoop'  # 表示用户名是root
prop['password'] = '123456'  # 表示密码是123
prop['driver'] = "com.mysql.jdbc.Driver"  # 表示驱动程序是com.mysql.jdbc.Driver

df.write.jdbc("jdbc:mysql://localhost:3306/ffdbs?useUnicode=true&characterEncoding=utf-8"
            , 'all_category'
             , 'append'
            , prop)