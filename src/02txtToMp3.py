# -*- coding: UTF-8 -*-
"""
@Project :Daily_Pro
@File    :02txtToMp3.py
@Author  :李睡睡 主人
@Date    :2022/9/19 18:18
@Scripts :gtts 、 os
@Function:文本转语音(程序运行可能受网络问题的影响)
@Tips    :宝剑锋从磨砺出，梅花香自苦寒来。
"""
import os
from gtts import gTTS

text_to_read = "这是一段用于测试文字转语言的文本"
language = 'zh-CN'
slow_audio_speed = False
filename = "../out/02pro.mp3"

def reading_from_string():
    audio_created = gTTS(text=text_to_read,lang=language,slow=slow_audio_speed)
    audio_created.save(filename)

    os.system(f'start{filename}')


if __name__ == '__main__':
    reading_from_string()
