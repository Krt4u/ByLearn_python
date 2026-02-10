from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb")

with Session(engine) as session, session.begin():
    pass
    # 这种写法是开启一个事务时并开始，当事务正常完成时则提交，否则报错回滚

with Session(engine) as session:
    with session.begin():
        pass
    pass
    # 这种写法于上述类似，当内层事务提交时回到外层执行其他代码，当外层事务提交时，Session关闭