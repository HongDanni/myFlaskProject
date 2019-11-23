# -*-coding:utf8-*-
from flask import Blueprint, render_template, request, jsonify
from .model import get_users

manager_blue = Blueprint('manager', __name__, template_folder='../../template', static_folder='../../static', url_prefix='/manager')


@manager_blue.route('/test', methods=['get'])
def test():
    return 'manager success'


@manager_blue.route('/register', methods=['post'])
def manager_register():
    data = request.form
    user = data['user']
    pwd = data['pwd']
    nick = data['nick']

    if not user:
        return jsonify({"code": 200, "msg": u"user参数错误"})
    if not pwd:
        return jsonify({"code": 200, "msg": u"pwd参数错误"})

    pass  # 未完待续


@manager_blue.route('/getuser', methods=['get', 'post'])
def get_user():
    users = get_users()
    return jsonify({"code": 200, "msg": u"成功", "data": users})






