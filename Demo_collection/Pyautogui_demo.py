# -*- coding: UTF-8 -*-
"""
@Project : Ray_Pro
@File    : Pyautogui_demo
@IDE     : PyCharm
@Author  : 李睡睡
@Date    : 2023/7/2 1:27
@Scripts :
@Documentation:
@Function: 
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""
import pyautogui as pyg
import cv2
import time
import pandas as pd

"""
    1.通过截图找到输入框坐标
    2.将记事本中的内容粘贴
    3.复制到聊天框中
    4.寻找发生按钮，并点击
    5.三四步进行循环
"""

def get_xy(img_model_path):
    """
    用来判断画面的点击坐标
    :param img_model_path:用来检测的模板图片的路径
    :return:以元组形式返回检测到的区域中心的坐标
    @important:
        MatchTemplate函数参数解析
        MatchTemplate(InputArray image, InputArray templ, OutputArray result, int method);
        image：输入一个待匹配的图像，支持8U或者32F。
        templ：输入一个模板图像，与image相同类型。
        result：输出保存结果的矩阵，32F类型。
        method：要使用的数据比较方法
    """
    # 将截图保存
    pyg.screenshot().save('./image/screenshot.png')
    # 载入截图
    img = cv2.imread('./image/screenshot.png')      # 屏幕截图路径
    # 图像模板
    img_terminal = cv2.imread('./image/target01.png')     # 目标模板截图
    # 保存截图的宽、高
    height,width,channel = img_terminal.shape
    # 进行模板匹配
    res = cv2.matchTemplate(img,img_terminal,cv2.TM_SQDIFF_NORMED)
    # 解析出匹配区域的左上角坐标
    upper_left = cv2.minMaxLoc(res)[2]
    # 计算匹配区域右下角的坐标
    lower_right = (upper_left[0] + width , upper_left[1] + height)
    # 计算中心区域的坐标并且返回
    avg = (int((upper_left[0] + lower_right[0])/2),int((upper_left[1] + lower_right[1])/2))
    return avg

# 得到坐标，从而实现自动点击（可以实现更多自动化操作）
def auto_click(var_avg):
    """
    接受一个元组参数，自动点击
    :param var_avg: 左边元组
    :return: None
    """
    pyg.click(var_avg[0],var_avg[1],button="left")
    # 睡眠操作：等待界面跳转
    time.sleep(1)

def openreadtxt(file_name):
    data = []
    file = open(file_name,'r')  #打开文件
    file_data = file.readlines() #读取所有行
    for row in file_data:
        tmp_list = row.split(' ') #按‘，’切分每行的数据
        tmp_list[-1] = tmp_list[-1].replace('\n',',') #去掉换行符
        data.append(tmp_list) #将每行数据插入data中
    return data

# 封装方法
def  routine(img_model_path,name):
    avg = get_xy(img_model_path)
    print(f"正在点击{name}")
    auto_click(avg)

def read_tablemethod(filename):
    data = pd.read_table(filename, delim_whitespace=True)
    return data


if __name__ == "__main__":
    routine("img/target01.png", "微信聊天框")
    data = read_tablemethod('./include/information.txt')
    print(data)
