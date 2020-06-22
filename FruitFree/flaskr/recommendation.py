import functools,json
from flask import(
    Blueprint,flash,g,redirect,render_template,request,session,url_for,jsonify
)
from werkzeug.security import check_password_hash,generate_password_hash
from pyecharts import options as opts
import csv
from . import db

bp=Blueprint('recom',__name__,url_prefix='/recom')
@bp.route('/max',methods=('GET','POST'))
def recom_max():
    conn=db.get_db()


def recom_min():
    conn=db.get_db()