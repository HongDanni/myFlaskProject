# -*-coding:utf8-*-
from flask import Blueprint, render_template, request, jsonify
from ..app_manager.model import get_users

login_blue = Blueprint('login', __name__, template_folder='../../template', static_folder='../../static', url_prefix='/login')


@login_blue.route('/test', methods=['get'])
def test():
    return 'welcome to login'


@login_blue.route('/index', methods=['get'])
def index():
    return render_template('login/login.html')


@login_blue.route('/hello', methods=['get'])
def hello():
    return render_template('login/hello.html')


@login_blue.route('/', methods=['post'])
def login():
    data = request.form
    user = data['user']
    pwd = data['pwd']
    # 检查参数
    if not user:
        return jsonify({"code": 200, "msg": u"user parameter null"})
    if not pwd:
        return jsonify({"code": 200, "msg": u"pwd parameter null"})

    # 用户是否存在
    if len(get_users(user)) == 0:
        return jsonify({"code": 200, "msg": "username error"})
    # 判断密码是否正确（暂时不md5处理）
    user_info = get_users(user)
    password = user_info['password']
    if password != pwd:
        return jsonify({'code': 200, 'msg': 'password error'})

    return jsonify({'code': 100, 'msg': 'login success'})










