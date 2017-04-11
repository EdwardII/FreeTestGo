# -*- coding:utf-8 -*-  

'''
Created on 2017年4月6日

@author: Jin
'''
import xlrd
import PublicTools.TestRequest
from PublicTools.TestRequest import TestPostRequest
from PublicTools.TestRequest import TestGetRequest
hhlist =PublicTools.TestRequest.hlist
Testdata = xlrd.open_workbook('C:/Jin/workpase/ApiTest/src/AdminTest/TestData/TestData.xls')#读取测试数据
table = Testdata.sheets()[0]#选择excle表中的sheet
hurl = table.cell(7,1).value#从测试数据中读取url
htoken = table.cell(8,1).value
hcontent_type = table.cell(6,1).value
def test_1add_admin():
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
        htestcassid = "1-1-"+str(i+1)
        htestcassname = "添加管理员"
        htesthope = table.cell(i,5).value
        TestPostRequest(hurl+'/admin/add', hdata, headers, htestcassid, htestcassname,htesthope)
        
def test_2del_admin():
    for i in range(13,16):
        table = Testdata.sheets()[1]#选择excle表中的sheet  
        hid = table.cell(i,0).value    
        hdata = None             
        headers = {
            'content-type': hcontent_type,
            'token': htoken
            }
        htestcassid = "1-2-"+str(i+1)
        htestcassname = "删除管理员"
        htesthope = table.cell(i,1).value
        TestPostRequest(hurl+'/admin/delete?id='+hid, hdata, headers, htestcassid, htestcassname,htesthope)       

def test_3edit_admin():
    for i in range(21,25):
        table = Testdata.sheets()[1]#选择excle表中的sheet  
         
        hdata = {
                "id": table.cell(i,0).value,
                "realName": table.cell(i,1).value,
                "adminType": table.cell(i,2).value,
                "remark": table.cell(i,3).value,
                "status":table.cell(i,4).value            
            }           
        headers = {
            'content-type': hcontent_type,
            'token': htoken
            }
        htestcassid = "1-3-"+str(i+1)
        htestcassname = "修改管理员"
        htesthope = table.cell(i,5).value
        TestPostRequest(hurl+'/admin/edit', hdata, headers, htestcassid, htestcassname,htesthope)       

def test_4list_admin():
    for i in range(31,35):
        table = Testdata.sheets()[1]#选择excle表中的sheet  
         
        hdata = {
            "status":table.cell(i,0).value,
            "username":table.cell(i,1).value         
            }           
        headers = {
            'content-type': hcontent_type,
            'token': htoken
            }
        htestcassid = "1-4-"+str(i+1)
        htestcassname = "返回管理员列表"
        htesthope = table.cell(i,2).value
        TestGetRequest(hurl+"/admin/getByStatusAndUsername", hdata, headers, htestcassid, htestcassname, htesthope)

def test_5exists_admin():  
    for i in range(40,42):
        table = Testdata.sheets()[1]#选择excle表中的sheet  
         
        hdata = {
            "username":table.cell(i,0).value         
            }           
        headers = {
            'content-type': hcontent_type,
            'token': htoken
            }
        htestcassid = "1-5-"+str(i+1)
        htestcassname = "判断管理员姓名是否已存在"
        htesthope = table.cell(i,1).value
        TestGetRequest(hurl+"/admin/existsByUserName", hdata, headers, htestcassid, htestcassname, htesthope)  
def test_6find_admin():
    for i in range(48,52):
        table = Testdata.sheets()[1]#选择excle表中的sheet  
         
        hdata = {
                "pageNo": table.cell(i,0).value,
                "pageSize": table.cell(i,1).value,   
            }           
        headers = {
            'content-type': hcontent_type,
            'token': htoken
            }
        htestcassid = "1-6-"+str(i+1)
        htestcassname = "查询管理员分页列表"
        htesthope = table.cell(i,2).value
        TestPostRequest(hurl+'/admin/findByCondition', hdata, headers, htestcassid, htestcassname,htesthope)   
        
# test_1add_admin()
# test_2dle_admin()
# test_3edit_admin()
# test_4list_admin()
# test_5exists_admin()
# test_6find_admin()

