import functools,json
from flask import(
    Blueprint,flash,g,redirect,render_template,request,session,url_for,jsonify
)
from werkzeug.security import check_password_hash,generate_password_hash
from pyecharts import options as opts
import csv
from . import db

bp=Blueprint('recom',__name__,url_prefix='/recom')
@bp.route('/',methods=('GET','POST'))
def recom():
    conn=db.get_db()
    cursor=conn.cursor()
    '''
    #测试一下
    type_="水果"
    sql="select * from all_category where category = '水果' order by marks desc limit 10 ;"
    print(sql)
    cursor.execute(sql)
    results=cursor.fetchall()
    print(results)
    data=[]
    for re in results:
        data.append(
            {
                "category":re[0],
                "brand":re[1],
                "price":re[2],
                "sales":re[3],
                "delivermark":re[4],
                "describemark":re[5],
                "servemark":re[6],
                "picture":re[8]
            }
        )
    print(data)
    '''
    if request.method=='GET':
        return render_template('tuijian.html')
    elif request.method=='POST':
        a=request.get_json(force=True)
        print(a)
        type_=a['name']
        
        sql="select * from all_category where category = '"+type_+"' order by marks desc limit 10 ;"
        print(sql)
        cursor.execute(sql)
        results=cursor.fetchall()
        print(results)
        data=[]
        for re in results:
            data.append(
                {
                    "category":re[0],
                    "brand":re[1],
                    "price":re[2],
                    "sales":re[3],
                    "delivermark":re[4],
                    "describemark":re[5],
                    "servemark":re[6],
                    "picture":re[8]
                    }
                )
        print(data)
        return jsonify({
            "data":data
        })