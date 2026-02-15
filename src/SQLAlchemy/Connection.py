# 介于orm于core的记忆混淆，在这里声明，在此后的所有数据库操作中，若不是特殊需要，则都是以orm方式

import sqlalchemy
print(sqlalchemy.__version__)

#创建引擎, 得到连接, create_engine() 调用本身不会直接建立任何实际的 DBAPI 连接。
engine = sqlalchemy.create_engine('mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb', echo=False)
# 通过构造方式获取连接url
# url = sqlalchemy.URL.create(
#     'mysql+pymysql',
#     username='pythondb',
#     password='pythondb',
#     database='testdb',
#     host='192.168.1.18',
# )
# engine = sqlalchemy.create_engine(url=url, echo=False)
#建立连接, 若使用上下文管理器创建连接，事务在进入时开启
connection = engine.connect()
#原始查询
query = sqlalchemy.text('select * from stu')
#执行语句
result_text = connection.execute(query)
for row in result_text:
    print(row)

connection.close()
engine.dispose()