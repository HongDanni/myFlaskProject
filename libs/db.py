# -*-coding:utf8-*-
import pymysql
from conf import conf


# 连接数据库
db = pymysql.connect(host=conf.DB_HOST, port=conf.DB_PORT, user=conf.DB_UN, passwd=conf.DB_PW, db=conf.DB_NAME)

# 建立游标
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)  # 返回{}或[{}, {}, ...]
# cursor = db.cursor()  # 返回()或((), (), ...)

