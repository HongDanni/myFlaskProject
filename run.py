# -*-coding:utf8-*-
from apps import create_app
from conf import conf

app = create_app()

if __name__ == '__main__':
    app.run(debug=conf.DEBUG, port=conf.PORT, host=conf.HOST)
