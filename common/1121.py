# #!/usr/bin/python
# # coding=utf8
# # Name:  py_sendattach.py
# # Purpose:       send ptp data to antifraud
# # Author:        yangshuqiang
#
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import smtplib
# import os, sys
#
# mail_host = 'smtp.163.com'
# mail_from = 'amazinglala@163.com'
# mail_pass = '40711960556123'
#
#
# def addAttch(to_list, subject, content, path):
#     # msg = MIMEMultipart('related')  ##采用related定义内嵌资源的邮件体
#     msg = MIMEMultipart()
#     msgtext = MIMEText(content, _subtype='html', _charset='utf-8')  ##_subtype有plain,html等格式，避免使用错误
#
#     msg.attach(msgtext)
#
#     os.chdir(path)
#     dir = os.getcwd()
#
#     for fn in os.listdir(dir):  ##返回字符串文件名
#         print(fn)
#         attach = MIMEText(open(fn, 'rb').read(), "base64", "utf-8")
#         attach["Content-Type"] = 'application/octet-stream'
#         attach["Content-Disposition"] = 'attachment; filename=' + fn
#         msg.attach(attach)
#     msg['Subject'] = subject
#     msg['From'] = mail_from
#     msg['To'] = to_list
#     return msg
#
#
# def sendMail(msg):
#     try:
#         server = smtplib.SMTP()
#         server.connect(mail_host, 25)
#         server.starttls()
#         server.login(mail_from, mail_pass)
#         server.sendmail(mail_from, msg['To'], msg.as_string())
#         server.quit()  ##断开smtp连接
#         print("邮件发送成功")
#     except Exception as e:
#         print("失败" + str(e))
#
#
# if __name__ == '__main__':
#     msg = addAttch('wuxia1@3856.cc', '对账', '对账数据', r'C:\\Users\\Administrator\\PycharmProjects\\zhandian_jiekou\\report1')
#     sendMail(msg)


# a = r"C:\Users\Administrator\PycharmProjects\zhandian_jiekou\report\2017_10_10_18_11_59result.html"
# b = a.split('report\\')
# print(b[1])

# import xlrd
# data = xlrd.open_workbook(r'C:\Users\Administrator\PycharmProjects\zhandian_jiekou\data\1.xlsx')
# table = data.sheet_by_index(1)
# nrows = table.nrows
# print(table.cell_value(1,0))

# for i in range(nrows):
#     print(table.row_values(i))
#
# for i in range(1,5):
#     for j in range(0,3):
#         print(i,j)


# dict = {'Name': 'Zara', 'Age': 7}
# dict2 = {'Sex': 'female'}
#
# dict.update(dict2)
# print(dict)
# dict3 = {'Sex1': 'female1'}
#
# dict.update(dict3)
# print(dict)


# import hashlib
# import random
# import string

# def gen_random_string(str_len):
#     chars = string.ascii_letters + string.digits
#     s = [random.choice(chars) for s in range(4)]
#     print(''.join(s))


# def gen_random_string(str_len):
#     print(
#      ''.join(
#         random.choice(string.ascii_letters + string.digits) for _ in range(str_len)
#     )
#     )
#
# def gen_md5(*args):
#     print(hashlib.md5("".join(args).encode('utf-8')).hexdigest())
#
#
# gen_random_string(4)
#
# TOKEN = "debugtalk"
# data = '{"name": "user", "password": "123456"}'
# random = "A2dEx"
# gen_md5(TOKEN, data, random)


# from xlutils.copy import copy
# import xlrd
#
# rd = xlrd.open_workbook(r'C:\Users\Administrator\PycharmProjects\zhandian_jiekou\data\站点运力列表.xls')
#
# wb = copy(rd)
#
# ws = wb.get_sheet(1)
# ws.write(1,5,'pass')
# wb.save(r'C:\Users\Administrator\PycharmProjects\zhandian_jiekou\data\站点运力列表.xls')


