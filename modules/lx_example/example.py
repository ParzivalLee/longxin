"""
@filename: lx_example.py
@author 葛文星
@date 2023-8-8
@lastModify 2023-8-14
@description 这是龙心系统的示例文件
"""


def test(params: dict):
    response: dict = {
        'code': 0,
        'msg': "这是一个示例文件，参数将原封不动的返回过去",
        'data': params
    }
    return response
