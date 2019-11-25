# -*-coding:utf8-*-
import csv
import pymysql


csv_file = open("food_info/中外名酒.csv", "r")
reader = csv.reader(csv_file)

db = pymysql.connect(host='139.224.10.202', port=3306, user='root', passwd='123456', db='danni')
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)  # 返回{}或[{}, {}, ...]


for item in reader:
    if item.line_num == 1:
        continue
    print(item)
