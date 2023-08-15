"""
@filename: meta.py
@author 葛文星
@date 2023-8-8
@lastModify 2023-8-14
@description 这是龙心系统插件的元数据文件
meta.py是每个模块必须的文件
1 该文件必须放在模块的一级目录下
2 该文件含有该模块应有的信息
3 模块必须是以python包的形式，且要以"lx_"打头
4 __init_.py中必须导入该meta.py
"""
from . import example

# command字典包含了该模块包含的命令及函数地址
command: dict = {'lx_example': example.test}