# -*- coding: utf-8 -*-
# '''
# Created on 2012-12-17
#
# @author: walfred
# @module: XLRDPkg.write_append
# @description:
# '''
# import os
# from xlutils.copy import copy
# import xlrd as ExcelRead
#
#
# def write_append(file_name):
#     values = ["Ann", "woman", 22, "UK"]
#
#     r_xls = ExcelRead.open_workbook(file_name)
#     r_sheet = r_xls.sheet_by_index(0)
#     rows = r_sheet.nrows
#     w_xls = copy(r_xls)
#     sheet_write = w_xls.get_sheet(0)
#
#     for i in range(0, len(values)):
#         sheet_write.write(i, rows, values[i])
#
#     w_xls.save(file_name);
#
#
# if __name__ == "__main__":
#     write_append(r"C:\Users\Administrator\PycharmProjects\zhandian_jiekou\data\test_append.xls")


# #coding:utf-8
#
# import xlrd,os
# import requests
# import openpyxl
# from openpyxl.styles import Font
# # from xlutils.copy import copy
# from datetime import datetime
# from xlrd import xldate_as_tuple
# from config import readConfig
# from common.logger import Log
# from case.user_login import Login
#
#
#
# runmode = readConfig.runmode
#
# if runmode == 'test':
#     ip = readConfig.test_ip  # 获取配置文件中接口ip
#     i_port = readConfig.test_port  # 获取配置文件中接口port
# elif runmode == 'pro':
#     ip = readConfig.pro_ip  # 获取配置文件中接口ip
#     i_port = readConfig.pro_port  # 获取配置文件中接口port
# else:
#     raise ValueError("run_config.ini文件配置的运行模式错误")

# import openpyxl
#
#
# wb = openpyxl.load_workbook(r"C:\Users\Administrator\PycharmProjects\zhandian_jiekou\data\a1.xlsx")
# ws = wb.worksheets[0]
# ws.cell(row=1,column=3,value='aaaa')
# wb.save(r"C:\Users\Administrator\PycharmProjects\zhandian_jiekou\data\a1.xlsx")

# from datetime import datetime
# from time import sleep
# a = datetime.now()
# print(a)
# sleep(1)
# b = datetime.now()
# print(b)
# print((b-a).seconds)


# import hashlib
# import base64
#
# md5 = hashlib.md5()
#
#
# # a = "<request><waybills><waybill><receiver><receiverName>张三</receiverName><receiverMobile>13000000000</receiverMobile><receiverZip>431400</receiverZip><receiverProvince>甘肃省</receiverProvince><receiverCity>兰州市</receiverCity><receiverArea>新洲区</receiverArea><receiverDistrict>李集街道</receiverDistrict><receiverAddress>天水南路222号</receiverAddress></receiver><sender><shopName>天猫超市</shopName><senderName>天猫超市仓库</senderName><senderPhone>02781739210</senderPhone><senderZip>430208</senderZip><senderProvince>甘肃省</senderProvince><senderCity>兰州市</senderCity><senderArea>新洲区</senderArea><senderAddress>金口街旭光村菜鸟物流园3号库</senderAddress></sender><packageInfo><packageCode>test0926001</packageCode><isExpensive>false</isExpensive><weight>2302</weight><volume>7888000</volume><length>290</length><width>170</width><height>160</height><storeOutTime>2017-09-22 08:55:04</storeOutTime></packageInfo><carrier/><sortingInfo><routetype>1</routetype><storeCode>pressureTest</storeCode><deliveryCode>CHENGBANGPEISONG-0001</deliveryCode><deliveryWlbCode>NJCB-001</deliveryWlbCode><cpSimplyCode>C</cpSimplyCode><citySimplyCode>H1</citySimplyCode><routePath>{'nextRouteId':890,'nextRouteType':2,'targerRdcType':2,'targetRdcId':890}</routePath><siteId>4859</siteId><siteCode>1619095</siteCode><carrierCode>CBWL</carrierCode><sortingRequireTimes><requireSendTime>2017-09-24 23:59:00</requireSendTime></sortingRequireTimes><sortingService><expressSerType>108</expressSerType></sortingService></sortingInfo><order><lgOrderSource>WLB</lgOrderSource><storeOrderCode>ydhtest1341573</storeOrderCode><logisticsId>LP00079477100697</logisticsId><mailNo>ddhtest5454253</mailNo><customerCode>SB-ZFB</customerCode><deliveryType>1</deliveryType><distributionType>1</distributionType></order><deliveryNodeInfo><nodeCode>1619095</nodeCode><nodeName>晟邦湖北分拨中心</nodeName><deliveryStatus>MainWaybillAccess</deliveryStatus><firstOwnerRdcCode>1619095</firstOwnerRdcCode></deliveryNodeInfo><uniqueCode>MainWaybillAccesstest09260012017-09-22 09:13:11</uniqueCode><remark>zpb_chuyan_cb</remark></waybill></waybills></request>"
# # b = a.replace("\\>\\s+\\<", "><")+"alogalog"
# #
# #
# # md5.update(b.encode('utf-8'))
# # b = md5.digest()
# # print(u"16位md5加密结果：%s"% b)
# # print(u"16位md5加密结果再进行base64编码：%s" % base64.b64encode(b).decode('utf-8'))
#
# c = "1508465162269"+"kfzc@1234"
# md5.update(c.encode('utf-8'))
# d = md5.hexdigest()
# print(d)

