# -*- coding:utf-8 -*-  

'''
Created on 2017年4月8日

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
def test_1relate_permissions():
    for i in range(3,4):
        table = Testdata.sheets()[3]#选择excle表中的sheet     
        hdata = {
            "id": table.cell(i,0).value, 
            "adminPermissionIdList": table.cell(i,1).value
            }         
        headers = {
            'content-type': hcontent_type,
            'token': htoken
            }
        htestcassid = "3-1-"+str(i+1)
        htestcassname = "管理员关联权限"
        htesthope = table.cell(i,2).value
        TestPostRequest(hurl+'/admin/relatePermissions', hdata, headers, htestcassid, htestcassname,htesthope)
        
def test_2get_permissions():
    for i in range(13,14):
        table = Testdata.sheets()[3]#选择excle表中的sheet           
        hdata = {
            'id' : table.cell(i,0).value
            }           
        headers = {
            'content-type': hcontent_type,
            'token': htoken
            }
        htestcassid = "3-2-"+str(i+1)
        htestcassname = "返回指定管理员Id的所有权限"
        htesthope = table.cell(i,1).value
        TestGetRequest(hurl+"/admin/getPermissions", hdata, headers, htestcassid, htestcassname, htesthope)
        
# test_1relate_permissions()
# test_2get_permissions()
