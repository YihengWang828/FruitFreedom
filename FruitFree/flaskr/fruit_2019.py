import functools,json
from flask import(
    Blueprint,flash,g,redirect,render_template,request,session,url_for,jsonify
)
from werkzeug.security import check_password_hash,generate_password_hash
from pyecharts import options as opts
import csv
from . import db

bp=Blueprint('jintou',__name__,url_prefix='/jintou')
@bp.route('/',methods=('GET','POST'))
def fruit_2019():
    conn=db.get_db()
