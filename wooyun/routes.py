from flask import render_template, Blueprint, redirect, request
from models import Bug, Drop
from sqlalchemy import or_
import re

user = Blueprint('user', __name__)


@user.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        text = request.form.get('text')
        target = request.form.get('target')
        if text == '':
            return render_template('result.html')
        if target == "bugs":
            # 查漏洞
            flag = 1
            results = Bug.query.filter(or_(Bug.wybug_title.contains(text), Bug.wybug_author.contains(text), Bug.wybug_type.contains(text))).order_by(Bug.wybug_date)
        else:
            # 查知识库
            # questions = Question.query.filter(or_(Question.title.contains(q), Question.content.contains(q))).order_by(Question.creat_time.desc())
            flag = 2
            results = Drop.query.filter(or_(Drop.title.contains(text), Drop.author.contains(text))).order_by(Drop.creat_time)
        # print(results)
        return render_template('result.html', results=results, flag=flag, num=results.count())


# 显示漏洞
@user.route('/bug/<string:tar>/', methods=['GET', 'POST'])
def showbug(tar):
    result = Bug.query.filter(Bug.wybug_id == tar).first()
    newstr = result.wybug_detail
    newstr = newstr.replace(r'http://static.loner.fm/upload/', '../../static/images/')
    newstr = newstr.replace(r'http://www.wooyun.org/whitehats/', '../../author/')
    newstr = newstr.replace(r'http://www.wooyun.org/bugs/', '""')
    result.wybug_detail = newstr
    return render_template('show.html', result=result, flag=1)


# 显示知识库
@user.route('/knowledge/<string:title>/', methods=['GET', 'POST'])
def showdrop(title):
    result = Drop.query.filter(Drop.title == title).first()
    return render_template('show.html', result=result, flag=2)


@user.route('/author/<string:author>/', methods=['GET', 'POST'])
def showauthor(author):
    D_results = Drop.query.filter(Drop.author == author).order_by(Drop.creat_time)
    B_results = Bug.query.filter(Bug.wybug_author == author).order_by(Bug.wybug_date)
    return render_template('author.html', author=author, D_results=D_results, B_results=B_results)


@user.route('/type/<string:type>/', methods=['GET', 'POST'])
def showtype(type):
    results = Bug.query.filter(Bug.wybug_type == type).order_by(Bug.wybug_date)
    return render_template('result.html', results=results, flag=1, num=results.count())



@user.route('/all/bugs/<int:page>/', methods=['GET', 'POST'])
def showallbugs(page):
    flag = 1
    results = Bug.query.order_by(Bug.wybug_date).paginate(page, per_page=100).items
    return render_template('result.html', results=results, flag=flag, page=page, num=100)


@user.route('/all/drops/<int:page>/', methods=['GET', 'POST'])
def showalldrops(page):
    flag = 2
    results = Drop.query.order_by(Drop.creat_time).paginate(page, per_page=100).items
    return render_template('result.html', results=results, flag=flag, page=page, num=100)