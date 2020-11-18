#coding:utf-8
import requests
import unittest
from common.logger import Log
from config import readConfig


class SSO_login(unittest.TestCase):
    '''
    用户登录
    '''

    log = Log()
    log.info("---用户登录接口测试--")

    def sso_login(self,username,password,mac=''):
        ip = readConfig.test_ip
        port = readConfig.test_port
        url = "http://" + ip + ":" + port + "/sso/userPassword"
        header = {"Content-Type":"application/x-www-form-urlencoded"}
        data = {"username":username,"password":password,"mac":mac}

        r = requests.post(url,data=data)
        result = r.text

        if self.assertIn(username,result):
            self.log.info("---测试用例通过")
        else:
            self.log.info("---测试用例失败")

    def test_login1(self):
        u'''测试用户正常登录'''
        self.sso_login('jizhen1','111111')


    def test_login2(self):
        self.sso_login()


if __name__ == "__main__":
    unittest.main()