# import string
# print(string.ascii_uppercase[0:7])
# for i in string.ascii_uppercase[0:7]:
#     print(i)

# sum = 1
# for i in range(0,101):
#     # sum = sum + i
#     sum += i
#
# print(sum)

# a = [str(i) for i in range(0,10) if i%2==0]
# print(''.join(a))

# print(i for i in range(0,10))



# a = [1,2]
#
# print("-".join(a))

# a = []
# for i in range(0,10):
#     if i%2 == 0:
#         a.append(str(i))
# print("".join(a))



# a = []
# for n in range(1,21):
#     if n <= 3:
#         for i in range(1,6):
#             a.append(i)
#         print(a)


    # for i in range(n,n+5):
    #     if i == n:
    #         a.append(str(i)+'*')
    #     else:
    #         a.append(i)
    # print(str(n)+' '+str(a))

# import random
#
# a = [1, 2, 3, 4, 5,6]
# random.shuffle(a)
#
# b = sorted(a,reverse=True)
# print(list(zip(a,b)))

# b = a[1::2]
# print(b)
#
# # print(b)
# sum = 0
# for i in b:
#     sum = (i+3) + sum
# print(sum)

# a = 'abcdef'
# print(''.join(sorted(a,reverse=True)))
# print(sorted(a,reverse=True))
# for i in sorted(a,reverse=True):
#     print(''.join(i))
# b = ['a','b','c']
# print(''.join(b))

# x = y = z = 1
# import re

# s = "abbacd"
#
# b = list(s)
# b1 = list(set(b))
# b1.sort(key=b.index)
# print(b1)
#
# c = {}
# for i in b1:
#     if s.count(i) == 1:
#         c[i] = s.count(i)
#         break
# for j in c.keys():
#     print(j)

# for i in b:
#     if a1.count(i) > 1:
#         print("字符：%s，重复次数：%s"%(i,a1.count(i)))

# def is_odd(n):
#     return n % 2 == 1
#
# newlist = filter(is_odd,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(list(newlist))


# s = "i am a student"
# print(''.join(list(s[::-1])))

# s1 = 'abcadfga'
# s2 = 'a'
# print(s1.replace(s2,''))

# L1 = [1,2,23,44,51]
#
# a = ''.join(map(str,L1))
# L2 = list(a)
# L2.sort()
# s = ''.join(L2)
# print(s)


# L1 = [1,2,3]
# L2 = [1]
# for i in L1:
#     if i not in L2:
#         print(i)


