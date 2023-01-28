# -*- coding: UTF-8 -*-
"""
@Project :Daily_Pro 
@File    :11add_color.py
@Author  :李睡睡 主人
@Date    :2022/9/23 21:32 
@Scripts :requests
@Documentation:https://deepai.org/machine-learning-model/colorizer
@Function:给图片上色（可能与真实原场景不符）
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""
import requests
r = requests.post(
    "https://api.deepai.org/api/colorizer",
    files={
        'image': open('../image/old-pic.jpg', 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())