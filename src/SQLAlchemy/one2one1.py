from sqlalchemy import Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column, relationship
from typing_extensions import Annotated

engine = create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/world")
Base = declarative_base()
Session = sessionmaker(bind=engine)

int_pk = Annotated[int, mapped_column(primary_key=True)]
name_pk = Annotated[str, mapped_column(String(128), nullable=False)]

class E(Base):
    __tablename__ = "e"

    id:Mapped[int_pk]   
    name:Mapped[name_pk]
    c_id:Mapped[int] = mapped_column(ForeignKey("c.id"),onupdate="CASCADE", nullable=True)
    # onupdate="CASCADE" 该参数只能放在子表，说明其可以脱离主表约束，变化值
    cx = relationship("C", back_populates="ex")
    # back_populates参数的值是对方类中对应关系的属性名（字符串形式），因为这是对象之间的关联，而不是数据库表之间的关联
    # 表间关联是基于外键，对象间关联基于 relationship

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'

class C(Base):
    __tablename__ = 'c'

    id:Mapped[int_pk]
    name:Mapped[name_pk]
    ex = relationship("E", back_populates="cx")

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'
    
Base.metadata.create_all(engine)