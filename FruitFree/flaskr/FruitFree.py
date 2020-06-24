from flask import Flask,url_for,render_template,request
import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost',
                       user='hadoop',
                       password='123456',
                       db='ffdbs',
                       charset='utf8')
# 创建一个游标
cursor = conn.cursor()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# 产地行情函数
@app.route('/map_distribution/',methods=['GET','POST'])
def map_distribution():
    # 查询初始设定值数据
    sql = "select region,average_price from map_distribution where category='西瓜'"
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
            sql = "select region,average_price from map_distribution " + where

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
        return render_template('recommend.html',information=all_recommend,types=types)
    else:
        type = request.form.get('type')

        # 未选择水果种类
        if type == "None":
            return render_template('recommend.html',information=all_recommend,types=types)
        else:
            # 根据水果种类进行查询
            where = 'where type = "{}" '.format(type)
            sql = "select picture,brand,type,sales,marks from all_category " + where + "order by marks desc"

        print(type)
        cursor.execute(sql)   # 执行sql
        query_data = cursor.fetchall()
        return render_template('recommend.html',information=query_data,types=types)


# 执行
if __name__ == '__main__':
    app.run(debug=True)
