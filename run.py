# -*-coding:utf8-*-
from apps import create_app
from conf import conf

app = create_app()  # 获取flask实例

if __name__ == '__main__':
    # 启动服务；是否开启调试模式、监听IP和端口在conf.py里设置
    app.run(debug=conf.DEBUG, port=conf.PORT, host=conf.HOST)
