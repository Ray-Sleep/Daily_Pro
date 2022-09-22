# -*- coding: UTF-8 -*-
"""
@Project :Daily_Pro 
@File    :09DollarToYuan.py
@Author  :李睡睡 主人
@Date    :2022/9/22 21:59 
@Scripts :requests
@Documentation:https://www.alphavantage.co/documentation/
@Function:美元转换人民币(= = 此功能需要开会员，楼主一开始也不知道，鞠躬了)
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""
import requests

url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=CNY&apikey=6IPUVSTG00'
r = requests.get(url)
data = r.json()

print(data)
