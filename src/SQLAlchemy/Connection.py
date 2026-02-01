import sqlalchemy
print(sqlalchemy.__version__)

#创建引擎, 得到连接
engine = sqlalchemy.create_engine('mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb', echo=False)
#建立连接
connection = engine.connect()
#原始查询
query = sqlalchemy.text('select * from stu')
#执行语句
result_text = connection.execute(query)
for row in result_text:
    print(row)

connection.close()
engine.dispose()