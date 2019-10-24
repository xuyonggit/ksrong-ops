from App.models import db
from flask import Blueprint


user_blueprint = Blueprint('user_blueprint', __name__)


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