from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb")

Base = automap_base()
Base.prepare(autoload_with=engine)
# Base = automap_base()
# Base.prepare(engine, reflect=True)
# 强调注意，若是使用原生表对象的类，那么其中定义的__REPR__方法可以使用，但是，若是用automap映射的表，则没有，则是根据存在的表结构，创造全新的表对象，解决方法是可以把__REPR__方法作为一个类属性赋值给automap映射的表对象

# 通过 Base.classes.<tablename> 来获取表
c = Base.classes.department

Session = sessionmaker(engine)
session = Session()
records = session.query(c).all()


for record in records:
    print(record.ID, record.Name)

ba = Base.classes.get('department')
print(ba)



# 方法	代码量	易用性	功能完整性
# automap (推荐)	4行	非常简单	自动映射所有表，包含关系
# metadata.reflect	多行	简单	只反射表结构，无ORM类
# 手动定义类+反射	复杂	繁琐	需要逐个表定义
