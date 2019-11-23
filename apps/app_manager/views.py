# -*-coding:utf8-*-
from flask import Blueprint, render_template, request, jsonify
from .model import get_users

manager_blue = Blueprint('manager', __name__, template_folder='../../template', static_folder='../../static', url_prefix='/manager')


@manager_blue.route('/test', methods=['get'])
def test():
    return 'manager success'


# 用户的用户名(user)不能重复
@manager_blue.route('/register', methods=['post'])
def manager_register():
    data = request.form
    user = data['user']
    pwd = data['pwd']
    nick = data['nick']
    return jsonify({'nick': nick})

    if not user:
        return jsonify({"code": 200, "msg": u"user parameter error"})
    if not pwd:
        return jsonify({"code": 200, "msg": u"pwd parameter error"})

    # 查找是否已经有相同user的会员
    user = get_users(user)
    if len(user) != 0:
        return jsonify({"code": 200, "msg": u"user already exists"})
    # 没有即新增会员信息




    pass  # 未完待续


# 获取所有会员信息
@manager_blue.route('/getuser', methods=['get', 'post'])
def get_user():
    users = get_users('')
    return jsonify({"code": 200, "msg": u"成功", "data": users})






