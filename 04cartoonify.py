# -*- coding: UTF-8 -*-
"""
@Project :Daily_Pro 
@File    :04cartoonify.py
@Author  :李睡睡 主人
@Date    :2022/9/19 23:01 
@Scripts :cv2.stylization
@Function:制作卡通图片
@Tips    :宝剑锋从磨砺出，梅花香自苦寒来。
"""
import cv2
import sys

img = sys.path[0] + '/image/lena.png'

color_image = cv2.imread(img)

while True:
    cartoon_style_selection = input("This script has 2 styles. Please type 1 or 2:")

    if cartoon_style_selection == "1":
        # Cartoonify process
        cartoon_style_selection_1 = cv2.stylization(color_image,sigma_s=150,sigma_r=0.25)
        cv2.imshow("cartoon_1",cartoon_style_selection_1)
        cv2.waitKey()
        cv2.destroyAllWindows()

    elif cartoon_style_selection == "2":
        cartoon_style_selection_2 = cv2.stylization(color_image,sigma_s=60,sigma_r=0.5)
        cv2.imshow('cartoon_2',cartoon_style_selection_2)
        cv2.waitKey()
        cv2.destroyAllWindows()

    elif cartoon_style_selection == "exit":
        print("退出程序")
        break

    else:
        print("Invalid style selection")
