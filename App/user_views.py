from App.models import db, Users
from flask import Blueprint, request, render_template, url_for, redirect
from flask import session
import json
from functools import wraps

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/create_db/')
def create_db():
    """
    创建数据库数据
    :return:
    """
    db.create_all()
    return "数据库创建成功"


@user_blueprint.route('/drop_db/')
def drop_db():
    """
    删除数据库
    :return:
    """
    db.drop_all()
    return "删除成功"


def is_login(func):
    """
    定义登陆注册验证得装饰器
    :param func:
    :return: check_login
    """
    @wraps(func)
    def check_login(*args, **kwargs):
        user_id = session.get('user_id')
        if user_id:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('user.login'))
    return check_login


@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    """
    登陆
    :return:
    """
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        result = {'status': 0, 'msg': '登陆成功'}
        username = request.values.get('username')
        password = request.values.get('password')
        if not all([username, password]):
            msg = '* 请填写好完整的信息'
            return render_template('login.html', msg=msg)

        user = Users.query.filter_by(net_name=username, password=password).first()
        if user:
            session['user_id'] = user.id
            session['username'] = user.net_name

            return json.dumps(result)
        else:
            msg = '* 用户名或者密码不一致'
            result['msg'] = msg
            result['status'] = 1
            return json.dumps(result)


@user_blueprint.route('/logout/', methods=['GET', 'POST'])
@is_login
def logout():
    if request.method == 'GET':
        session.clear()
        return redirect(url_for('user.login'))