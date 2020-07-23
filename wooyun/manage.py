from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from exts import db
from models import Bug, Drop

manager = Manager(app)

# 使用 Migrate 绑定 app 和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到 manager 中
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()