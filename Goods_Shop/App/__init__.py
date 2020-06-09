from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import Config

class Middleware():
    def __init__(self,wsgi_app):
        self.wsgi_app = wsgi_app
    def __call__(self, *args, **kwargs):
        obj = self.wsgi_app(*args,**kwargs)
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request()
        return obj

db = SQLAlchemy()

from App.view import user   # 这里db要在蓝图之前，不然会报错
from App.view import exchange
from App.view import menu
from App.view import role
from App.view import depart

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(user.users)
    app.register_blueprint(exchange.change)
    app.register_blueprint(menu.menus)
    app.register_blueprint(role.roles)
    app.register_blueprint(depart.departs)
    db.init_app(app)


    return app