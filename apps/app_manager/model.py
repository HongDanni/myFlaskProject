# -*-coding:utf8-*-
from libs.db import db
import datetime
import pymysql


# 根据用户名user获取对应的用户信息；如果user为空，则获取所有用户信息
def get_users(user):
    sql = 'select * from girls where status != 1001'
    if user:
        sql += ' and name = %a' % user
    # 数据库的连接参数在libs/db.py设置
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)  # 返回{}或[{}, {}, ...]
    cursor.execute(sql)
    users = cursor.fetchall()
    cursor.close()  # 记得要关闭
    return users


def insert_user(user, pwd, nick):
    status = 1000
    create_time = current_time()
    update_time = current_time()
    # sql = """insert into girls
    # (name, password, nickname, status, created_at, updated_at)
    # values ({}, {}, {}, {}, {}, {})
    # """.format(user, pwd, nick, status, create_time, update_time)
    print(create_time)
    print(user)

    sql = """insert into girls 
        (name, password, nickname, status, created_at, updated_at)
        values ('%s', '%s', '%s', %d, '%s', '%s')
        """ % (user, pwd, nick, status, create_time, update_time)  # 一定要写成'%s'这种，不管用format或者不加引号就会报错
    print(sql)  # 打印出来的sql语句没有错误，但是在代码里插入就始终是失败的
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)  # 返回{}或[{}, {}, ...]
    res = cursor.execute(sql)
    print(res)
    affected = cursor.fetchall()
    db.commit()
    cursor.close()
    return affected





def current_time():
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    return now
