import sqlalchemy

Target = 'mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb'

engine = sqlalchemy.create_engine(Target, echo=True)

#存储表空间定义
meta_data = sqlalchemy.MetaData()

#创建表，若数据库中已经存在则不执行
person = sqlalchemy.Table(
    'person', meta_data, # 表名，将所有表结构都存储在该对象中
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True, nullable=False),
    sqlalchemy.Column("Birthday", sqlalchemy.DATE, nullable=False)
)
#创建所有存储在该表空间中的表，基于那个引擎创建
meta_data.create_all(engine)

# #增加一条语句
# person_insert = person.insert() #获取person的insert对象
# # print(person_insert) #INSERT INTO person (id, name, "Birthday") VALUES (:id, :name, :Birthday)
# person_tom = person_insert.values(name='tom', Birthday='2000-1-1')
# # print(person_tom)
# #person_insert.values(name='tom', Birthday='2000-1-1')最终将其转换成sql语句

# with engine.connect() as conn:
#     result = conn.execute(person_tom) 
#     print(result.inserted_primary_key) #获取自增加键值，即使语句添加出错也增
#     conn.commit() #sqlalchemy 默认开启事务模式，需要进行提交

# # 多条语句
# person_insert = person.insert()
# with engine.connect() as conn:
#     conn.execute(person_insert, [
#         {"name":"aaa", "Birthday":"2030-1-1"},
#         {"name":"bbb", "Birthday":"2022-1-1"},
#         {"name":"ccc", "Birthday":"1999-1-1"},
#     ])
#     conn.commit()
