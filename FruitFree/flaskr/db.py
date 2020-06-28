import FruitFree.config
import pymysql
from flask import current_app,g
from flask.cli import with_appcontext
import click
from  FruitFree.compute.y2019_Fruit_Price import go_0
from FruitFree.compute.recommend import go_1
from FruitFree.compute.Map_Distribution import go_2
from FruitFree.compute.Fruit import go_3
from FruitFree.compute.all_category import go_4
def get_db():
    if 'db' not in g:
        g.db=pymysql.connect(
            host='localhost',
            user=FruitFree.config.user,
            password=FruitFree.config.password,
            db=FruitFree.config.database,
            charset='utf8'
        )
    return g.db
def close_db(e=None):
    db=g.pop('db',None)
    if db is not None:
        db.close()
def init_db():
    db=get_db()
    with db.cursor() as cursor:
        with current_app.open_resource('schema.sql') as f:
            ret=f.read().decode('utf8').split(';')
            # drop last empty entry
            print(ret)
            ret.pop()
            for sql_req in ret:
                cursor.execute(sql_req+';')
    
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('初始化表完成')
    go_0()
    go_1()
    go_2()
    go_3()
    go_4()
    click.echo('数据写入完成')
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)