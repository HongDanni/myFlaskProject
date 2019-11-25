# -*-coding:utf8-*-
import os


class Config(object):
    DEBUG = True  # flask是否开启debug模式
    DB_NAME = 'danni'  # 数据库名称
    DB_HOST = '127.0.0.1'  # 数据库IP
    # DB_HOST = '139.224.10.202'  # 数据库IP

    DB_PORT = 3306  # 数据库端口(mysql默认为：3306)
    DB_UN = 'root'  # 数据库账号名
    DB_PW = '123456'  # 数据库密码

    # R_HOST = '127.0.0.1'  # Redis IP地址
    # R_PORT = 6379  # Redis 端口
    # R_AUTH = 'pc001762'  # Redis 密码
    #
    # bucket_name = "image"
    # access_key = '-DsUqpMMsTQzxrh20cNpbhee4GkFb_drJXXQ3I0h'
    # secret_key = 'Jm1H9fPH-xzm1as-TVycdTA6Qc0zDku_hocq66em'


class ProductionConfig(Config):
    """
    生产环境
    """
    DEBUG = False  # flask是否开启debug模式


class TestingConfig(Config):
    """
    测试环境
    """
    DB_HOST = '127.0.0.1'  # 数据库IP地址

    R_HOST = '127.0.0.1'   # Redis IP地址


class DevelopConfig(Config):
    """
    开发环境
    """
    PORT = 8082  # flask端口；flask默认监听本地127.0.0.1:5000
    HOST = '0.0.0.0'  # flask绑定ip；0.0.0.0表示监听所有地址


# 自动判断环境生产config
if os.path.exists('production.conf'):
    conf = ProductionConfig()
    conf_ver = 'conf.ProductionConfig'
    conf_env = u'生产环境'
elif os.path.exists('test.conf'):
    conf = TestingConfig()
    conf_ver = 'conf.TestingConfig'
    conf_env = u'测试环境'
else:
    conf = DevelopConfig()
    conf_ver = 'conf.DevelopConfig'
    conf_env = u'开发环境'

