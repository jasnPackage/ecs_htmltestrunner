#coding:utf-8
import base
from common.mysql_pub import MysqlUtil
from config import readConfig
import requests

s = requests.session()

# 用户登录ecs
def userlogin():
    # 调用登录接口
    login_url = "http://" + readConfig.test_ip + ":" + readConfig.test_port + "/sso/login"
    login_data = {"username": readConfig.loginName, "password": readConfig.password, "mac": ""}
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/74.0.3729.131 Safari/537.36"
    }
    r = s.post(login_url, data=login_data, headers=headers)


# 预检分诊工作台，返回登录用户的cookies
def userlogin_cookies():
    # 用户登录ecs
    userlogin()

    # 访问预检分诊首页，如果不访问，直接调用接口会报重定向次数过多
    triageindex = "http://" + readConfig.test_ip + ":" + readConfig.test_port + "/triage/index"
    r = s.get(triageindex)
    return s.cookies



# 医生站，返回登录用户的cookies
def triagedoctor_userlogin_cookies():
    # 用户登录ecs
    userlogin()

    # 访问医生站首页，如果不访问，直接调用接口会报重定向次数过多
    triageindex = "http://" + readConfig.test_ip + ":" + readConfig.test_port + "/triagedoctor/index"
    r = s.get(triageindex)
    return s.cookies



# 抢救工作站，返回登录用户的cookies
def triagerescue_userlogin_cookies():
    # 用户登录ecs
    userlogin()

    # 访问医生站首页，如果不访问，直接调用接口会报重定向次数过多
    triageindex = "http://" + readConfig.test_ip + ":" + readConfig.test_port + "/triagerescue/index"
    r = s.get(triageindex)
    print(s.cookies)
    return s.cookies



# 留观工作站，返回登录用户的cookies
def triageobserve_userlogin_cookies():
    # 用户登录ecs
    userlogin()

    # 访问医生站首页，如果不访问，直接调用接口会报重定向次数过多
    triageindex = "http://" + readConfig.test_ip + ":" + readConfig.test_port + "/triageobserve/index"
    r = s.get(triageindex)
    return s.cookies

COOKIES_PATH = r'C:\Users\Administrator\PycharmProjects\ECS\cookies.txt'

# 预检分诊工作台，返回登录用户的cookies
def userlogin_cookies2():
    # 用户登录ecs
    userlogin()

    # 访问预检分诊首页，如果不访问，直接调用接口会报重定向次数过多
    triageindex = "http://" + readConfig.test_ip + ":" + readConfig.test_port + "/triage/index"
    r = s.get(triageindex)
    cookies = s.cookies
    # print(cookies)
    foo = []
    # 遍历 cookies 拆分 dict 并拼接为特定格式的 str
    # 如: server=xxxxx; sid=xxxxxx; track=xxxxx;
    for k, v in cookies.items():
        foo.append(k + '=' + v + '; ')
    bar = "".join(foo)
    print(bar)
    with open(COOKIES_PATH, 'w') as f:
        f.write(bar)
    # cookies = s.cookies.items()
    #
    # cookie = ''
    # for name, value in cookies:
    #     cookie += '{0}={1};'.format(name, value)
    # return cookie



# userlogin_cookies2()








