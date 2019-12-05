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


@tools.route('/finance_check/', methods=['POST'])
def finance_check():
    if request.method == 'POST':
        dic = {'state': 'success', 'mon': 0, "msg": ""}
        # 获取当前总资产
        print(request.values)
        finance_mon = request.values.get("finance_mon")
        if not finance_mon:
            dic['state'] = 'error'
            dic['msg'] = '当前总资产不能为空'
            return json.dumps(dic)

        # 获取收益率
        finance_shouyilv = request.values.get('finance_shouyilv')
        if not finance_shouyilv:
            dic['state'] = 'error'
            dic['msg'] = '收益率不能为空'
            return json.dumps(dic)
        else:
            finance_shouyilv = round(float(finance_shouyilv) / 100, 4)

        # 获取计划定投额
        finance_dingtoue = request.values.get('finance_dingtoue')
        if not finance_dingtoue:
            dic['state'] = 'error'
            dic['msg'] = '计划定投额不能为空'
            return json.dumps(dic)

        _this_time_in = tools_finance_check(int(finance_dingtoue), float(finance_shouyilv), 0.02, int(finance_mon))
        dic['mon'] = _this_time_in
        return json.dumps(dic)