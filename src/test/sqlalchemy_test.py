import sqlalchemy
from sqlalchemy.orm import sessionmaker, declarative_base

# 创建引擎
engine = sqlalchemy.create_engine('mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb', echo=False)

#建立表空间
metadata = sqlalchemy.MetaData()

tableBYmeta = sqlalchemy.Table(
    "table_by_meta", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), nullable=False)
)
metadata.create_all(engine)

# 添加数据
def add():
    test_insert = tableBYmeta.insert()
    with engine.connect() as conn:
        conn.execute(test_insert, [
            {"name":"A"},
            {"name":"B"}
        ])
        conn.commit()

#删除数据
def delete():
    with engine.connect() as conn:
        conn.execute(tableBYmeta.delete().where(tableBYmeta.c.id == 10))
        conn.commit()

#修改数据
def modify():
    with engine.connect() as conn:
        conn.execute(tableBYmeta.update().values(name = "some_name").where(tableBYmeta.c.id == 1))
        conn.commit()

# 查找数据
def search():
    with engine.connect() as conn:
        query = tableBYmeta.select()
        result = conn.execute(query).fetchall()
        print(result)

# 类映射表
def create_srh_modify_table_class():
    Base = declarative_base()
    class TableByClass(Base):
        __tablename__ = "TableByClass"
        
        id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
        name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    ps = [
        TableByClass(name = "tom"),
        TableByClass(name = "alice"),
        TableByClass(name = "jack"),
        TableByClass(name = "amy")
    ]
    session.add_all(ps)
    session.commit()

    result_all = session.query(TableByClass).all()
    for i in result_all:
        print(i.id, i.name)

    result_id = session.query(TableByClass).filter(TableByClass.id < 2)
    for i in result_id:
        print(i.id, i.name)

    result = session.query(TableByClass).filter(TableByClass.name == "tom").scalar()
    print(result.id, result.name)

    session.query(TableByClass).filter(TableByClass.name == "tom").update({"name":"kk"})
    session.commit()

def has_table(tablename:str):
    bool = sqlalchemy.inspect(engine).has_table(tablename)
    return bool

# 将表结构映射成对象的方式
def get_table_By_table(tablename:str):
    if has_table(tablename): 
        table = sqlalchemy.Table(tablename, metadata,autoload_with=engine)
        # print(f"tablename {tablename}")
        # print(f"colume {[c.name for c in table.columns]}")
        Session = sessionmaker(bind=engine)
        session = Session()
        rows = session.query(table).all()
        return rows
    return -1

# 使用反射获取所有表，再选择特定表
def 

            

if __name__ == '__main__':
    pass
    table = "TableByClass"
    msg = get_table_By_table(table)
    for i in msg:
        print(i)