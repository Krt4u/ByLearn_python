from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column,relationship,joinedload
import datetime
from typing import List
from typing_extensions import Annotated

engine = create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb")

Base = declarative_base()

id_int = Annotated[int, mapped_column(primary_key=True)]
dname_str = Annotated[str, mapped_column(String(128),nullable=False, unique=True)]
time_time = Annotated[datetime.datetime, mapped_column(nullable=False)]

class Department(Base):
    __tablename__ = "department"

    id:Mapped[id_int]
    dname:Mapped[dname_str]
    time:Mapped[time_time]
    employees:Mapped[List['Employee']] = relationship(lazy=False, back_populates='department')

    def __repr__(self):
        return f"id: {self.id}, dname: {self.dname}, time: {self.time}"
    
class Employee(Base):
    __tablename__ = "employee"

    id:Mapped[id_int] 
    did:Mapped[int] = mapped_column(ForeignKey("department.id"))
    name:Mapped[dname_str]
    ctime:Mapped[time_time]
    department:Mapped[Department] = relationship(back_populates='employees')

    def __repr__(self):
        return f"id: {self.id}, did: {self.did}, name: {self.name}, ctime: {self.ctime}"

Base.metadata.create_all(engine)

def insert():
    Session = sessionmaker(bind=engine)
    session = Session()


    d1 = Department(dname='hr', time='2000-1-1')
    d2 = Department(dname='it', time='2020-1-1')


    ps_Employee = [
        Employee(department=d1, name="jack", ctime="2000-1-1"),
        Employee(department=d1, name="tony", ctime="2020-1-1"),
        Employee(department=d2, name="amy", ctime="2010-1-1"),
        Employee(department=d2, name="tiantian", ctime="2050-1-1")
    ]
    session.add_all(ps_Employee)
    session.commit()


if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    print(session.query(Employee).filter(Employee.did == 1).all())
    # 使用预加载可以一次性将数据加载进入内容，减少查询次数。
    # ps 注意 如果只是打印dept并不会有其关联的表内容，因为在其表对象中设定了 __repr__ 打印函数，只会打印特定的值，需要显式指定打印关联表的内容/更改打印函数的输出
    dept = session.query(Department).options(joinedload(Department.employees)).filter(Department.id == 1).first()

    for emp in dept.employees:
        print(f"部门：{dept.dname}, 姓名：{emp.name}")
