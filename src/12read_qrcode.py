# -*- coding: UTF-8 -*-
"""
@Project :Daily_Pro 
@File    :12read_qrcode.py
@Author  :李睡睡 主人
@Date    :2022/9/24 21:28 
@Scripts :pyzbar 、
@Documentation:https://pypi.org/project/pyzbar/
@Function:识别二维码、条形码
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""
from pyzbar.pyzbar import decode
from PIL import Image
out = decode(Image.open("../out/02pro.png"))
print(out)
