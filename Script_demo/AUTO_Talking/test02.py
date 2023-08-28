# -*- coding: UTF-8 -*-
"""
@Project : Ray_Pro 
@File    : test02.py
@IDE     : PyCharm 
@Author  : 李睡睡
@Date    : 2023/2/10 0:37 
@Scripts :
@Documentation:
@Function:
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""
# coding:utf-8
import requests
from wxpy import *
import itchat
import requests
import json

def get_response(_info):
    print(_info)                                       # 从好友发过来的消息
    api_url = 'http://www.tuling123.com/openapi/api'   # 图灵机器人网址
    data = {
        'key': 'b3285425a60444e1b3d42d90c0e8c603',
        'info': _info,                                 # 这是我们从好友接收到的消息 然后转发给图灵机器人
        'userid': 'wechat-robot',                      # 这里你想改什么都可以
    }
    r = requests.post(api_url, data=data).json()       # 把data数据发
    print(r.get('text'))                               # 机器人回复给好友的消息
    return r

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return get_response(msg["Text"])["text"]           # 将信息转发给好友


if __name__ == '__main__':
    itchat.auto_login(True)
    itchat.run()