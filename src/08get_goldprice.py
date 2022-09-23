# -*- coding: UTF-8 -*-
"""
@Project :Daily_Pro 
@File    :08get_goldprice.py
@Author  :李睡睡 主人
@Date    :2022/9/22 0:56 
@Scripts :requests 、 beautifulsoup4
@Function:获取实时黄金价格
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""
import re
import requests

gold_api_url = "https://api.jijinhao.com/quoteCenter/history.htm?code=JO_52683&style=3&pageSize=10&needField=128,129,70&currentPage=1&_=1663781809870"
response = requests.get(gold_api_url)

# 正则表达式第一次过滤
# temp = re.findall(r'[^{]*?1663689600000',response.text)
temp = re.findall(r'\[.*?]', response.text)
# 正则表达式第二次过滤
ans = re.findall(r'[0-9]{3}\.[0-9]',temp[0][-86:-1])
print("中国黄金基础金价："+ans[0])

# 2022/9/21 黄金价格：385.4
# 2022/9/22 黄金价格：385.7

"""
def get_price(url):
    data = requests.get(url)
    data.encoding = 'utf8'
    soup = bs(data.text, 'html.parser')  # converting
    ans = soup.find('table', id="goldTableSum").text
    return ans


url = "https://quote.cngold.org/gjs/swhj_zghj.html"
ans = get_price(url)
print(ans)

"""
