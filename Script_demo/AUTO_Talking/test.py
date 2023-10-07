# -*- coding: UTF-8 -*-
"""
@Project : Ray_Pro 
@File    : test.py
@IDE     : PyCharm 
@Author  : 李睡睡
@Date    : 2023/2/10 0:34 
@Scripts :
@Documentation:
@Function:
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""
#-*- coding:utf-8 -*-
import requests
import itchat
import re

KEY = 'b3285425a60444e1b3d42d90c0e8c603'  #可以到图灵机器人官网申请一个apikey，现在要收费，一个月的费用不高
Target_user = "filehander"
flag = 1

def is_right_id(targe_char, string):         # 在字符串string中，查找单个字符targe_char
    a = re.search(targe_char, string)        # 采用正则表达式查找，如果找到返回True，否则返回False
    if a:
        return True
    else:
        return False

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()   # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')                          # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    except:                                           # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
        return                                        # 将会返回一个None


@itchat.msg_register(['Text','Map', 'Card', 'Note', 'Sharing', 'Picture', 'Video'])
def tuling_reply(msg):
    global Target_user, flag
    if flag == 1:
        itchat.send("收到的消息：" + msg['Text'] + '\n' + "消息来自：" + msg["FromUserName"], toUserName='filehelper')
    if msg["FromUserName"] == Target_user or msg["ToUserName"] == "filehelper":
        if is_right_id('@', msg['Content']):
            Target_user = msg['Content']
            flag = 0
            itchat.send("更新聊天小伙伴成功", toUserName='filehelper')
        if msg["ToUserName"] == "filehelper" and msg['Content'] == "更新聊天小伙伴" or msg['Content'] == "更新":
            flag = 1
            itchat.send("更新设置已开启，等待设置新的聊天小伙伴", toUserName='filehelper')
        if msg["FromUserName"] == Target_user:
            reply = get_response(msg['Text'])
            itchat.send(reply, toUserName=Target_user)

itchat.auto_login(hotReload=True)
itchat.run()

