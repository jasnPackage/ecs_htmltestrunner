#coding:utf-8
import unittest,ddt,os,requests
from common.readexcel import *

testxlsx = get_excelpath()
for filepath in testxlsx:
    testdata = ExcelUtil(filepath).dict_data()

@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()

    @ddt.data(*testdata)
    def test_api(self,data):
        res = 1
        pass