# list = ['a','b','c']
# list.insert(0,'1')
# print(list)


# import ast,json,re
#
# str_lists = '[{"status":"300"},{"message":"用户名或密码错误"}]'
# list_lists = ast.literal_eval(str_lists)   # string转换成list
#
# result = '{"message":"用户名或密码错误","status":"300"}'
#
#
# for list_list in list_lists:
#     a = json.dumps(list_list,separators=(',',':'),ensure_ascii=False).strip()
#     # 通过正则去除{}中间的值
#     new_a = (re.findall('{(.*)}',a))[0]
#     print("new_a的值:%s"%new_a)
#     if new_a in result:
#         print("成功")
#     else:
#         print("失败")


# import datetime,time
#
# start_time = datetime.datetime.now()
# print(start_time.strftime('%Y-%m-%d %H:%M:%S'))

# pa = 0
# fa = 0
# checkPoint_pass = 0
# checkPoint_fail = 0
# ac = [3,4]
# string_a = '123'
# for a in ac:
#     if str(a) in string_a:
#         checkPoint_pass += 1
#     else:
#         checkPoint_fail += 1
#
#
# if checkPoint_pass == len(ac):
#     print("pass")
#     pa = pa + 1
# else:
#     print("fail")
#     fa = fa + 1
#
# print(pa)
# print(fa)

#
# list = ['password', 'userId']
# new_res = ['${' + x + '}' for x in list]
# print(type(new_res))



# from common.mysql_pub import MysqlUtil
#
# ms = MysqlUtil()
#
#
# SQL = "update user set pass_word = '333333' where login_name = 'zrf1';"
#
# ms.mysql_execute(SQL)

# import ast
#
# a = "['预检分诊-报特殊/PD/实际响应/rows/id']"
# print(a)
# print(type(a))
# list_a = ast.literal_eval(a)
# print(list_a)
# print(type(list_a))


# a = ['预检分诊-报特殊/PD/实际响应/rows/id','1']
# for i in a:
#     i1 = i.split('/')
#     print(i1)


# a = ['abcd']
# # a1 = [str(i) for i in a]
# a2 = ''.join(a)
# print(a2)

# import ast
# from common.comm_function import *
#
#
# a = "['预检分诊-接诊/Preset Data/id','get_jiezhentime()','预检分诊-接诊/Preset Data1/id2']"
# list_rely_data=ast.literal_eval(a)  # string转换成list
# # print(list_rely_data)
# for j in list_rely_data:
#     if '/' in j:
#         rely_data = j.split('/')
#         print(rely_data)
#         relyexcel_name = rely_data[0] + ".xlsx"  # 依赖用例所在Excel名称
#         relycase_id = rely_data[1]  # 依赖用例编号
#         relycase_path = rely_data[2]  # 依赖数据的取值路径
#         print(relyexcel_name,relycase_id,relycase_path)
#     elif '(' and ')' in j:
#         aa = j
#         print(eval(aa))


    # rely_value = a.get_response_value(relyexcel_name, relycase_id, relycase_path)



# def text():
#     print("+++++++++++++++++++++++++++++++")
#
# if __name__ == '__main__':
#
#     name = "text"
#     s = eval(name)
#     s()





