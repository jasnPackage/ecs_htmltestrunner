#coding:utf-8
import base

import datetime,jsonpath,json,ast
import os,os.path
from common.mysql_pub import *
from config import readConfig
from common.base_login import *
from common.base_rely import *
from common.parameters_handle import *


# 返回当前时间，作为接诊时间，给预检分诊-接诊接口用
def get_currenttime():
    nowtime = datetime.datetime.now()
    currenttime = nowtime.strftime('%Y-%m-%d %H:%M')
    return currenttime


# 返回测试用户的userid
def get_login_userid():

    # 查询登录测试用户userid
    SQL = "select tu_id from stt_user  where loginname = " + "\"" + readConfig.loginName + "\"" +";"
    mysqlutil = MysqlUtil()

    userid = mysqlutil.mysql_getstring(SQL)
    return str(userid)



# 遍历测试用例目录data，返回所有的测试用例
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            if f.endswith('.xlsx'):
                fullname = os.path.join(root, f)
                yield fullname

def get_excel_lists(base):
    excel_lists = []
    for i in findAllFile(base):
        excel_lists.append(i)
    return excel_lists



# 获取抢救室床位，并且取空的一个床位id
def get_bed_id():
    # 调用抢救工作站，返回登录时的cookies
    cookies = triagerescue_userlogin_cookies()

    s = requests.session()
    # 请求查询抢救室床位信息接口，获取所有床位信息
    url = "http://" + readConfig.test_ip + ":" + readConfig.test_port + "/triagerescue/index/seachBedInfo"
    data = {'department':'抢救室1'}
    r = s.post(url=url,data=data,cookies=cookies)
    response = json.loads(r.text)

    # 获取一个空的床位id
    for i in response['rows']:
        if i['patient_id'] == None:
            bed_id = i['bed_id']
            break
    print(bed_id)
    return bed_id



# 获取留观室床位，并且取空的一个床位id
def get_observebed_id():
    # 调用留观工作站，返回登录时的cookies
    cookies = triageobserve_userlogin_cookies()

    s = requests.session()
    # 请求查询留观室床位信息接口，获取所有床位信息
    url = "http://" + readConfig.test_ip + ":" + readConfig.test_port + "/triageobserve/index/seachBedInfo"
    data = {'department':'留观室1'}
    r = s.post(url=url,data=data,cookies=cookies)
    response = r.json()
    print(response['rows'])

    # 获取一个空的床位id
    for i in response['rows']:
        if i['patient_id'] == None:
            bed_id = i['bed_id']
            break
    return bed_id


def get_excelpath():
    '''
    获取测试用例data所在的目录
    '''
    d = os.path.dirname(__file__)  # 返回当前文件所在目录（common文件夹路径）
    parent_path = os.path.dirname(d)  # 返回common的父级目录
    data_path = os.path.join(parent_path, 'data')  # 返回data所在目录
    case_path = get_excel_lists(data_path)  # 返回data目录下所有的excel文件
    # print(case_path)
    return case_path


# 根据run_config.ini中配置的运行环境，返回对应的ip和端口
def get_ipport():
    runmode = readConfig.runmode
    if runmode == 'test':
        ip = readConfig.test_ip  # 获取配置文件中接口ip
        port = readConfig.test_port  # 获取配置文件中接口port
    elif runmode == 'pro':
        ip = readConfig.pro_ip  # 获取配置文件中接口ip
        port = readConfig.pro_port  # 获取配置文件中接口port
    else:
        raise ValueError("run_config.ini文件运行环境(runmode)错误")
    return ip,port



def get_cookie(login_token,address):
    # 判断测试用例是否需要登录的cookie
    if address.find('/triage/') >= 0:
        if login_token == '是':
            cookies = userlogin_cookies()
        else:
            cookies = ''
    elif address.find('/triagedoctor/') >= 0:
        if login_token == '是':
            cookies = triagedoctor_userlogin_cookies()
        else:
            cookies = ''
    elif address.find('/triagerescue/') >= 0:
        if login_token == '是':
            cookies = triagerescue_userlogin_cookies()
        else:
            cookies = ''
    elif address.find('/triageobserve/') >= 0:
        if login_token == '是':
            cookies = base_login.triageobserve_userlogin_cookies()
        else:
            cookies = ''
    return cookies



# 返回请求body数据
def get_params(params,relydatas):
    # 读取测试用例的数据
    if relydatas:
        list_relydatas = ast.literal_eval(relydatas)  # string转换成list
        for j in list_relydatas:
            if '/' in j:
                rely_data = j.split('/')
                relyexcel_name = rely_data[0] + ".xlsx"  # 依赖用例所在Excel名称
                relycase_id = rely_data[1]  # 依赖用例编号
                relycase_path = rely_data[2]  # 依赖数据的取值路径
                rely_value = get_response_value(relyexcel_name, relycase_id, relycase_path)
                # 判断请求参数中是否需要userid或者其他变量
                if '$' in params:
                    params = parameters_handle(params, rely_value)
                else:
                    params = params
            elif '(' and ')' in j:
                rely_func = j

        if '*' in params:
            params = parameters_handle(params, eval(rely_func), partten=r"\*{(.*?)}")
        else:
            params = params
    return params


# 返回headers
def get_headers(type):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive"
    }

    if type == "form":
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    elif type == "json":
        headers["Content-Type"] = "application/json"
    else:
        raise ValueError("请求头header不能识别")
    return headers



# 返回新增科室的departid
def get_departid():

    # 查询登录测试用户userid
    SQL = "select td_id from stt_depart where td_name = '皮肤科';"
    mysqlutil = MysqlUtil()

    departid = mysqlutil.mysql_getstring(SQL)
    print(departid)
    return str(departid)


# 返回新增病区的wardid
def get_wardid():

    # 查询登录测试用户userid
    SQL = "select id from stt_ward where name = '抢救室3';"
    mysqlutil = MysqlUtil()

    wardid = mysqlutil.mysql_getstring(SQL)
    return str(wardid)


# 返回新增用户的userid
def get_userid():

    # 查询登录测试用户userid
    SQL = "select tu_id from stt_user where username = '郝敏';"
    mysqlutil = MysqlUtil()

    userid = mysqlutil.mysql_getstring(SQL)
    return str(userid)


# get_excelpath()

