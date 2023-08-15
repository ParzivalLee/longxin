"""
@filename config.py
@author Parzival
@date 2023-07-24
@lastModified 2023-07-24
@encoding utf-8
@description 配置文件读取
"""

import configparser

"""
1. 读取配置文件
2. 服务器配置
3. MongoDB
"""

"""读取配置文件"""
configParser = configparser.ConfigParser()
configParser.read("config.ini", encoding='utf-8')

# """服务器配置"""
# WEBSERVER_HOST = configParser.get("web_server", "host")
# WEBSERVER_PORT = int(configParser.get("web_server", "port"))

# """MongoDB"""
# MONGO_HOST = configParser.get("mongo", "host")
# MONGO_PORT = int(configParser.get("mongo", "port"))
# MONGO_DATABASE = configParser.get("mongo", "database")
