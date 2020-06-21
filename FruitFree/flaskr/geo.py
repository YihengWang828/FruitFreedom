import functools,json
from flask import(
    Blueprint,flash,g,redirect,render_template,request,session,url_for,jsonify
)
from werkzeug.security import check_password_hash,generate_password_hash
from pyecharts import options as opts
import csv

bp=Blueprint('map',__name__,url_prefix='/map')
@bp.route('/',methods=('GET','POST'))
def fruit():
    csvFile=open("flaskr/yimutian.csv","r",encoding='utf-8')
    reader=csv.reader(csvFile)
    items=[]
    for item in reader:
        items.append(item)
    csvFile.close()
    items=items[1:]
    s=set()
    data_all={}
    for item in items:
        s.add(item[0])
    for i in s:
        data=[]
        fruit=[ item for item in items if item[0]==i]
        for item in fruit:
            data.append(
                {
                    "name":item[2],
                    "value":float(item[3])
                }
                )
        nums=[float(a[3]) for a in fruit]
        min_=min(nums)
        max_=max(nums)
        data_all[i]={
            "data":data,
            "min":min_,
            "max":max_
        }
    #print(s)
    if request.method=='GET':
        return render_template('map/map_yimutian.html')
    elif request.method=='POST':
        a=request.get_json(force=True)
        print(a)
        type_=a["name"]
        print(type_)
        print(data_all[type_])
        return jsonify({
            "name":type_,
            "data":data_all[type_]
        })