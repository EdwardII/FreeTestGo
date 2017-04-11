# -*- coding:utf-8 -*-  

'''
Created on 2017年4月6日

@author: Jin
'''
import json
import requests

hlist = []#添加一个数组，用来装测试结果
def TestPostRequest(hurl,hdata,headers,htestcassid,htestcassname,htesthope):
    hr = requests.post(hurl,data=json.dumps(hdata), headers=headers)
    hjson = json.loads(hr.text)#获取并处理返回的json数据
    herror ="error"
    if herror in hjson: 
        hstatus = str(hjson["status"])
        if hstatus == htesthope:
            hhhdata = {"t_id": htestcassid,
                          "t_name": htestcassname,
                          "t_method": "post", 
                          "t_url": hurl, 
                          "t_param": "测试数据:"+str(hdata),
                          "t_hope": "code:"+str(htesthope), 
                          "t_actual": "Code:"+hstatus+";msg:"+str(hjson['message']), 
                          "t_result": "通过"} 
            hlist.append(hhhdata)#把测试结果添加到数组里面
            print(htestcassname)
            print("测试通过")
            print("返回的消息是："+str(hjson['message']))  
        else:          
            hhhdata = {"t_id": htestcassid,
                              "t_name": htestcassname,
                              "t_method": "post", 
                              "t_url": hurl, 
                              "t_param": "测试数据:"+str(hdata),
                              "t_hope": "Code:"+str(htesthope), 
                              "t_actual": str(hjson), 
                              "t_result": "失败"} 
            hlist.append(hhhdata)
            print(htestcassname)
            print('测试不通过')
            print("返回的消息为："+str(hjson))
    else:
        hcode = str(hjson['code'])     
        if hcode == htesthope:  
            hhhdata = {"t_id": htestcassid,
                          "t_name": htestcassname,
                          "t_method": "post", 
                          "t_url": hurl, 
                          "t_param": "测试数据:"+str(hdata),
                          "t_hope": "Code:"+str(htesthope), 
                          "t_actual": "Code:"+hcode+";msg:"+str(hjson['msg']), 
                          "t_result": "通过"} 
            hlist.append(hhhdata)#把测试结果添加到数组里面
            print(htestcassname)
            print("测试通过")
            print("返回的消息是："+str(hjson['msg']))              
        else:
            hhhdata = {"t_id": htestcassid,
                          "t_name": htestcassname,
                          "t_method": "post", 
                          "t_url": hurl, 
                          "t_param": "测试数据:"+str(hdata),
                          "t_hope": "Code:"+str(htesthope), 
                          "t_actual": "Code:"+hcode+";msg:"+str(hjson['msg']), 
                          "t_result": "失败"} 
            hlist.append(hhhdata)
            print(htestcassname)
            print('测试不通过')
            print("返回的消息是："+str(hjson['msg']))

def TestGetRequest(hurl,hdata,headers,htestcassid,htestcassname,htesthope):
    hr = requests.get(hurl,params=hdata, headers=headers)
    hjson = json.loads(hr.text)#获取并处理返回的json数据
    herror ="error"
    if herror in hjson:       
        hstatus = str(hjson["status"])
        if hstatus == htesthope:
            hhhdata = {"t_id": htestcassid,
                          "t_name": htestcassname,
                          "t_method": "get", 
                          "t_url": hurl, 
                          "t_param": "测试数据:"+str(hdata),
                          "t_hope": "code:"+str(htesthope), 
                          "t_actual": "Code:"+hstatus+";msg:"+str(hjson['errors']), 
                          "t_result": "通过"} 
            hlist.append(hhhdata)#把测试结果添加到数组里面
            print(htestcassname)
            print("测试通过")
            print("返回的消息是："+str(hjson['errors']))  
        else:            
            hhhdata = {"t_id": htestcassid,
                              "t_name": htestcassname,
                              "t_method": "get", 
                              "t_url": hurl, 
                              "t_param": "测试数据:"+str(hdata),
                              "t_hope": "code:"+str(htesthope), 
                              "t_actual": str(hjson), 
                              "t_result": "失败"} 
            hlist.append(hhhdata)
            print(htestcassname)
            print('测试不通过')
            print("返回的消息为："+str(hjson))
    else:
        hcode = str(hjson['code'])     
        if hcode == htesthope:  
            hhhdata = {"t_id": htestcassid,
                          "t_name": htestcassname,
                          "t_method": "get", 
                          "t_url": hurl, 
                          "t_param": "测试数据:"+str(hdata),
                          "t_hope": "code:"+str(htesthope), 
                          "t_actual": "Code:"+hcode+";msg:"+str(hjson['msg']), 
                          "t_result": "通过"} 
            hlist.append(hhhdata)#把测试结果添加到数组里面
            print(htestcassname)
            print("测试通过")
            print("返回的消息是："+str(hjson['msg']))            
        else:
            hhhdata = {"t_id": htestcassid,
                          "t_name": htestcassname,
                          "t_method": "get", 
                          "t_url": hurl, 
                          "t_param": "测试数据:"+str(hdata),
                          "t_hope": "code:"+str(htesthope), 
                          "t_actual": "Code:"+hcode+";msg:"+str(hjson['msg']), 
                          "t_result": "失败"} 
            hlist.append(hhhdata)
            print(htestcassname)
            print('测试不通过')
            print("返回的消息是："+str(hjson['msg']))
            

