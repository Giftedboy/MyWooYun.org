from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from exts import db

## bugs
class Bug(db.Model):
    __tablename__ = 'bugs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wybug_id = db.Column(db.String(50), nullable=False)  # 漏洞编号
    wybug_title = db.Column(db.String(150), nullable=False)  # 标题
    wybug_author = db.Column(db.String(50), nullable=False)  # 作者
    wybug_date = db.Column(db.String(50), nullable=False)  # 时间
    wybug_type = db.Column(db.String(50), nullable=False)  # 内容
    wybug_level = db.Column(db.String(20), nullable=False)
    wybug_detail = db.Column(db.Text, nullable=False)
    replys = db.Column(db.Text, nullable=False)


class Drop(db.Model):
    __tablename__ = 'drop'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)  # 标题
    author = db.Column(db.String(50), nullable=False)  # 作者
    creat_time = db.Column(db.String(50), nullable=False)  # 时间
    content = db.Column(db.Text, nullable=False)  # 内容