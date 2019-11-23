# -*-coding:utf8-*-
from libs.db import db, cursor


def get_users():
    sql = 'select * from girls where status != 1001'
    cursor.execute(sql)
    users = cursor.fetchall()
    cursor.close()
    return users
