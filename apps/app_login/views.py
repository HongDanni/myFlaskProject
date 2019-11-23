# -*-coding:utf8-*-
from flask import Blueprint, render_template, request, jsonify


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
        return jsonify({"code": 200, "msg": u"user参数错误"})
    if not pwd:
        return jsonify({"code": 200, "msg": u"pwd参数错误"})