# import ast,json,re
#
#
# a = '[{"message":"查询成功"},{"status":200},{"total":1},{"rows":1}]'
# result = '{"total":1,"message":"查询成功","rows":[{"receivedepartment":"抢救02","dividtime":"2020-09-09 12:47:56","jiange2":"109","gender":"女","pid":"2009090003","jiange1":"-","cixu":"1","dividdepartment":"急诊耳鼻喉科","grade_color":"#ffe203","gradename":"2","cardnum":"4962285719298","registertime":null,"fullname":"钟建华","age":"21岁","receivetime":"2020-09-09 14:36:57"}],"status":200}'
#
# json_result = json.loads(result)
# count_rows = len(json_result['rows'])
#
#
# if a:
#     list_checkPoints = ast.literal_eval(a)  # string转换成list
#     print(list_checkPoints)
#
#     for checkPoint in list_checkPoints:
#         # 将dict转换成json，并且去除转换成json后冒号后的空格
#         json_checkPoint = json.dumps(checkPoint, separators=(',', ':'), ensure_ascii=False)
#         # print(json_checkPoint,type(json_checkPoint))
#         # 通过正则取{}中间的值
#         new_checkPoint = (re.findall('{(.*)}', json_checkPoint))[0]
#         print(new_checkPoint)
#         if 'rows' not in new_checkPoint:
#             if new_checkPoint in result:
#                 print("pass")
#             else:
#                 print("fail")
#
#         else:
#             if int(new_checkPoint.split(':')[-1]) == count_rows:
#                 print("pass")
#             else:
#                 print("fail")








# from common.mysql_pub import MysqlUtil
# mysql_db = MysqlUtil()
#
#
# a = "DELETE FROM trt_patient WHERE fullname = '郑连';"
# print(a,type(a))
# new_sqls = a.split('\n')
# for new_sql in new_sqls:
#     mysql_db.mysql_execute(new_sql)


# import os,os.path
#
# '''
# # 获取测试用例data所在的目录
# # '''
# d = os.path.dirname(__file__) #返回当前文件所在目录（common文件夹路径）
# parent_path = os.path.dirname(d) #返回common的父级目录
# data_path = os.path.join(parent_path,'data') #返回data所在目录
# data_path1 = os.listdir(data_path) #返回data目录下所有的文件
#
#
# def findAllFile(base):
#     for root, ds, fs in os.walk(base):
#         for f in fs:
#             if f.endswith('.xlsx'):
#                 fullname = os.path.join(root, f)
#                 yield fullname
#
# def main(base):
#     # base = data_path
#     excel_lists = []
#     for i in findAllFile(base):
#         excel_lists.append(i)
#     print(excel_lists)
#
#
# main(data_path)

# case_path = [os.path.join(data_path, i) for i in os.listdir(data_path) if i[-5:] == '.xlsx']



# import string
# #
# # a = "/triagedoctor/index/getIp"
# # print(a.find("triage"))



# import re
#
# """
#     判断输入的字符串中是否有关键字（做全字匹配，例如关键字为scanf则不匹配sscanf）
#         如果匹配到了，返回1，没有返回0
# """
# def isIncludeKeyWord(detailinfo,keyword_list):
#     for tmp_keyword in keyword_list:
#         #正则表达查询性能较差，先用find函数过滤，因为大部分字符串都不需要走正则查询
#         if  -1 != detailinfo.find(tmp_keyword):
#             #匹配^tmp_keyword$或^tmp_keyword(非字母数字下划线)(任意字符)
#             #或(任意字符)(非字母数字下划线)tmp_keyword$或(任意字符)(非字母数字下划线)tmp_keyword(非字母数字下划线)(任意字符)
#             pattern_str='(^'+tmp_keyword+'$)|(^'+tmp_keyword+'(\W+).*)|(.*(\W+)'+tmp_keyword+'$)|(.*(\W+)'+tmp_keyword+'(\W+).*)'
#             print(pattern_str)
#             m = re.match(r''+pattern_str+'', detailinfo)
#             if m:
#                 return 1
#     return 0
#
#
# a = isIncludeKeyWord("/triagedoctor/index/getIp",'/triagedoctor/index/getIp')
# print(a)


# a = "/triagedoctor/index/getIp"
# print(a.find('/triage/'))
# if a.find('/triagedoctor/'):
#     print(1)
# else:
#     print(0)


# import json
#
# a = '{"total":null,"message":"接诊成功","rows":{"saveResult":"1","id":"758649117474816000"},"status":200}'
# print(json.loads(a),type(json.loads(a)))
# print(json.loads(a)['rows'],type(json.loads(a)['rows']))


