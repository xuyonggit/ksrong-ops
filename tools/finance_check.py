# -*- coding:utf-8 -*-
import random


class JiJin(object):
    def __init__(self, dingtoue, shouyilv, lixiangshouyilv=0.02):
        """
        基金定投计算
        :param dingtoue: 定投额
        :param shouyilv: 当前收益率
        :param lixiangshouyilv: 理想收益率
        """
        self.dingtoue = dingtoue
        self.shouyilv = shouyilv
        self.lixiangshouyilv = lixiangshouyilv

    def check(self):
        _s = self.dingtoue + self.dingtoue * (self.lixiangshouyilv - self.shouyilv)
        return _s

    def check_new(self, dingtoue, shouyilv):
        """
        新方案投入
        公式：本次需投入 = 定投额 + 定投额*（理想收益率 - 实际收益率）
        收益差： 0.3% 左右
        :param dingtoue: 定投额
        :param shouyilv: 实际收益率
        :return:
        """

        _s = dingtoue + round(dingtoue * (self.lixiangshouyilv - shouyilv), 2)
        return _s

    def check_new2(self, zongzichan):
        """
        新方案投入2
        公式：本次需投入 = 定投额 + 定投额*（理想收益率 - 实际收益率）* （总资产 // 定投额）
        收益差： 0.3% 左右
        :param zongzichan: 当前总资产
        :return:
        """
        _s = self.dingtoue + round(self.dingtoue * (self.lixiangshouyilv - self.shouyilv) * round(zongzichan // self.dingtoue, 2), 2)
        return _s

    def count(self, shouyilv_l):
        if isinstance(shouyilv_l, list):
            num = 1     # 初始化投入次数
            mon = self.dingtoue     # 初始化总金额
            mon_l = []  # 初始化收益记录
            all_in = self.dingtoue      # 总投入
            all_mon = mon       # 总资产
            all_shouyilv = 0  # 总收益率

            for i in shouyilv_l:
                mon = mon + self.dingtoue + round(mon * i, 2)
                num += 1

                #
                all_in += self.dingtoue
                all_mon = mon
                mon_l.append({'第{}个月资产'.format(num): mon, '第{}个月投入'.format(num): self.dingtoue})
            all_shouyilv = round((all_mon - all_in) / all_in * 100, 1)
            return {'总投入': all_in, '总资产': mon, '总收益率': all_shouyilv, 'info': mon_l}

    def count_new(self, shouyilv_l):
        if isinstance(shouyilv_l, list):
            num = 1     # 初始化投入次数
            mon = self.dingtoue     # 初始化总金额
            mon_l = []  # 初始化收益记录
            all_in = self.dingtoue
            all_mon = mon       # 总资产
            all_shouyilv = 0       # 总收益率

            for i in shouyilv_l:
                _in = self.check_new(self.dingtoue, i)
                if _in < 100:
                    _in = 100
                mon = mon +round(mon * i, 2) + _in
                num += 1
                all_in += _in
                all_mon = mon

                mon_l.append({'第{}个月资产'.format(num): mon, '第{}个月投入'.format(num): _in})
            all_shouyilv = round((all_mon - all_in) / all_in * 100, 1)
            return {'总投入': all_in, '总资产': mon, '总收益率': all_shouyilv, 'info': mon_l}

    def count_new2(self, shouyilv_l):
        if isinstance(shouyilv_l, list):
            num = 1     # 初始化投入次数
            mon = self.dingtoue     # 初始化总金额
            mon_l = []  # 初始化收益记录
            all_in = self.dingtoue
            all_mon = mon       # 总资产
            all_shouyilv = 0       # 总收益率

            for i in shouyilv_l:
                _in = self.check_new2(mon, self.dingtoue, i)
                if _in < 100:
                    _in = 100
                mon = mon +round(mon * i, 2) + _in
                num += 1
                all_in += _in
                all_mon = mon

                mon_l.append({'第{}个月资产'.format(num): mon, '第{}个月投入'.format(num): _in})
            all_shouyilv = round((all_mon - all_in) / all_in * 100, 1)
            return {'总投入': all_in, '总资产': mon, '总收益率': all_shouyilv, 'info': mon_l}


def mk_data(num):
    i = 0
    l = []
    while i < num:
        l.append(round((random.uniform(0, 4) - 2) / 10, 2))
        i += 1
    return l


# if __name__ == '__main__':
    # i = 0
    # F = JiJin(100, -0.012, lixiangshouyilv=0.01)
    # count1 = []
    # count2 = []
    # while i < 1000:
    #     l = mk_data(23)
    #     i += 1
    #     count1.append(F.count(l)['总收益率'])
    #     count2.append(F.count_new2(l)['总收益率'])
    # count1.sort()
    # count1 = count1[1:-1]
    # shouyilv_1 = round(sum(count1)/len(count1), 2)
    # count2.sort()
    # count2 = count2[1:-1]
    # shouyilv_2 = round(sum(count2)/len(count2), 2)
    #
    # print("old方法定投平均收益率：{} %".format(shouyilv_1))
    # print("new方法定投平均收益率：{} %".format(shouyilv_2))
    # print("收益差：{} %".format(shouyilv_2-shouyilv_1))
    # -------------------------------------------------------
    # l = mk_data(23)
    # print(F.count(l))
    # print(F.count_new2(l))

    # 计算本次应投入金额
    # print(F.check_new2(1800, 100, -0.03))
