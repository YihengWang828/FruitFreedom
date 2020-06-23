import os
from flask import Flask
print(__name__)
def create_app(test_config=None):
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    from . import db
    db.init_app(app)
    from . import geo
    app.register_blueprint(geo.bp)
    from . import recommendation
    app.register_blueprint(recommendation.bp)
    from . import fruit_2019
    app.register_blueprint(fruit_2019.bp)
    return app