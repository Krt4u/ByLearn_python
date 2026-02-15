https://zhuanlan.zhihu.com/p/637347770

typing常用类型
以下是typing包中常用的类型和泛型。

注意，int, float,bool,str, bytes不需要import typing，Any,Union,Tuple等需要import typing

基本类型:
int: 整数类型
float: 浮点数类型
bool: 布尔类型
str: 字符串类型
bytes: 字节类型
Any: 任意类型
Union: 多个类型的联合类型，表示可以是其中任意一个类型
Tuple: 固定长度的元组类型
List: 列表类型
Dict: 字典类型，用于键值对的映射
泛型:
Generic: 泛型基类，用于创建泛型类或泛型函数
TypeVar: 类型变量，用于创建表示不确定类型的占位符
Callable: 可调用对象类型，用于表示函数类型
Optional: 可选类型，表示一个值可以为指定类型或None
Iterable: 可迭代对象类型
Mapping: 映射类型，用于表示键值对的映射
Sequence: 序列类型，用于表示有序集合类型
Type:泛型类，用于表示类型本身