"""
@filename: Longxin.py
@author 葛文星
@date 2023-8-8
@lastModify 2023-8-14
@description 龙心系统核心类
"""
import os

import Log
import importlib


class Longxin:
    """
    龙心系统核心类
    """

    def __init__(self, modules_dir: str = 'modules'):
        self.modulesDir = modules_dir  # 模块储存的文件夹
        self.variables: dict = dict()
        self.commands: dict = dict()
        self.modules: dict = dict()  # 加载的模块

    def execute(self, command: str, params: str) -> dict:
        """
        执行前端发送来的命令
        :param command: 命令名称
        :param params: 命令参数
        :return: 命令执行姐结果
        """
        response: dict = self.commands.get(command)(params)
        return response

    def loadModules(self) -> None:
        """
        加载龙心系统的模块
        :return: None
        1 读取文件列表
        """
        Log.printInfo("正在加载模块")
        Log.printInfo("正在读取模块...")
        # 读取文件列表
        modules_dir: list = list(os.listdir(self.modulesDir))
        modules_dir.remove('__pycache__')
        for i in modules_dir:
            Log.printInfo("正在尝试加载模块 %s" % i)
            try:
                modules_files: list = os.listdir(os.path.join(self.modulesDir, i))
                if 'meta.py' in modules_files:
                    Log.printInfo("正在载入模块 %s" % i)
                    self.modules.update({i: importlib.import_module("%s.%s" % (self.modulesDir, i))})
                    self.commands.update(self.modules.get(i).meta.command)
            except NotADirectoryError:
                Log.printWarning("%s 模块格式有误，已跳过" % i)

