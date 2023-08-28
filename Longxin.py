"""
@filename: Longxin.py
@author 葛文星
@date 2023-8-8
@lastModify 2023-8-15
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
        self.variables: dict = dict()  # 变量
        self.commands: dict = dict()  # 命令
        self.modules: dict = dict()  # 加载的模块

        """常量区"""
        self.RESP_ERROR_NO_FUNCTION: dict = {'code': -1, 'msg': '未找到该命令'}

    def execute(self, command: str, params: str) -> dict:
        """
        执行前端发送来的命令
        :param command: 命令名称
        :param params: 命令参数
        :return: 命令执行结果
        """
        func = self.commands.get(command)
        if not func:
            return self.RESP_ERROR_NO_FUNCTION
        response: dict = func(params)
        return response

    def loadModules(self) -> None:
        """
        加载龙心系统的模块
        :return: None
        1 读取文件列表
        2 剔除非模块文件
        3 逐个读取加载模块
        """
        Log.printInfo("正在加载模块")
        Log.printInfo("正在读取模块")
        # 读取文件列表
        modules_dir: list = list(os.listdir(self.modulesDir))
        # 剔除非模块文件
        modules_dir.remove('__pycache__')
        # 逐个读取加载模块
        for i in modules_dir:
            # 检查模块是否符合命名规则
            if i.startswith('lx_'):
                Log.printInfo("正在读取模块 %s" % i)
                try:
                    # 列出模块目录下的文件
                    modules_files: list = os.listdir(os.path.join(self.modulesDir, i))
                    # 检查模块中是否含有meta.py文件
                    if 'meta.py' in modules_files:
                        Log.printInfo("正在载入模块 %s" % i)
                        self.modules.update({i: importlib.import_module("%s.%s" % (self.modulesDir, i))})
                        self.commands.update(self.modules.get(i).meta.command)
                        Log.printInfo("已载入模块 %s" % i)
                    else:
                        Log.printWarning("%s 模块格式有误，模块中应包含meta.py文件，已跳过" % i)
                except NotADirectoryError:
                    Log.printWarning("%s 模块格式有误，模块应为python库格式，已跳过" % i)
            else:
                Log.printWarning("%s 模块名称有误，请以lx_打头，已跳过" % i)

    def loadModule(self, module_name: str) -> dict:
        """
        加载单一模块，可动态加载
        :param module_name: 模块名称
        :return: 加载结果（字典）
        """
        result: dict = dict()
        if module_name.startswith('lx_'):
            try:
                modules_files: list = os.listdir(os.path.join(self.modulesDir, module_name))
                if 'meta.py' in modules_files:
                    self.modules.update(
                        {module_name: importlib.import_module("%s.%s" % (self.modulesDir, module_name))})

                    self.commands.update(self.modules.get(module_name).meta.command)

                    result.update({'code': 0, 'msg': "已载入模块 %s" % module_name})
                else:
                    result.update({'code': -1, 'msg': "%s 模块格式有误，模块中应包含meta.py文件，已跳过" % module_name})
            except NotADirectoryError:
                result.update({'code': -1, 'msg': "%s 模块格式有误，模块应为python库格式，已跳过" % module_name})
        else:
            result.update({'code': -1, 'msg': "%s 模块名称有误，请以lx_打头，已跳过" % module_name})

        return result
