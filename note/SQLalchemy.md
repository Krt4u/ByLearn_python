官方文档：[概述 — SQLAlchemy 2.0 文档 - SQLAlchemy 中文](https://docs.sqlalchemy.org.cn/en/20/intro.html)

注意：本文档不涉及库的基础知识，如有需要，请到上述官方文档链接处查看



# SQLAlchemy-Core

## 1，建立连接，定义表空间，创建表 ，插入

```python
import sqlalchemy

# 创建连接引擎
URL = 'mysql+pymysql://username:username@host/database'
engine = sqlalchemy.create_engine(URL, echo=True)
# 定义存储表空间
meta_data = sqlalchemy.MetaData()
# 创建一张表
person = sqlalchemy.Table(
	'person', meta_data,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True,nullable=False),
    sqlalchemy.Column("Birthday", sqlalchemy.DATE, nullable=False)
)
# 创建存储在meta_data表空间中的表
meta_data.create_all(engine)
# 构建person表的插入SQL语句
person_insert = person.insert() #INSERT INTO person (id, name, "Birthday") VALUES (:id, :name, :Birthday)
person_tom = person_insert.values(name='tom', Birthday='2000-1-1')
# 建立引擎连接，执行构建的SQL语句
with engine.connect() as conn:
    result = conn.execute(person_tom)
    conn.commit() #sqlalchemy 默认开启事务模式，需要进行提交
# 多条语句
# person_insert = person.insert()
# with engine.connect() as conn:
#     conn.execute(person_insert, [
#         {"name":"aaa", "Birthday":"2030-1-1"},
#         {"name":"bbb", "Birthday":"2022-1-1"},
#         {"name":"ccc", "Birthday":"1999-1-1"},
#     ])
#     conn.commit()

```

