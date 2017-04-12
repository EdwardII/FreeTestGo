# -*- coding:utf-8 -*-  

'''
Created on 2017年4月7日

@author: Jin
'''
import xlrd
from PublicTools.TestRequest import TestPostRequest
from PublicTools.TestRequest import TestGetRequest
Testdata = xlrd.open_workbook('../TestData/TestData.xls')#读取测试数据
table = Testdata.sheets()[0]#选择excle表中的sheet
hurl = table.cell(7,1).value#从测试数据中读取url
htoken = table.cell(8,1).value
hcontent_type = table.cell(6,1).value
def test_1add_permission():
    for i in range(3,6):
        table = Testdata.sheets()[2]#选择excle表中的sheet  
        hdata = {
                "pid": table.cell(i,0).value,
                "name": table.cell(i,1).value,
                "authorityType": table.cell(i,2).value,
                "authority": table.cell(i,3).value,
                "remark":table.cell(i,4).value,
                "isLog": table.cell(i,5).value,
                "logLevel":table.cell(i,6).value                
                }             
        headers = {
            'content-type': hcontent_type,
            'token': htoken
            }
        htestcassid = "2-1-"+str(i+1)
        htestcassname = "新增权限"
        htesthope = table.cell(i,7).value
        TestPostRequest(hurl+'/adminPermission/add', hdata, headers, htestcassid, htestcassname,htesthope)

def test_2del_permission():
    for i in range(13,16):
        table = Testdata.sheets()[2]#选择excle表中的sheet  
        hid = table.cell(i,0).value    
        hdata = None             
        headers = {
            'content-type': hcontent_type,
            'token': htoken
            }
        htestcassid = "2-2-"+str(i+1)
        htestcassname = "删除权限"
        htesthope = table.cell(i,1).value
        TestPostRequest(hurl+'/adminPermission/delete/'+hid, hdata, headers, htestcassid, htestcassname,htesthope)

def test_3find_permission():
    for i in range(21,22):
        table = Testdata.sheets()[2]#选择excle表中的sheet           
        hdata = None           
        headers = {
            'content-type': hcontent_type,
            'token': htoken
            }
        htestcassid = "2-3-"+str(i+1)
        htestcassname = "查询所有权限列表"
        htesthope = table.cell(i,0).value
        TestGetRequest(hurl+"/adminPermission/findAll", hdata, headers, htestcassid, htestcassname, htesthope)
        
def test_4exists_permission():
    for i in range(31,34):
        table = Testdata.sheets()[2]#选择excle表中的sheet           
        hdata = {
            "name": table.cell(i,0).value
            }           
        headers = {
            'content-type': hcontent_type,
            'token': htoken
            }
        htestcassid = "2-4-"+str(i+1)
        htestcassname = "系统中是否有同名的权限"
        htesthope = table.cell(i,1).value
        TestGetRequest(hurl+"/adminPermission/isHomonymic", hdata, headers, htestcassid, htestcassname, htesthope)
    
# test_4exists_permission()        
