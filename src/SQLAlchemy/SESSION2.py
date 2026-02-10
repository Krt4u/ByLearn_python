from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb")
engine1 = create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb1")

# 当项目遇到需要操作多个数据库时，可以创建多个引擎和会话Session，在各自的上下文管理器中执行各自的动作即可

with Session(engine) as session:
    with session.begin():
        pass
    pass

with Session(engine1) as session:
    with session.begin():
        pass
    pass

# 假设需要同时操作两个数据库的会话
with Session(engine) as session, session.begin(), Session(engine1) as session1, session1.begin():
    pass