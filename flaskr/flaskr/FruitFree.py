from flask import Flask,url_for,render_template,request
import pymysql
import datetime
import random
import utils

# 连接数据库
conn = pymysql.connect(host='localhost',
                       user='hadoop',
                       password='123456',
                       db='ffdbs',
                       charset='utf8')
# 创建一个游标
cursor = conn.cursor()

app = Flask(__name__)

# 推荐小窗放首页
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def gettime():
    return utils.get_time()

# 产地行情函数
@app.route('/map_distribution/',methods=['GET','POST'])
def map_distribution():
    # 查询初始设定值数据
    sql = "select region,average_price from map_distribution where category='西瓜' order by average_price limit 0,10"
    cursor.execute(sql)   # 执行sql
    # 查询所有数据，返回结果默认以元组形式，所所以可以进行迭代处理
    init_data = cursor.fetchall()

    # 获得所有水果种类
    sql_1 = "select category from map_distribution group by category"
    cursor.execute(sql_1)
    types = cursor.fetchall()
    if request.method == 'GET':
        return render_template('map_distribution.html',fruit=init_data,category="西瓜",types=types)
    else:
        category = request.form.get('category')

        # 未选择水果种类
        if category == "None":
            return render_template('map_distribution.html',fruit=init_data,category="西瓜",types=types)
        else:
            # 根据水果种类进行查询
            where = 'where category = "{}" '.format(category)
            sql = "select region,average_price from map_distribution " + where + " order by average_price limit 0,10"

        print(category)
        cursor.execute(sql)   # 执行sql
        query_data = cursor.fetchall()
        return render_template('map_distribution.html',fruit=query_data,category=category,types=types)

# 价格行情函数
@app.route('/fruit_2019_price/',methods=['GET','POST'])
def fruit_2019_price():
    # 查询初始设定值数据
    sql = "select month,day,price from 2019_fruit_price where type='哈密瓜' and month=1 order by day"
    cursor.execute(sql)   # 执行sql
    # 查询所有数据，返回结果默认以元组形式，所所以可以进行迭代处理
    init_data = cursor.fetchall()

    # 获得所有水果种类
    sql_1 = "select type from 2019_fruit_price group by type"
    cursor.execute(sql_1)
    types = cursor.fetchall()

    if request.method == 'GET':
        return render_template('fruit_2019_price.html',fruit=init_data,type="哈密瓜",month=1,year=0,types=types)
    else:
        type = request.form.get('type')
        month = int(request.form.get('month'))
        year = int(request.form.get('year'))

        # 未选择水果种类 或 时间
        if type == "None" or (month == 0 and year == 0):
            return render_template('fruit_2019_price.html',fruit=init_data,type="哈密瓜",month=1,year=0,types=types)

        if year != 0 :
            # 以年为首要指标，看全年
            where = 'where type = "{}" '.format(type)
            sql = "select month,day,price from 2019_fruit_price " + where + " order by month,day"

        else:
            # 以月份查询
            where = 'where type = "{}" '.format(type)+'and month={}'.format(month)
            sql = "select month,day,price from 2019_fruit_price " + where + " order by day"

        print(type,month,year)
        cursor.execute(sql)   # 执行sql
        query_data = cursor.fetchall()
        return render_template('fruit_2019_price.html',fruit=query_data,type=type,month=month,year=year,types=types)

# 推荐函数，小窗放哪里
@app.route('/recommend/',methods=['GET','POST'])
def recommend():
    # 今日小窗内容
    tmp_date = datetime.datetime.now() #获取系统当前时间
    tmp_month = tmp_date.month

    # 在recommend表中找适合的月份的水果种类和其省份
    sql_recommend = 'select category,province from recommend where month = {}'.format(tmp_month)
    cursor.execute(sql_recommend)
    data_recommend = cursor.fetchall()

    daily_fruit = []
    # data_recommend存储了，水果种类，省份
    for recommend_fruit in data_recommend:
        # 根据水果种类进行查询，水果种类、品牌、照片
        sql_daily = 'select type,brand,price,sales,delivermark,describemark,servermark from all_category where type = "{}" '.format(recommend_fruit[0])
        cursor.execute(sql_daily)
        # 获取每一种的前三，存入总的今日水果推荐表
        tmp_date = cursor.fetchmany(10)
        for i in tmp_date:
            daily_fruit.append(i)

    # 实际的水果推荐表
    real_recommend_fruit = random.sample(daily_fruit, 10)
    for i in real_recommend_fruit:
        print(i)

    # 查询初始设定值数据
    sql = "select picture,brand,type,sales,marks from all_category order by marks desc limit 0,10"
    cursor.execute(sql)   # 执行sql
    # 查询所有数据，返回结果默认以元组形式，所所以可以进行迭代处理
    all_recommend = cursor.fetchall()

    # 查询水果种类
    sql = "select type from all_category group by type"
    cursor.execute(sql)   # 执行sql
    # 查询所有数据，返回结果默认以元组形式，所所以可以进行迭代处理
    types = cursor.fetchall()
    if request.method == 'GET':
        return render_template('recommend.html',information=all_recommend,types=types,real_recommend=real_recommend_fruit,type='所有水果')
    else:
        type = request.form.get('type')

        # 未选择水果种类
        if type == "None":
            return render_template('recommend.html',information=all_recommend,types=types,real_recommend=real_recommend_fruit,type='所有水果')
        else:
            # 根据水果种类进行查询
            where = 'where type = "{}" '.format(type)
            sql = "select picture,brand,type,sales,marks from all_category " + where + "order by marks desc"

        print(type)
        cursor.execute(sql)   # 执行sql
        query_data = cursor.fetchall()
        return render_template('recommend.html',information=query_data,types=types,real_recommend=real_recommend_fruit,type=type)


# 执行
if __name__ == '__main__':
    app.run(debug=True)
