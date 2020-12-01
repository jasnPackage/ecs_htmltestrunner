#coding:utf-8
import unittest,ddt,os,requests
from common.base_api import *
from common.readexcel import *

# 获取case下xlsx用例路径
testxlsx = get_excelpath()
# print(testxlsx)

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
if __name__ == '__main__':
    unittest.main()
