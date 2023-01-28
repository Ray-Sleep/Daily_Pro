# -*- coding: UTF-8 -*-
"""
@Project : Daily_Pro 
@File    : 13ToImagePerspective.py
@IDE     : PyCharm 
@Author  : 李睡睡
@Date    : 2023/1/28 23:31 
@Scripts :
@Documentation:
@Function:
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""
import cv2
import numpy as np

# 报错信息：215
# 断言失效：OpenCV可能无法找到图片路径；src指定坐标对应位置报错

img = cv2.imread('')

# 获取变换矩阵
# src是原图的 4 个坐标
src = np.float32([[80,200],[1000,25],[0,1500],[1200,1460]])
dst = np.float32([[0,0],[638,0],[0,851],[638,851]])
M = cv2.getPerspectiveTransform(src,dst)

# 透视变换
new_img = cv2.warpPerspective(img,M,(638,851))

cv2.imshow('img',img)
cv2.imshow('new_img',new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()