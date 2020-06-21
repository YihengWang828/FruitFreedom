import pymysql
from flask import current_app,g
from flask.cli import with_appcontext
import click
def get_db():
    if 'db' not in g:
        g.db=pymysql.connect(
            host='localhost',
            user='hadoop',
            password='123456',
            db='ffdbs',
            charset='utf8'
        )
    return g.db
def close_db():
    db=g.pop('db',None)
    if db is not None:
        db.close()
def init_db():
    db=get_db()
    with db.cursor() as cursor:
        with current_app.open_resource('schema.sql') as f:
            ret=f.read().encode('utf8').split(';')
            # drop last empty entry
            print(ret)
            ret.pop()
            for sql_req in ret:
                cursor.execute(sql_req+';')
    
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)