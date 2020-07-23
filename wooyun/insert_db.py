# 将文件内容导入数据库

import os
import re
from exts import db
from models import Bug, Drop
from app import app

drop_path = "./drops" # 文件存放位置
bug_path = "./bugs"


def getDropsInfo(path):
	info_list = []
	filenames = os.listdir(path)  # 取得文件名
	print(len(filenames))
	for file in filenames:
		info = {"title":re.sub(".html", "", re.sub(r"\d+\.", "", file)), "author": "", "creat_time": "", "content": ""}
		with open(path+"/"+file, encoding ='utf-8') as f:
			text = f.read()
			match_author = re.findall(r'<a target="_blank" class="author name ng-binding">(.*?)</a>', text, re.DOTALL)
			if match_author=="":
				match_author="带头大哥"
			match_time = re.findall(r'<time title="(.*?) ', text, re.DOTALL)
			if match_time=="":
				match_time = "2012/02/30"
			info['author'] = match_author
			info['creat_time'] = match_time
			info['content'] = text
		info_list.append(info)
	# 插入到数据库中
	for info in info_list:
		with app.app_context():
			new_Drop = Drop(title=info['title'], author=info['author'], creat_time=info['creat_time'], content=info['content'])
			try:
				db.session.add(new_Drop)
				db.session.commit()
			except:
				print("fail!")
				db.session.rollback()

if __name__ == '__main__':

	getDropsInfo(drop_path)