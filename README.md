## 资源地址

BaiDuYun：图片+代码+数据库文件
 链接：https://pan.baidu.com/s/1IANH7c7F9zeVgXkgrb7ATQ 提取码：n1bi

## 具体效果请看

[MyWooYun]()

## 怎么搭建
* 将所有文件下载下来
    * 源代码 `MyWooYun源码.zip`
    * 数据库文件 `WooYundata.zip`
    * 图片文件: Drops图片 `full.zip`    漏洞图片 `10-14.zip`、`15-a.zip`、`15-b.zip`、`16.zip`

* 将图片文件解压
 其中 `full.zip` 内所有图片放在代码文件中的 `full` 文件夹中
 将 `10-14.zip`、`15-a.zip`、`15-b.zip`、`16.zip` 解压放在代码文件中的 `images` 文件夹中

* 将数据库文件 
建议下载一个 `phpstudy`，然后新建一个数据库，将数据库文件 `WooYundata.zip` 解压内容放在数据库安装位置的 `data` 目录下对应数据库文件夹里面
例如：`phpstudy\Extensions\MySQL5.7.26\data\wooyun`
更改代码文件 `config.py`，中的
```
DATABASE = 'wooyun'   # 你的数据库名
USERNAME = 'wooyun'   # 数据库账号
PASSWORD = 'qwe123'   # 数据库密码
```
* 运行以下神奇代码即可
```
pip install -r requirements.txt
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
python3 -m flask run
```
* 打开 `127.0.0.1:5000` 即可



## 说明

漏洞总共包括了 88820 个， Drops 文章总共有 1235 篇，全来自公开数据，在 Github 上收集的
数据全集成到数据库中了
版权归 WooYun.org 所有
