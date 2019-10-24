from tools.mkpasswd import Mkpasswd


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