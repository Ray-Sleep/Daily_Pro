# -*- coding: UTF-8 -*-
"""
@Project : Ray_Pro
@File    : auto_wx_talk
@IDE     : PyCharm
@Author  : 李睡睡
@Date    : 2023/10/8 5:31
@Scripts :
@Documentation:
@Function: 
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""

import pandas as pd
import numpy as np

from uiautomation import WindowControl

# 绑定微信主窗口

wx = WindowControl(
    Name="微信",
)
print(wx)

# 切换到微信窗口
wx.SwitchToThisWindow()

# 寻找会话控件绑定
hw = wx.ListControl(Name='会话')
print('寻找会话控件绑定', hw)

# # 通过pd读取数据
# df = pd.read_csv('./data/回复数据.csv',encoding='gb18030')

# 死循环接受信息
while True:
    # 查找未读消息(查找深度，前四个对话框）
    we = hw.TextControl(searchDepth=4)

    # 当没有未读消息时，死循环维持
    while not we.Exists(0):
        pass

    # 存在未读消息，获取未读消息的文本
    print('查找未读消息',we)
    if we.Name:
        # 点击未读消息
        we.Click(simulateMove=False)

        # 读取最后一条消息
        last_msg = wx.ListControl(Name='消息').GetChildren()[-1].Name
        print('最后一条消息', last_msg)

        # 接入ai，得到最后一条消息的ai回复

        # 将数据输入
        wx.SendKeys(text='AI回复',waitTime=0)
        # 发送文本
        wx.SendKeys('{Enter}',waitTime=0)

        # 通过消息匹配检索会话栏的联系人
        wx.TextControl()