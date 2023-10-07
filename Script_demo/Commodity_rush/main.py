# -*- coding: UTF-8 -*-
"""
@Project : Daily_Pro
@File    : main
@IDE     : PyCharm
@Author  : 李睡睡
@Date    : 2023/4/27 1:15
@Scripts :
@Documentation:
@Function: 抢购商品
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""

import datetime
now = datetime.datetime.now().strftime('-%Y-%m-%d %H:%M:%S.%f')
import time
from selenium import webdriver
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

"""提前把商品添加到购物车
1.打开游览器
2.进入电商平台
3.输入官网网址
4.进入购物车
"""