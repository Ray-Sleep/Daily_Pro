# -*- coding: UTF-8 -*-
"""
@Project :Daily_Pro 
@File    :10add_size.py
@Author  :李睡睡 主人
@Date    :2022/9/23 21:16 
@Scripts :requests
@Documentation:https://deepai.org/machine-learning-model/torch-srgan
@Function:超分辨率就是把通过网络图像分辨率变大，将模糊的图片变得更加清晰且图像中的原有信息不会缺失。(
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""
import requests
r = requests.post(
    "https://api.deepai.org/api/torch-srgan",
    files={
        'image': open('../image/old-pic.jpg', 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())



