# -*- coding: UTF-8 -*-
"""
@Project :Daily_Pro 
@File    :06JpegToPNG.py
@Author  :李睡睡 主人
@Date    :2022/9/22 0:22 
@Scripts :pillow
@Function:jpeg图片 与 PNG图片的互相转换
@Tips    :宝剑锋从磨砺出，梅花香自苦寒来。
"""
from PIL import Image
img = Image.open('../image/lena.png')
img.save('../out/06_pro.jpeg')
