from flask import Blueprint,render_template
#蓝图
index_blu = Blueprint('index_blu',__name__)
#视图函数
@index_blu.route('/')
def index():
    return render_template('index_templates/index.html')