"""
@filename: LongxinController.py
@author 葛文星
@date 2023-8-8
@lastModify 2023-8-10
@description 龙心控制器
"""

import WebServer
from fastapi import Request
from Longxin import Longxin

# 初始化龙心核心类
longxin: Longxin = Longxin()
longxin.loadModules()


@WebServer.app.post('/longxin')
async def longxin_call(request: Request) -> dict:
    """
    龙心呼叫函数
    :param request: 呼叫请求
    :return: 响应结果
    1。 验证身份
    2. 获取参数
    3. 执行命令
    4. 返回结果
    """
    # 验证身份
    token: str = request.headers.get('Authorization')

    # 获取参数
    req_params: dict = await request.json()
    command = req_params.get('command')
    params = req_params.get('params')

    # 执行命令
    response: dict = longxin.execute(command, params)

    # 返回响应结果
    return response
