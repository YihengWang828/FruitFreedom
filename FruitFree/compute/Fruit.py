from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import pandas as pd
import os
import json

# path = '/home/huasiyu/fruit_trade'
# path = 'C:/Users/Hazewu/Desktop/spark_script/spark_script/fruit_trade'
indexx = str(sys.path[0]).index('compute')
path_d = str(sys.path[0])[:42]      # 获取上一层路径
print(path_d)
path = path_d + 'resource/fruit_trade'
dir_list = os.listdir(path)
provinces = [
    '河北','山西','内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西',
    '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '四川', '贵州', '云南', '西藏', '陕西',
    '甘肃', '青海', '宁夏', '新疆', '北京', '天津', '上海', '重庆'
]

def part(line):
    lst = line.split(',')
    new_lst = []
    region = lst[5]
    flag = 0
    for province in provinces:
        if region.find(province) != -1:     # 找到
            region = province
            flag = 1
            break

    # if flag != 1:
    #     if region.find('市') != -1:
    #         region = str(region)[:str(region).index('市')]
    #     else:
    #         region = ''

    new_lst.append(region)
    new_lst.append(lst[0])
    new_lst.append(float(lst[4]))
    if lst[3] == '':
        new_lst.append(float(lst[4]))
    else:
        new_lst.append(float(lst[3]))
    if lst[2] == '':
        new_lst.append(float(lst[4]))
    else:
        new_lst.append(float(lst[2]))
    new_lst.append(lst[6])
    tup = tuple(new_lst)
    return tup

def remove(line):
    lst = line.split(',')

    # 判断是否有7个，防止数组越界
    i = 0
    for ls in lst:
        i = i + 1
    if i != 7:
        return False

    if lst[0]=='':
        return False
    if lst[5]=='':
        return False
    if lst[6]=='':
        return False

    # 剔除2020-12-   数据
    x = str(lst[6]).endswith('-')
    if x:
        return False

    return True

conf = SparkConf().setAppName('Fruit.py').setMaster('local[*]')
spark = SparkSession.builder.config(conf=conf).getOrCreate()
sc = spark.sparkContext
schema = StructType([StructField("region", StringType(), False), StructField("category", StringType(), False),
                     StructField("avg_price", DoubleType(), False), StructField("min_price", DoubleType(), False),
                     StructField("max_price", DoubleType(), False), StructField("time", StringType(), False)])

for dir in dir_list:
    csv_path = 'file:///{}/{}'.format(path, dir)
    #df = spark.read.format('csv').option("header", "true").schema(schema).load(csv_path)
    RDD = sc.textFile(csv_path)
    RDD = RDD.filter(lambda line: remove(line))
    mappedRDD = RDD.map(part)
    df = spark.createDataFrame(mappedRDD, schema)
    df = df.distinct()
    #df = df.sort("region", "category", "time")
    df = df.orderBy("region", "category", "time")
    df.show(5)
    '''
    prop = {}
    prop['user'] = 'root'  # 表示用户名是root
    prop['password'] = '123'  # 表示密码是123
    prop['driver'] = "com.mysql.jdbc.Driver"  # 表示驱动程序是com.mysql.jdbc.Driver

    # 下面就可以连接数据库，采用append模式，表示追加记录到数据库dbtaobao的rebuy表中
    df.write.jdbc("jdbc:mysql://localhost:3306/datebase", 'Fruit', 'append', prop)
    '''

    prop = {}
    prop['user'] = 'hadoop'  # 表示用户名是root
    prop['password'] = '123456'  # 表示密码是123
    prop['driver'] = "com.mysql.jdbc.Driver"  # 表示驱动程序是com.mysql.jdbc.Driver

    df.write.jdbc("jdbc:mysql://localhost:3306/ffdbs?useUnicode=true&characterEncoding=utf-8"
                  , 'fruit'
                  , 'append'
                  , prop)