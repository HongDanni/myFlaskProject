# -*-coding:utf8-*-
from flask import Flask
import os
from datetime import timedelta
from .app_login.views import login_blue
from .app_manager.views import manager_blue


def create_app():
    app = Flask(__name__)  # 创建flask实例

    app.register_blueprint(login_blue)  # 注册蓝图(路由)
    app.register_blueprint(manager_blue)

    app.config.update(SECRET_KEY=os.urandom(24))  # 设置密钥
    app.permanent_session_lifetime = timedelta(minutes=24*60)
    return app  # 返回设置完参数的flask实例

