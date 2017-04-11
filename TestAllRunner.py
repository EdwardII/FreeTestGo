# -*- coding:utf-8 -*-  

'''
Created on 2017年3月31日

@author: Jin
'''

from PublicTools.GetToken import test_get_token
import threading    #导入多线程库
import TestAllCass

test_get_token()#数据初始化，获取token
def hthreads():
    threads = []    #创建线程数组
    #定义线程
    threads.append(threading.Thread(target=TestAllCass.Test_01AdminCass))      #添加线程到数组
    #定义线程
    threads.append(threading.Thread(target=TestAllCass.Test_02PermissionCass()))      #添加线程到数组    
    #定义线程
    threads.append(threading.Thread(target=TestAllCass.Test_03AdminroleCass()))      #添加线程到数组    
    
    for h in threads:   #读取数组里的所有线程，并同时执行
        h.start()       #开始线程活动            
        h.join()    #把主线程挂起，等待上面的线程跑完了再运行  
         
    AllTestReportData = TestAllCass.hhhlist
    return AllTestReportData
hthreads()
