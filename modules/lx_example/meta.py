"""
@filename: meta.py
@author 葛文星
@date 2023-8-8
@lastModify 2023-8-28
@description 这是龙心系统插件的元数据文件
meta.py是每个模块必须的文件
1 该文件必须放在模块的一级目录下
2 该文件含有该模块应有的信息
3 模块必须是以python包的形式，且要以"lx_"打头
4 __init_.py中必须导入该meta.py
"""
from . import example

# info字典包含了该模块的相关信息，包含name,version,author,description,updateTime字段
info: dict = {
    'name': 'lx_example',
    'version': 'v1.00',
    'author': '葛文星',
    'description': '测试模块案例',
    'updateTime': '2023-08-28'
}
# command字典包含了该模块包含的命令及函数地址，该字段必须包含模块的名称作为命令
command: dict = {'lx_example': example.test}
