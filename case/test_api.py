#coding:utf-8
import unittest,ddt,os,requests
from common.base_api import *
from common.readexcel import *

# 获取case下xlsx用例路径
testxlsx = get_excelpath()

casedata = []
for filepath in testxlsx:
    testdata = ExcelUtil(filepath).dict_data()
    casedata += testdata


@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()

    @ddt.data(*casedata)
    def test_api(self,data):
        res = send_requests(self.s,data)
        # 执行结果
        res_result = res['执行结果']
        # print("返回执行结果->：%s" % res_result)
        # 断言
        if res_result == 'Pass':
            self.assertTrue(True)
        elif res_result == 'Fail':
            self.assertFalse(True)

if __name__ == '__main__':
    unittest.main()
