# -*- coding: UTF-8 -*-
"""
@Project :Daily_Pro 
@File    :07ToThumbnail.py
@Author  :李睡睡 主人
@Date    :2022/9/22 0:36 
@Scripts :os 、 Image
@Function:生成缩放图
@Tips    :宝剑锋从磨砺出，梅花香自苦寒来。
"""
import os
from PIL import Image

size = (128,128)

for infile in os.listdir("../image"):
    # 是否不是以"."开头
    if not infile.startswith("."):
        outfile = infile.split(".")[0] + "_thumbnail"
        with Image.open("../image/"+infile) as  img:
            img.thumbnail(size)
            img.save("../out/"+outfile+".png")


