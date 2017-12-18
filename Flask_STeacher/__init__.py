from flask import Flask
#初始化应用对象
app = Flask(__name__)
#蓝图
from Flask_STeacher.login_register.views import login_register_blu
app.register_blueprint(login_register_blu,url_prefix = '/login_register')

from Flask_STeacher.index.views import index_blu
app.register_blueprint(index_blu)