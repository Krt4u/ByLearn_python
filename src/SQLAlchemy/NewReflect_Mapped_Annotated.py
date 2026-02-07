# 表的新映射方法
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, sessionmaker
from sqlalchemy import create_engine, String
import datetime
from typing_extensions import Annotated



engine = create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/world", echo=False)
Base = declarative_base()

# 使用 Mapped 来映射字段
def mapped():
    class Customer(Base):
        __tablename__ = "customer"

        # 字段名：类型 = 更详细字段限制
        id:Mapped[int] = mapped_column(primary_key=True)
        name:Mapped[str] = mapped_column(String(128), nullable=False)
        birthday:Mapped[datetime.datetime] = mapped_column(nullable=False, server_default="")
        # server_default="" 相当于定义sql表中缺省值是什么

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # ps = [
    #     Customer(name = "alice", birthday = "2000-1-1"),
    #     Customer(name = "amy", birthday = "2000-1-1"),
    #     Customer(name = "damn", birthday = "2000-1-1")
    # ]
    # session.add_all(ps)
    # session.commit()
    rows = session.query(Customer).all()
    for row in rows:
        print(row.id, row.name, row.birthday)

# 与定义字段定义信息
def annotated():
    # 意义，直接将字段转换成一种类型来使用
    int_id = Annotated[int, mapped_column(primary_key=True)]
    str_name = Annotated[String(128), mapped_column(nullable=False)]
    # 上述对象就可定义为 id:Mapped[int_id]
    

if __name__ == '__main__':
    pass