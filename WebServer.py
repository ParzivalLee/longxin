"""
@filename WebServer.py
@author Parzival
@date 2023-07-24
@lastModified 2023-07-24
@encoding utf-8
@description 网页服务器
"""
import pymongo
import config
from fastapi import FastAPI

"""全局变量"""
global_variable: dict = dict()

"""FastAPI服务"""
app = FastAPI(debug=True)

# """Mongo数据库连接"""
# mongoClient = pymongo.MongoClient(host=config.MONGO_HOST, port=config.MONGO_PORT)
# mongoDB = mongoClient[config.MONGO_DATABASE]
