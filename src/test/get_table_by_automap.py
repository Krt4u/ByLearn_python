from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/world")

Base = automap_base()
Base.prepare(autoload_with=engine)

c = Base.classes.c

Session = sessionmaker(engine)
session = Session()
records = session.query(c).all()


for record in records:
    print(record.id, record.name)



# 方法	代码量	易用性	功能完整性
# automap (推荐)	4行	非常简单	自动映射所有表，包含关系
# metadata.reflect	多行	简单	只反射表结构，无ORM类
# 手动定义类+反射	复杂	繁琐	需要逐个表定义
