# -*- coding: UTF-8 -*-
"""
@Project :Daily_Pro 
@File    :03generate_qrcode.py
@Author  :李睡睡 主人
@Date    :2022/9/19 21:41 
@Scripts :qrcode
@Function:制作二维码
@Tips    :宝剑锋从磨砺出，梅花香自苦寒来。
"""
import qrcode

input_URL = "https://www.bilibili.com/"
img_file = r'../out/02pro.png'

# 实例化QRCode 生成qr对象
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

# 传入数据
qr.add_data(input_URL)

qr.make(fit=True)

# 生成二维码
img = qr.make_image(fill_color="blue",back_color="white")

img.save(img_file)

img.show()