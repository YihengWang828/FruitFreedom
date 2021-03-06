
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import pandas as pd
import os
import json

path = 'E:\\大三下学期\\实训\\提交文档\\spark_script\\spark_script\\jintouwang_2019'
dir_list = os.listdir(path)


def part(line):
    lst = line.split(',')
    new_lst = []
    new_lst.append(lst[0].strip('报价'))
    date = lst[2]
    month = date.split('-')[1]
    day = date.split('-')[2]
    new_lst.append(int(month))
    new_lst.append(int(day))
    new_lst.append(float(lst[1].strip('.')))
    tup = tuple(new_lst)
    return tup


conf = SparkConf().setAppName('2019_Fruit_Price.py').setMaster('local[*]')
spark = SparkSession.builder.config(conf=conf).getOrCreate()
sc = spark.sparkContext
schema = StructType([StructField("type", StringType(), False), StructField("month", StringType(), False),
                     StructField("day", StringType(), False), StructField("price", DoubleType(), False)])

for dir in dir_list:
    csv_path = 'file:\\{}\\{}'.format(path, dir)
    #df = spark.read.format('csv').option("header", "true").schema(schema).load(csv_path)
    RDD = sc.textFile(csv_path)
    header = RDD.first()
    RDD = RDD.filter(lambda line : line != header)
    mappedRDD = RDD.map(part)
    df = spark.createDataFrame(mappedRDD, schema)
    df = df.sort("type", "month", "day")
    df.show(10)
    prop = {}
    prop['user'] = 'hadoop'  # 表示用户名是root
    prop['password'] = '123456'  # 表示密码是123
    prop['driver'] = "com.mysql.jdbc.Driver"  # 表示驱动程序是com.mysql.jdbc.Driver

    # 下面就可以连接数据库，采用append模式，表示追加记录到数据库dbtaobao的rebuy表中
    df.write.jdbc("jdbc:mysql://localhost:3306/ffdbs", '2019_Fruit_Price', 'append', prop)
    '''
    prop = {}
    prop['user'] = 'root'  # 表示用户名是root
    prop['password'] = '123'  # 表示密码是123
    prop['driver'] = "com.mysql.jdbc.Driver"  # 表示驱动程序是com.mysql.jdbc.Driver

    # 下面就可以连接数据库，采用append模式，表示追加记录到数据库dbtaobao的rebuy表中
    df.write.jdbc("jdbc:mysql://localhost:3306/datebase", '2019_Fruit_Price', 'append', prop)
    '''