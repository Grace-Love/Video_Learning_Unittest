#coding：utf-8

import requests
import json
def getToken(userName,password):

    token_url = "http://47.96.181.17:9090/rest/toController"
    header = {"Content-Type":"application/json"}
    tokenData = {"userName":userName,"password":password}

    res = requests.post(url=token_url,data = json.dumps(tokenData),headers = header)
    #print(res.text)  #字符串类型  json是数据格式
    res_dict = json.loads(res.text)
    return res_dict['token']

if __name__ == '__main__':
    userName = 'J201903070064'
    password = '362387359'
    token = getToken(userName,password)
    print(token)



"""
1、字典：tokenData = {"userName":"J201903070064","password":"362387359"}
2、json tokenData = "{"userName":"J201903070064","password":"362387359"}"
"""
