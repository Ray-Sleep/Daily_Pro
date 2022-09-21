# -*- coding: UTF-8 -*-
"""
@Project ：Daily_Pro
@File    ：01voice_recorder.py
@Author  ：李睡睡 主人
@Date    ：2022/9/17 20:06
@Scripts :sounddevice、scipy.io.wavfile
@Function:录音功能(程序会自动检测外接的录音设备，如果没有会报错)
@Tips    ：宝剑锋从磨砺出，梅花香自苦寒来。
"""
import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # sample_rate

second = int(input("Enter the time duration in second: "))  # enter your required time ..

print("Recording...\n")

record_voice = sd.rec(int(second * fs),samplerate = fs,channels = 2)

sd.wait()

write("../out/01pro.wav",fs,record_voice)

print("Finished...\nPlease Check it...")
