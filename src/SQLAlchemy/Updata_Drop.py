import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

# 连接数据库新方法，创建自动映射基类
DATABASE_URL = sqlalchemy.URL.create(
    "mysql+pymysql",
    username='pythondb',
    password='pythondb',
    host='192.168.1.18',
    database='testdb'
)
engine = sqlalchemy.create_engine(DATABASE_URL, echo=False)
# 自动映射表
person = sqlalchemy.Table('person', sqlalchemy.MetaData(),autoload_with=engine)

# 更新：update person set name = 'KK' where id = 1
#   -> person.update().where(person.c.id == 5).values(name = 'KK')
with engine.connect() as conn:
    update_query = person.update().where(person.c.id == 1).values(name = 'KK')
    conn.execute(update_query)
    conn.commit()
