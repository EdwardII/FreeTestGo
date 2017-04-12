# -*- coding:utf-8 -*-  

'''
Created on 2017年3月29日

@author: Jin

'''
#导入测试用例
import time
import TestCass.TestCassAdmin_01
import TestCass.TestCassPermission_02
import TestCass.TestCassAdminrole_03


def Test_01AdminCass():
    print('开始测试')
    now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
    print(now)
    TestCass.TestCassAdmin_01.test_1add_admin()#添加需要测试测试用例
    TestCass.TestCassAdmin_01.test_2del_admin()
    TestCass.TestCassAdmin_01.test_3edit_admin()
    TestCass.TestCassAdmin_01.test_4list_admin()
    TestCass.TestCassAdmin_01.test_5exists_admin()
    TestCass.TestCassAdmin_01.test_6find_admin()
    print('结束测试')

    
def Test_02PermissionCass():
    print("开始测试")
    now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
    print(now)
    TestCass.TestCassPermission_02.test_1add_permission()
    TestCass.TestCassPermission_02.test_2del_permission()
    TestCass.TestCassPermission_02.test_3find_permission()
    TestCass.TestCassPermission_02.test_4exists_permission()
    print('结束测试')

def Test_03AdminroleCass():
    print("开始测试")
    now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
    print(now)
    TestCass.TestCassAdminrole_03.test_1relate_permissions()
    TestCass.TestCassAdminrole_03.test_2get_permissions()
    print("结束测试")  



 
# Test_01AdminCass()
# Test_02PermissionCass()
# Test_03AdminroleCass()
