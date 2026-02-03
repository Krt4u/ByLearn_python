# 映射类与添加记录，基于类的方式实现
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Integer, String, Column, MetaData, Date

engine = create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb")

#调用时动态生产一个基础类，用于定义映射类的基类
Base = declarative_base()

#即是直接定义类，也是在定义表
class Person(Base):
    __tablename__ = "people" #指定表名

    #指定行即字段
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    birthday = Column(Date, nullable=False)

# MetaData.create_all(engine) , 该表没有存入metadata 只能使用Base自带的metadata
Base.metadata.create_all(engine)

# 基于映射添加记录, 因为操作的数据从数据库内容变成了类，因此需要用sessionmaker
# 绑定引擎
Session = sessionmaker(bind=engine)
session = Session() # 使用session代替connection会话开启，事务开始，每一次调用则开启一次事务

if __name__ == '__main__':
    # 添加单条记录对象
    p = Person(name = "kangkang", birthday = "2000-1-1")
    session.add(p) # 添加提交到会话中
    session.commit()
    # 添加多条记录, 将多个对象，将多个对象放入序列，一次提交即可
    ps = [
        Person(name = "alice", birthday = "2000-1-1"),
        Person(name = "amy", birthday = "2000-1-1"),
        Person(name = "damn", birthday = "2000-1-1")
    ]
    session.add_all(ps)
    session.commit()