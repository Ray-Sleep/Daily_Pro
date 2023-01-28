# -*- coding: UTF-8 -*-
"""
@Project : Daily_Pro 
@File    : Image finding.py
@IDE     : PyCharm 
@Author  : 李睡睡
@Date    : 2023/1/28 6:43 
@Scripts : time、cv2、pyautogui
@Documentation:https://www.bilibili.com/video/BV1YR4y1G7Ye/?spm_id_from=333.337.search-card.all.click&vd_source=fa4736bfe6ad0afc755decfbf72b082a
@Function: 点击屏幕中与目标图片相匹配的中心坐标
@Bug     : 目前只能进行主屏幕的屏幕截取与目标查询工作
@Tips    : 不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""
import time
import cv2
import pyautogui

def get_xy(img_model_path):
    """
    用来判断游戏画面的点击坐标
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
    pyautogui.screenshot().save('./img/screenshot.png')
    # 载入截图
    img = cv2.imread('./img/screenshot.png')      # 屏幕截图路径
    # 图像模板
    img_terminal = cv2.imread('./img/target01.png')     # 目标模板截图
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
    pyautogui.click(var_avg[0],var_avg[1],button="left")
    # 睡眠操作：等待界面跳转
    time.sleep(1)

# 封装方法
def  routine(img_model_path,name):
    avg = get_xy(img_model_path)
    print(f"正在点击{name}")
    auto_click(avg)


routine("./img/target01.png","目标")