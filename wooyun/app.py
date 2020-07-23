from flask import Flask
import os
import config
from exts import db
from routes import user

app = Flask(__name__)
app.config['thread'] = 10
app.config.from_object(config)
db.init_app(app)

app.register_blueprint(user)


if __name__ == '__main__':
    app.run()
