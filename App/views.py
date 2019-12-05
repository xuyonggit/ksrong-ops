from flask import Blueprint
from flask import request, session, render_template
from App.user_views import is_login
from App.models import Users

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
@is_login
def home():
    """
    主页
    :return:
    """
    if request.method == 'GET':
        user_id = session.get('user_id')
        username = Users.query.filter_by(id=user_id).first().name
        print(username)
        return render_template('home.html')

