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

# 查询数据
sql = "select month,day,price from 2019_fruit_price where type='哈密瓜' and month=1 order by day"
cursor.execute(sql)   # 执行sql
# 查询所有数据，返回结果默认以元组形式，所所以可以进行迭代处理
data = cursor.fetchall()

# 获得所有水果种类
sql_1 = "select type from 2019_fruit_price group by type"
cursor.execute(sql_1)
types = cursor.fetchall()
print(types[0][0])



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# 产地行情函数
@app.route('/map_distribution/')
def map_distribution():
    return render_template('map_distribution.html')

# 价格行情函数
@app.route('/fruit_2019_price/',methods=['GET','POST'])
def fruit_2019_price():
    if request.method == 'GET':
        return render_template('fruit_2019_price.html',fruit=data,type="哈密瓜",month=1,year=0,types=types)
    else:
        type = request.form.get('type')
        month = int(request.form.get('month'))
        year = int(request.form.get('year'))

        # 未选择水果种类 或 时间
        if type == "None" or (month == 0 and year == 0):
            return render_template('fruit_2019_price.html',fruit=data,type="哈密瓜",month=1,year=0,types=types)

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
        datas = cursor.fetchall()
        return render_template('fruit_2019_price.html',fruit=datas,type=type,month=month,year=year,types=types)

# 推荐函数
@app.route('/recommend/')
def recommend():
    return render_template('recommend.html')

# 执行
if __name__ == '__main__':
    app.run(debug=True)
