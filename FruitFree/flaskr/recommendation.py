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

    #测试一下
    type_="水果"
    sql="select * from all_category where category = '水果' ;"
    print(sql)
    cursor.execute(sql)
    results=cursor.fetchall()
    print(results)