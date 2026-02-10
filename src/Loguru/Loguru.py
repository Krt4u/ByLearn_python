# 内置日志库login的补强
from loguru import logger
import sys

logger.remove(0) # 移除处理程序的默认配置，（默认配置id为0）

# 新增默认配置，并设置提示等级，输出格式
logger.add(sys.stderr,  # 默认，错误信息输入位置 如果是 “filename” 则将内容输出到该文件中
            level="TRACE",
            # format="{time} | {level} | {message}",
            # serialize=True, 序列化选项，支持json格式输入日志内容
            # rotation="5 seconds", # 关闭当前文件并创建新文件
            # retention="1 minute" / 3 # 仅保留最新 3 各文件或1分钟内的文件
            # encoding='urf-8', 输出编码
            # mode="w", 文件打开方式
            ) 

logger.trace("A trace message.")
logger.debug("A debug message.")
logger.info("An info message.")
logger.success("A success message.")
logger.warning("A warning message.")
logger.error("An error message.")
logger.critical("A critical message.")





