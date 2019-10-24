from flask import Blueprint
from flask import request, session, render_template
import json
from utils.tools_function import *

tools = Blueprint('tools', __name__)


@tools.route('/', methods=['GET'])
def tools_index():
    if request.method == 'GET':

        return render_template('tools.html')


@tools.route('/make_passwd/', methods=['POST'])
def make_passwd():
    if request.method == 'POST':
        dic = {'state': 'success', 'passwd': ""}
        passwd_level = request.values.get("passwd_level")
        passwd_num = request.values.get("passwd_num", 18)
        passwd = tools_make_passwd(passwd_level, passwd_num)
        dic['passwd'] = passwd
        return json.dumps(dic)