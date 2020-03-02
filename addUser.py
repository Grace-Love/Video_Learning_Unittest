#coding：utf-8
"""
1、获取token值，账号、密码登录后，服务器会返回一个token值
2、新增用户接口
"""
import requests
import json
from getToken import *
from getUrl import getUrl
from useExcelToReadCase import getPara
import os
from oper_cfg import readCfg
import HTMLTestRunner

# def addUser(userName,password):
#     header = {'Content-Type':'application/json','X-AUTH-TOKEN':getToken(userName,password)}
#     userData =getPara().encode('utf-8') #若excel单元格中有中文，需要添加：encode('utf-8')
#     res = requests.post(url=getUrl(),data = userData,headers = header) #构造post请求
#     print(res.text)
#
#     assResult = json.loads(res.text)['message']
#     #添加断言：
#     if assResult == '成功':
#         #print('adduser -----> pass')
#         excel_res = 'pass'
#     else:
#         #print('adduser ----> fail')
#         excel_res = 'fail'
#
#     return excel_res

here_path = os.path.dirname(os.path.abspath(__file__))

config = here_path+'/addUserConfig.cfg'
read_config = readCfg(config) #读取配置文件
report_path = read_config.get("path","report_path") #从配置文件中，获取section和其对应的值，即就是：获取到report的路径


fp = open(report_path,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = '测试报告',description = '执行添加用户的测试用例执行情况')




# if __name__ == '__main__':
#     a = addUser('J201903070064','362387359')
#     print(a)



# #请求消息头
# print(res.request.headers)
# #打印消息体
# print(res.request.body)
