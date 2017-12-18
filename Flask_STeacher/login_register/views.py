from flask import Blueprint
#注册蓝图
login_register_blu = Blueprint('login_register_blu',__name__)
#视图函数
@login_register_blu.route('/login',methods = ['GET','POST'])
def login():
    pass

@login_register_blu.route('/register',methods = ['GET','POST'])
def register():
    pass