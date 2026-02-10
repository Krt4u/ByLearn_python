from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb")

Session = sessionmaker(bind=engine) # 到这里就创建好了事务类
session = Session() # 这里就实例化一个事务类并开启
# 事务的ACID原则，如果产生异常，则回滚不会提交，因此多使用上下文管理
# session.close() 关闭事务



