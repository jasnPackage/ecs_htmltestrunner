#coding:utf-8
import xlrd,openpyxl,os
from openpyxl.styles import Font,Alignment


book = xlrd.open_workbook('C:\\Users\\Administrator\\PycharmProjects\\ecs_ddt_htmltestrunner\\data\\预检分诊站\\预检分诊-用户登录.xlsx')
'''
使用openpyxl操作excel，openpyxl支持excel2007以上版本
'''
wb = openpyxl.load_workbook('C:\\Users\\Administrator\\PycharmProjects\\ecs_ddt_htmltestrunner\\data\\预检分诊站\\预检分诊-用户登录.xlsx')
ws = wb.worksheets[1]
font_green = Font(color="37b400")
font_red = Font(color="ff0000")

'''
获取excel文件中测试用例信息，将A-K列转换成字典存储
'''
sheet = book.sheet_by_index(1)  # 通过索引，获取相应的列表，这里表示获取excel的第二个列表
nrows = sheet.nrows  # 获取所有行数
print(nrows)
ncols = sheet.ncols  # 获取所有列数
print(ncols)
key = sheet.row_values(0)

align = Alignment(horizontal='left', vertical='center', wrap_text=True)  # 纯色填充
ws.cell(row=2, column=ncols - 3, value='你好').alignment = align

wb.save('C:\\Users\\Administrator\\PycharmProjects\\ecs_ddt_htmltestrunner\\data\\预检分诊站\\预检分诊-用户登录.xlsx')
