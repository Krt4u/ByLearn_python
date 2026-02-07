# 表的多对多关系

from sqlalchemy import create_engine, String, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column, Relationship
from typing import List
from typing_extensions import Annotated

engine = create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/world")
Base = declarative_base()

# 对于多对多的关系，可以使用对象创建表，然后将其关联即可，这里使用更基础的方法，使用 core 的方法创建被多关联的表，对象创建其关联的表

int_pk = Annotated[int, mapped_column(primary_key=True)]
name_pk = Annotated[str, mapped_column(String(128), unique=True, nullable=False)]
string = Annotated[str, mapped_column(String(128), nullable=False)]

# 关联关系表定义, 假设关联 A C 表，则需要使用CROE方式创建中间表 B，他不需要orm且唯一作用就是存储两表的id之间的关系
association_table = Table(
    "user_role",
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('role_id', ForeignKey('roles.id'), primary_key=True)
)

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int_pk]
    name: Mapped[name_pk]

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"
    
class User(Base):
    __tablename__ = "users"

    id: Mapped[int_pk]
    name: Mapped[name_pk]
    pwd: Mapped[string]
    roles: Mapped[List['Role']] = Relationship(secondary=association_table, lazy=False)
    # secondary 该参数意在告诉系统，查找user表的角色数据，可以通过中间表secondary=association_table，来定位第三张表，如果想要从第三张表定位到该表，则也按此添加一个属性即可，建立双向查询

# secondary 参数是 SQLAlchemy 在多对多关系中的关键指令。它直接告诉ORM：
# “不要试图在这两张表（users 和 roles）之间直接找外键，它们是通过我指定的这个 association_table（关联表）来间接连接的。”
# 没有 secondary 参数：SQLAlchemy会认为你想建立的是一个基于直接外键的一对多或多对一关系。
# 有了 secondary 参数：SQLAlchemy立刻明白这是一个多对多关系，并会使用你指定的关联表来构建正确的JOIN查询。

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"
    
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


    

