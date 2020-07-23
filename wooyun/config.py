import os
import pymysql

DEBUG = True


HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'wooyun'
USERNAME = 'wooyun'
PASSWORD = 'qwe123'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
threaded = True
host = '0.0.0.0'
port = '80'

SQLALCHEMY_TRACK_MODIFICATIONS = False