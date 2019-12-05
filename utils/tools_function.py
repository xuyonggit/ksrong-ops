from tools.mkpasswd import Mkpasswd
from tools.finance_check import JiJin

def tools_make_passwd(pwd_level, pwd_num):
    pwd_num = int(pwd_num)
    MK = Mkpasswd()
    if int(pwd_level) == 1:
        result = MK.level1(pwd_num)
    elif int(pwd_level) == 2:
        result = MK.level2(pwd_num)
    else:
        result = MK.level3(pwd_num)
    return result


def tools_finance_check(dingtoue, shouyilv, lixiangshouyilv, mon):
    """
    计算本次投入
    :param dingtoue: 定投额
    :param shouyilv: 当前收益率
    :param lixiangshouyilv: 理想收益率
    :param mon: 当前总资产
    :return:
    """
    J = JiJin(dingtoue, shouyilv, lixiangshouyilv)
    return J.check_new2(mon)