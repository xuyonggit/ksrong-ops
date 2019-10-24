# _*_ coding:utf-8 _*_
import random


class Mkpasswd():
    def __init__(self, level=2):
        self.level = level
        self.passwd = ""

    # 字符菜单
    # 获取指定数量数字,返回列表
    def get_num(self, num=1):
        templates = "0123456789"
        s = []
        for i in range(num):
            s.append(random.sample(templates, 1)[0])
        return s

    # 获取指定数量小写字母,返回列表
    def get_lword(self, num=1):
        L = []
        for i in range(97, 123):
            L.append(chr(i))
        s = []
        for i in range(num):
            s.append(random.sample(L, 1)[0])
        return s

    # 获取指定数量大写字母,返回列表
    def get_bword(self, num=1):
        L = []
        for i in range(65, 91):
            L.append(chr(i))
        s = []
        for i in range(num):
            s.append(random.sample(L, 1)[0])
        return s

    # 获取指定数量特殊符号,返回列表
    def get_fuhao(self, num=1):
        S = "!~`@#$%^&*()_+}{[]:;?/>.<,|"
        return random.sample(S, num)

    # 级别1(8位)
    def level1(self, num=8):
        self.passwd = ""
        # 1/2 数字 & 1/2 小写字母 & other 小写字母
        nums = num // 2
        lw = num // 2
        other = num % 2
        listofpasswd = self.get_num(nums) + self.get_lword(lw) + self.get_lword(other)
        temp_l = [x for x in range(0, len(listofpasswd))]
        while len(temp_l) > 0:
            l = random.sample(temp_l, 1)
            self.passwd = self.passwd + str(listofpasswd[l[0]])
            temp_l.remove(l[0])
        return self.passwd

    # 级别2（12位）
    def level2(self, num=12):
        self.passwd = ""
        # 1/3 数字 & 1/3 小写字母 & 1/3 大写字母  & other 小写字母
        nums = num // 3
        lw = num // 3
        bw = num // 3
        other = num % 3
        listofpasswd = self.get_num(nums) + self.get_lword(lw) + self.get_bword(bw) + self.get_lword(other)
        temp_l = [x for x in range(0, len(listofpasswd))]
        while len(temp_l) > 0:
            l = random.sample(temp_l, 1)
            self.passwd = self.passwd + str(listofpasswd[l[0]])
            temp_l.remove(l[0])
        return self.passwd

    # 级别3（18位）
    def level3(self, num=18):
        self.passwd = ""
        # 1/5 数字 & 1/5 小写字母 & 1/5 大写字母 1/5 特殊符号 & other 小写字母
        nums = num // 5
        lw = num // 5
        bw = num // 5
        fh = num // 5
        other = num % 5
        listofpasswd = self.get_num(nums) + self.get_lword(lw) + self.get_bword(bw) + self.get_fuhao(fh) + self.get_lword(other)
        temp_l = [x for x in range(0, len(listofpasswd))]
        while len(temp_l) > 0:
            l = random.sample(temp_l, 1)
            self.passwd = self.passwd + str(listofpasswd[l[0]])
            temp_l.remove(l[0])
        return self.passwd

