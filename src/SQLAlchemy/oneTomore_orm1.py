# 一对多的映射关系
from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship
from typing_extensions import Annotated
from sqlalchemy.sql import func
import datetime
from typing import List


engine = create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/world")
Base = declarative_base()
Session = sessionmaker(bind=engine)

int_id = Annotated[int, mapped_column(primary_key=True)]
required_unique_name = Annotated[str, mapped_column(String(128),nullable=False, unique=True)]
# 获取时间戳
timestamp_not_null = Annotated[datetime.datetime, mapped_column(nullable=False)]

class Department(Base):
    __tablename__ = "department"

    id:Mapped[int_id]
    name:Mapped[required_unique_name]
    create_time:Mapped[timestamp_not_null]
    # 关联表查询什么字段时能获取主表的内容 back_populates 指定表关联属性名
    employees:Mapped[List["Employee"]] = relationship(back_populates="department")
    # 我的Department类有有一个叫employees的属性，他的值是由一个Employee对象组成的列表，在插入Department表内容时，relationship(back_populates="department")告诉 employees中的Employee也要同步创建去关联department字段的数据，因为一个Dpartment对象可以对应多个Employee所以需要使用序列来存储

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, create_time: {self.create_time}"
    
class Employee(Base):
    __tablename__ = "employee"

    id:Mapped[int_id]
    dep_id:Mapped[int] = mapped_column(ForeignKey("department.id"))
    name:Mapped[required_unique_name]
    birthday:Mapped[timestamp_not_null]
    # 该字段指向另一个数据库，relationship() 表示不是一个真正的字段，而是关系字段，是内存中的关系
    department:Mapped[Department] = relationship(lazy=False, back_populates="employees") # 该表指向关联表，主表查询其中的名称时能获取关联表的内容 back_populates 指定表

    # department:Mapped[Department] = relationship(lazy=False, backref="employee")
    # lazy=False, 关闭懒查询
    # backref="employee"，为关联字段的表执行双向关联，在其查询 backref 的命名值时，同时也查询其被关联的表的同字段内容，返回数组，但这是单方面的双向关联，在主表内容中没有体系，不便于维护，因此上述方法更好

    def __repr__(self):
        return f"id: {self.id}, dep_id: {self.dep_id}, name: {self.name}, create_time: {self.birthday}"

if __name__ =='__main__':
    Base.metadata.create_all(engine)
