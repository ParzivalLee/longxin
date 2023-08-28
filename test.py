"""
@filename: test.py
@author 葛文星
@date 2023-8-24
@lastModify 2023-8-24
@description 龙心系统测试脚本
"""
import requests

"""常量"""
# 龙心系统响应地址
url: str = 'http://127.0.0.1:5000/longxin'
# 测试龙心示例响应
params: dict = {
    'command': 'lx_example',
    'params': {'test': '0'}
}
resp: requests.Response = requests.post(url, json=params)
print(resp.json())
