# -*-coding:utf8-*-
from libs.db import db, cursor
import datetime


def get_users(user):
    sql = 'select * from girls where status != 1001'
    if user:
        sql += ' and user = {}'.format(user)
    cursor.execute(sql)
    users = cursor.fetchall()
    cursor.close()
    return users


def insert_user(user, pwd, nick):
    status = 1000
    create_time = current_time()
    update_time = current_time()
    sql = """insert into girls 
    (name, password, nickname, status, created_at, updated_at)
    values ({}, {}, {}, {}, {}, {})
    """.format(user, pwd, nick, status, create_time, update_time)
    cursor.execute(sql)
    affected = cursor.fetchall()
    cursor.close()
    return affected





def current_time():
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    return now
