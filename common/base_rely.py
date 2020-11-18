#coding:utf-8

import xlrd,os,json,jsonpath,re


'''
获取测试用例data所在的目录
'''
d = os.path.dirname(__file__) #返回当前文件所在目录（common文件夹路径）
parent_path = os.path.dirname(d) #返回common的父级目录
data_path = os.path.join(parent_path,'data') #返回data所在目录
data_path1 = os.listdir(data_path) #返回data目录下所有的文件


def get_response_value(excelname,caseid='',resp_path=''):
    book = xlrd.open_workbook(os.path.join(data_path, excelname))
    sheet = book.sheet_by_index(1)  # 通过索引，获取相应的列表，这里表示获取excel的第二个列表（测试用例）

    # 获取列表的有效列数
    ncols = sheet.ncols

    # 返回第一列（用例编号）所有单元格的数据
    case_ids = sheet.col_values(0,start_rowx=1)

    # 找到caseid所在的行
    r = 1
    # result = [r+1 for i in case_ids if i == caseid]
    # print(result)

    for i in case_ids:
        if str(i) == caseid:
            break
        else:
            r += 1

    # 获取caseid所在行的响应数据值
    resp = sheet.cell_value(r,ncols-4)
    json_resp = json.loads(resp)
    # 提取对应的字段值
    if re.search(r"\[(.*?)]",resp_path):
        # 提取[]的内容，例如bed_id[0]，提取[0]
        path_number = re.search(r"\[(.*?)]",resp_path).group()
        # 提取[]的内容，例如bed_id[0]，提取0
        path_number2 = re.search(r"\[(.*?)]", resp_path).group(1)
        # 去除resp_path中的[]，例如bed_id[0]，去除后变成bed_id
        newresp_path = resp_path.replace(str(path_number),'')
        # 用jsonpath提取bed_id对应下标的值
        resp_value = jsonpath.jsonpath(json_resp,'$..%s'%newresp_path)[int(path_number2)]
    else:
        resp_value = jsonpath.jsonpath(json_resp, '$..%s' % resp_path)
    return ''.join(resp_value)



# get_response_value('预检分诊-报特殊.xlsx',caseid='Preset Data',resp_path='id')