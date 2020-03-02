#coding:utf-8
#time:2020-02-28 21:58

# """1、读取excel中的测试用例
#  1)、用到的库 xlrd：用来读取excel <pip install xlrd>
#  2)、需要确定要读取的excel是否存在：
#  excelDir = 'excel路径+名称'
#  路径注意：写路径时，给前面加 r ，例如：path = r'D:\xxx.xlsx'
#  3)、打开excel：
#     excel = xlrd.open_workbook(path)
#  4)、若一个excel中有多个子表，查看所有的子表名：
#    print(path.sheet_names()),返回的是列表类型
#   拿出想要的sheet的名字：
#    worksheet = path.sheet_names()[1]
#    或者
#    worksheet = path.sheet_by_name('输入你想要操作的sheet的表名')
#  5)、读取一行的内容<下标读取，返回列表>
#   rows = worksheet.row_values(1) ？？？
#   print(rows)
#  6)、读取一列的内容<下标读取，返回列表>
#   clos = wordsheet.cell_values(1，6)  读取第一行第六列
#
# 2、构建接口对应请求
# 3、测试结果写入excel
#  1)、xlutils模块：from xlutils.copy import copy #复制函数
#   a、首先打开excel workBook = xlrd.open_workboot(要打开的excel文件)
#   b、复制：workbookNew = copy(workbook)
#   """
import requests
import xlrd
import os
from getUrl import getUrl

def getPara():

    here_path = os.path.dirname(os.path.abspath(__file__))
    excel_path = here_path + '/unittest_readExcel.xls'

    excel_workbook = xlrd.open_workbook(excel_path) #打开要操作的excel
    #print(excel_workbook.sheet_names()) #打印当前excel中的所有sheet的名字,类型为list
    excel_workbook_sheet = excel_workbook.sheet_by_name('要测试的_Sheet2') #拿出想要操作的sheet的名字：

    nrows = excel_workbook_sheet.nrows #获取行号
    ncols = excel_workbook_sheet.ncols #获取列号
    # print(nrows)
    # print(ncols)

    for i in range(1,nrows):
        alldata = excel_workbook_sheet.cell_value(i,6)  #循环取出第i行，第6列的数据
        print(alldata)


if __name__ == '__main__':
    getPara()




