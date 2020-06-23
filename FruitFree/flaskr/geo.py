import functools,json
from flask import(
    Blueprint,flash,g,redirect,render_template,request,session,url_for,jsonify
)
from werkzeug.security import check_password_hash,generate_password_hash
from pyecharts import options as opts
import csv
from . import db

bp=Blueprint('map',__name__,url_prefix='/map')
@bp.route('/',methods=('GET','POST'))
def fruit():
    conn=db.get_db()
    cursor =conn.cursor()
    
    if request.method=='GET':
        return render_template('map/map_yimutian.html')
    elif request.method=='POST':
        a=request.get_json(force=True)
        print(a)
        type_=a["name"]
        sql="select * from Map_Distribution where category = '"+type_+"';"
        print(sql)
        cursor.execute(sql)
        results=cursor.fetchall()
        print(results)
        prices=[]
        data=[]
        for re in results:
            prices.append(re[2])
            data.append({
                "name":re[0],
                "value":re[2]
            })
        max_=max(prices)
        min_=min(prices)
        print(max_,min_)
        print(data)
        print(
            {
                "name":type_,
                "max":max_,
                "min":min_,
                "data":data
            }
        )
        return jsonify({
            "name":type_,
            "max":max_,
            "min":min_,
            "data":data
        })