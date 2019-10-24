from flask import Blueprint
from flask import request, session, render_template


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
#@is_login
def home():
    """
    主页
    :return:
    """
    if request.method == 'GET':
        # user = session.get('username')
        return render_template('home.html')

