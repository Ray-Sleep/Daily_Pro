# -*- coding: UTF-8 -*-
"""
@Project : Ray_Pro 
@File    : auto_web.py
@IDE     : PyCharm 
@Author  : 李睡睡
@Date    : 2023/1/30 1:52 
@Scripts :
@Documentation:
@Function:
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""
import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import traceback
from selenium.webdriver.common.keys import Keys

def auto_web():
    # 此为本作者浏览器本地位置
    Edgedriver = 'C:\Program Files (x86)\Microsoft\Edge\Application'

    os.environ["webdriver.ie.driver"] = Edgedriver

    driver = webdriver.Chrome()  # 选择Chrome浏览器

    driver.get('https://www.bilibili.com/')  # 输入自己要打开的网站
    driver.maximize_window()  # 最大化Edge浏览器














