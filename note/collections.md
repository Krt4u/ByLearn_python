https://zhuanlan.zhihu.com/p/343747724

这个模块实现了特定目标的容器，以提供Python标准内建容器dict , list , set , 和tuple 的替代选择。

namedtuple()	创建命名元组子类的工厂函数，生成可以使用名字来访问元素内容的tuple子类
deque	类似列表(list)的容器，实现了在两端快速添加(append)和弹出(pop)
ChainMap	类似字典(dict)的容器类，将多个映射集合到一个视图里面
Counter	字典的子类，提供了可哈希对象的计数功能
Counter(iter).most_commom(top) 返回计算对象的前top个
OrderedDict	字典的子类，保存了他们被添加的顺序，有序字典
defaultdict	字典的子类，提供了一个工厂函数，为字典查询提供一个默认值
UserDict	封装了字典对象，简化了字典子类化
UserList	封装了列表对象，简化了列表子类化
UserString	封装了字符串对象，简化了字符串子类化（中文版翻译有误）


Counter.elements（）方法
c = Counter(a=4, b=2, c=0, d=-2)
list(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']

sorted(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']

c = Counter(a=4, b=2, c=0, d=5)
list(c.elements())
['a', 'a', 'a', 'a', 'b', 'b', 'd', 'd', 'd', 'd', 'd']

subtract()
从迭代对象或映射对象减去元素。像dict.update() 但是是减去，而不是替换。输入和输出都可以是0或者负数。

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

#减去一个abcd
str0 = Counter('aabbccdde')
str0
Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 1})

str0.subtract('abcd')
str0
Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1})