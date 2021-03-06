from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import pandas as pd
import os
import json

path = 'E:\\大三下学期\\实训\\提交文档\\spark_script\\spark_script\\yimutian'
dir_list = os.listdir(path)


def part(line):
    lst = line.split(',')
    new_lst = []
    new_lst.append(lst[0])
    date = lst[1][3:13]
    new_lst.append(date)
    new_lst.append(lst[2])
    new_lst.append(float(lst[3]))
    tup = tuple(new_lst)
    return tup


conf = SparkConf().setAppName('Map_Distribution.py').setMaster('local[*]')
spark = SparkSession.builder.config(conf=conf).getOrCreate()
sc = spark.sparkContext
schema = StructType([StructField("category", StringType(), False), StructField("date", StringType(), False),
                     StructField("region", StringType(), False), StructField("average_price", DoubleType(), False)])

for dir in dir_list:
    csv_path = 'file:\\{}\\{}'.format(path, dir)
    #df = spark.read.format('csv').option("header", "true").schema(schema).load(csv_path)
    RDD = sc.textFile(csv_path)
    header = RDD.first()
    RDD = RDD.filter(lambda line : line != header)
    mappedRDD = RDD.map(part)
    df = spark.createDataFrame(mappedRDD, schema)
    date = mappedRDD.first()[1]
    df = df.select("region", "category", "average_price")
    #df.cache()
    print(date)
    df.show(5)
    '''
    kindOfFruit = df.select("category").distinct().collect()
    print(kindOfFruit)
    dictOfName = {}
    cnt = 0
    for fruit in kindOfFruit:
        fruit = str(fruit).split('\'')[1]
        print(fruit)
        dictOfName[cnt] = fruit
        sub_table = df.where('category == \'{}\''.format(fruit)).select("province", "average_price")
        sub_table.show(3)
        cnt = cnt + 1
    '''
    prop = {}
    prop['user'] = 'hadoop'  # 表示用户名是root
    prop['password'] = '123456'  # 表示密码是123
    prop['driver'] = "com.mysql.jdbc.Driver"  # 表示驱动程序是com.mysql.jdbc.Driver

    # 下面就可以连接数据库，采用append模式，表示追加记录到数据库dbtaobao的rebuy表中
    df.write.jdbc("jdbc:mysql://localhost:3306/ffdbs", 'map_distribution', 'append', prop)

    #print(dictOfName)
    #with open('Map_Dis_dic.json', 'w', encoding='utf-8') as json_file:
        #json_str = json.dumps(dictOfName, indent=4, ensure_ascii=False)
        #json_file.write(json_str)