# -*- coding:utf-8 -*-  

'''
Created on 2017年4月6日

@author: Jin
'''
import xlrd
import TestRequest
from TestRequest import TestPostRequest
hhlist =TestRequest.hlist
Testdata = xlrd.open_workbook('C:/Jin/workpase/ApiTest/src/TestData.xls')#读取测试数据
table = Testdata.sheets()[0]#选择excle表中的sheet
hurl = table.cell(7,1).value#从测试数据中读取url
htoken = table.cell(8,1).value
hcontent_type = table.cell(6,1).value
def TestCass01():
    for i in range(3,9):
        table = Testdata.sheets()[1]#选择excle表中的sheet  
        hdata = {
                "username": table.cell(i,0).value,
                "realName": table.cell(i,1).value,
                "password": table.cell(i,3).value,
                "remark": table.cell(i,4).value,
                "status":table.cell(i,2).value
                }             
        headers = {
            'content-type': hcontent_type,
            'token': htoken
            }
        htestcassid = "1-"+str(i+1)
        htestcassname = "添加管理员"
        htesthope = table.cell(i,5).value
        TestPostRequest(hurl+'/admin/add', hdata, headers, htestcassid, htestcassname,htesthope)
        
        
# TestCass01()
