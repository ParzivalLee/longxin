# FastAPI构建服务基础框架

- # Log.py 日志功能类
 - ##  基础函数
 - ### printLog
    用于输出自定义的日志
```python
import Log
Log.printLog('消息类型', '消息内容')
```
 - ### printNotice, printWarning, printError
    用于输出通知，警告和错误消息
```python
import Log
Log.printNotice("通知内容")
Log.printWarning("警告内容")
Log.printError("错误内容")
```