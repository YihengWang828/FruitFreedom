import functools,json
from flask import(
    Blueprint,flash,g,redirect,render_template,request,session,url_for,jsonify
)
from werkzeug.security import check_password_hash,generate_password_hash
from pyecharts import options as opts
import csv
from . import db

bp=Blueprint('jintou',__name__)
@bp.route('/jintou/',methods=('GET','POST'))
def fruit_2019():
    conn=db.get_db()
    cursor=conn.cursor()
    '''
    #测试一下
    type_="'西瓜'"
    sql="select day from 019_Fruit_Price ;"
    print(sql)
    cursor.execute(sql)
    results=cursor.fetchall()
    print(results)
    '''
    if request.method=='GET':
        return render_template('fruit_hangqing.html')
    elif request.method=='POST':
        a=request.get_json(force=True)
        print(a)
        type=a['name']
        month=a['month']
        sql="select day,price from 2019_Fruit_Price where type='"+type+"' and month="+month+" order by day;"
        print(sql)
        cursor.execute(sql)
        res=cursor.fetchall()
        print(res)
        date=[]
        value=[]
        for re in res:
            date.append(re[0])
            value.append(re[1])
        print({
            "date":date,
            "value":value
        })
        return jsonify({
            "date":date,
            "value":value
        })
@bp.route('/index/',methods=('GET',),endpoint='index')
def index():
    return render_template('shouye.html')