# import datetime
#
# t = datetime.datetime.now()
# dividtime = (t - datetime.timedelta(hours=0.1)).strftime("%Y-%m-%d %H:%M:%S")
# print(dividtime)






# import jsonpath,json
#
#
# a = '{"total":22,"message":"查询成功","rows":[{"receivedepartment":"688043158591766528","arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":"13525216300","id":"2009270025","others":"","receivetime":"2020-09-27 16:46:52","dividtime":"2020-09-07 13:34:00","consciousness":"模糊","diagnosis":null,"admission":"步行","dividenurse":"高博","dividdoctor":"","registertime":null,"bornday":"1991-06-01","patient_id":"2009270025","greenchannel":"N","grade":"1001","teshu":null,"status":"抢救已接诊","rctdiagnosis":null,"gender":"男","hisid":"","allergic_history1":null,"addbedsign":"0","cixu":"1","grade_color":"#f01620","bedarrivetime":"2020-09-27 16:46:52","allergic_history":"不详","bedleavetime":null,"finalgrade":"","bed_id":"688043158914727936","rowno":1,"bed_num":"1","process":"","address":"江苏省南京市江宁区双龙大道1088号明月新寓花园","anamnesis":"无","dividdepartment":"39","paddiagdesc":null,"doctor":null,"cardnum":"698515201409045288","anonymous":null,"fullname":"刘星","category":"1","autograde":"1001","age":"29岁","memberstel":"夏东海","changereason":"选择修改原因"},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"688043158931505152","rowno":2,"bed_num":"2","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769172434944000","rowno":3,"bed_num":"3","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769172434944001","rowno":4,"bed_num":"4","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769172434944002","rowno":5,"bed_num":"5","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769172497858560","rowno":6,"bed_num":"6","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769172825014272","rowno":7,"bed_num":"7","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769172892123136","rowno":8,"bed_num":"8","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"68976917289212 2000 3137","rowno":9,"bed_num":"9","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769172892123138","rowno":10,"bed_num":"10","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769172959232000","rowno":11,"bed_num":"11","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769173152169984","rowno":12,"bed_num":"12","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769173286387712","rowno":13,"bed_num":"13","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769173483520000","rowno":14,"bed_num":"14","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769173483520001","rowno":15,"bed_num":"15","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769173546434560","rowno":16,"bed_num":"16","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769173546434561","rowno":17,"bed_num":"17","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769173546434562 129a ","rowno":18,"bed_num":"18","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":null,"arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":null,"id":null,"others":null,"receivetime":null,"dividtime":null,"consciousness":null,"diagnosis":null,"admission":null,"dividenurse":null,"dividdoctor":null,"registertime":null,"bornday":null,"patient_id":null,"greenchannel":null,"grade":null,"teshu":null,"status":null,"rctdiagnosis":null,"gender":null,"hisid":null,"allergic_history1":null,"addbedsign":"0","cixu":null,"grade_color":null,"bedarrivetime":null,"allergic_history":null,"bedleavetime":null,"finalgrade":null,"bed_id":"689769173546434563","rowno":19,"bed_num":"19","process":"","address":null,"anamnesis":null,"dividdepartment":null,"paddiagdesc":null,"doctor":null,"cardnum":null,"anonymous":null,"fullname":null,"category":null,"autograde":null,"age":null,"memberstel":null,"changereason":null},{"receivedepartment":"590193845140979712","arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":null,"leavetime":null,"tel":"13948025966","id":"2009180001","others":"","receivetime":"2020-09-18 13:54:15","dividtime":"2020-09-18 08:02:52","consciousness":"谵妄","diagnosis":null,"admission":"步行","dividenurse":"护一","dividdoctor":"","registertime":null,"bornday":"1980-07-12","patient_id":"2009180001","greenchannel":"N","grade":"1001","teshu":null,"status":"抢救已接诊","rctdiagnosis":null,"gender":"女","hisid":"","allergic_history1":null,"addbedsign":"0","cixu":"1","grade_color":"#f01620","bedarrivetime":"2020-09-18 13:54:15","allergic_history":"头孢,红霉素,青霉素,阿奇霉素","bedleavetime":null,"finalgrade":"","bed_id":"689769173613543424","rowno":20,"bed_num":"20","process":"腹痛","address":"湖北省凯市房山尹路F座 ","anamnesis":"COPD,冠心病,高血压,哮喘","dividdepartment":"7","paddiagdesc":null,"doctor":null,"cardnum":"3132101121920","anonymous":null,"fullname":"韦军","category":"7","autograde":"1001","age":"40岁","memberstel":"张博","changereason":""},{"receivedepartment":"590193845140979712","arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":"222","leavetime":null,"tel":"15319486279","id":"2009080049","others":"","receivetime":"2020-09-15 16:06:38","dividtime":"2020-09-08 14:37:26","consciousness":"谵妄","diagnosis":null,"admission":"步行","dividenurse":"护一","dividdoctor":"","registertime":null,"bornday":"1980-11-02","patient_id":"2009080049","greenchannel":"N","grade":"1001","teshu":null,"status":"抢救已接诊","rctdiagnosis":"","gender":"男","hisid":"2004140006","allergic_history1":"头孢,红霉素,青霉素,阿奇霉素","addbedsign":"1","cixu":"1","grade_color":"#f01620","bedarrivetime":"2020-09-15 16:06:38","allergic_history":"头孢,红霉素,青霉素,阿奇霉素","bedleavetime":null,"finalgrade":"","bed_id":"743795793982390272","rowno":21,"bed_num":"+1","process":"急性心肌梗死","address":"河北省瑜市上街王路Q座 ","anamnesis":"COPD,冠心病,高血压,哮喘","dividdepartment":"","paddiagdesc":null,"doctor":"111","cardnum":"4369199657409","anonymous":null,"fullname":"陆玉英","category":"7","autograde":"1001","age":"39岁","memberstel":"董梅","changereason":""},{"receivedepartment":"590193845140979712","arrivetime":null,"depart_id":"688043158591766528","resdoctor3":null,"type":null,"resdoctor2":"","leavetime":null,"tel":"18567826840","id":"2009210004","others":"","receivetime":"2020-09-22 18:37:13","dividtime":"2020-09-21 08:34:51","consciousness":"谵妄","diagnosis":null,"admission":"平车","dividenurse":"护一","dividdoctor":"","registertime":null,"bornday":"1987-11-24","patient_id":"2009210004","greenchannel":"N","grade":"1001","teshu":null,"status":"抢救已接诊","rctdiagnosis":"","gender":"女","hisid":"","allergic_history1":"头孢,红霉素,青霉素,阿奇霉素","addbedsign":"1","cixu":"1","grade_color":"#f01620","bedarrivetime":"2020-09-22 18:37:13","allergic_history":"头孢,红霉素,青霉素,阿奇霉素","bedleavetime":null,"finalgrade":"","bed_id":"751444429679624192","rowno":22,"bed_num":"+2","process":"多发伤","address":"广东省香港市清城覃路W座 ","anamnesis":"COPD,冠心病,高血压,哮喘","dividdepartment":"4","paddiagdesc":null,"doctor":"黄欢欢","cardnum":"3474127241993","anonymous":null,"fullname":"罗玉英","category":"7","autograde":"1001","age":"32岁","memberstel":"周桂珍","changereason":""}],"status":200}'
#
# a1 = json.loads(a)
# print(a1)
# print(jsonpath.jsonpath(a1,'$..bed_id'))
# print(type(jsonpath.jsonpath(a1,'$..bed_id')))
# a2 = jsonpath.jsonpath(a1,'$..bed_id')[0]
# print(a2)




# a = 'bed_id[0]'
# import re
#
# a1 = re.search(r"\[(.*?)]",a).group()
# print(a1)

import time

excel_name = time.strftime('%Y_%m_%d_%H_%M_%S')
print(excel_name)


