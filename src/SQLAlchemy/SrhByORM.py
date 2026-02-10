# 使用ORM方式查询一对多的关系表
from sqlalchemy import create_engine, String,ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column,relationship, sessionmaker
from typing_extensions import List, Annotated
from datetime import datetime

url = 'mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb?charset=utf8mb4'
engine = create_engine(url, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

int_pk = Annotated[int, mapped_column(primary_key=True)]
str_name = Annotated[str, mapped_column(String(128), nullable=False, unique=True)]
date_date = Annotated[datetime, mapped_column(nullable=False)]


class Department(Base):
    """Department
    Attributes:
        ID:int
        Name:String(128)
    Relationship:
        employee:List['Employee']
    Methods:
        None
    """    
    __tablename__ = 'department'
    __table_args__ = {
        'mysql_charset': 'utf8mb4',  # MySQL指定字符集
        'mysql_collate': 'utf8mb4_unicode_ci'  # 指定排序规则
    }

    ID:Mapped[int_pk]
    Name:Mapped[str_name]

    employee:Mapped[List['Employee']] = relationship(back_populates='department')

    def __repr__(self):
        return f"id = {self.ID}, name = {self.Name}"

class Employee(Base):
    """Employee
    Attributes:
        ID:int
        Name:String(128)
        Birthday:datetime
        Department_id:Mapped[int] = mapped_column(ForeignKey(Department.ID))
    Relationship:
        department:Mapped[Department] = relationship(back_populates='employee') 
    Methods:
        None
    """ 
    __tablename__ = 'employee'
    __table_args__ = {
        'mysql_charset': 'utf8mb4',  # MySQL指定字符集
        'mysql_collate': 'utf8mb4_unicode_ci'  # 指定排序规则
    }

    ID:Mapped[int_pk]
    Name:Mapped[str_name]
    Birthday:Mapped[date_date]
    Department_id:Mapped[int] = mapped_column(ForeignKey(Department.ID))

    department:Mapped[Department] = relationship(back_populates='employee')

    def __repr__(self):
        return f"id = {self.ID}, name = {self.Name}, Birthday = {self.Birthday}, Department_ID = {self.Department_id}"
    
Base.metadata.create_all(engine)