JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，易于人类阅读和编写，同时也便于机器解析和生成。Python 提供了内置的 json 模块，用于处理 JSON 数据，包括编码和解码操作。

json.dumps() 将 Python 对象编码为 JSON 字符串。
json.dump() 将 Python 对象编码为 JSON 格式并写入文件。
json.loads() 将 JSON 字符串解码为 Python 对象。
json.load() 从文件中读取 JSON 数据并解码为 Python 对象。

JSON 与 Python 数据类型的映射

Python 的 dict 映射为 JSON 的 object。

Python 的 list 和 tuple 映射为 JSON 的 array。

Python 的 str 映射为 JSON 的 string。

Python 的 int 和 float 映射为 JSON 的 number。

Python 的 True 和 False 映射为 JSON 的 true 和 false。

Python 的 None 映射为 JSON 的 null。