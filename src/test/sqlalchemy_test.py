import sqlalchemy
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import NoReturn
from tabulate import tabulate
import pandas as pd

# 创建引擎
engine = sqlalchemy.create_engine('mysql+pymysql://pythondb:pythondb@192.168.1.18/world', echo=False)

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
        # table = metadata.Table[tablename]

        # print(f"tablename {tablename}")
        # print(f"colume {[c.name for c in table.columns]}")
        Session = sessionmaker(bind=engine)
        session = Session()
        rows = session.query(table).all()
        return rows
    return -1

# 使用反射获取所有表，再选择特定表(查询所有表及其内容)
def Reflect_all() -> NoReturn:
    # 反射所有表空间
    metadata.reflect(bind=engine)
    with engine.connect() as conn:
        for table in metadata.tables:
            print(f"表名: {table}")
            print("------------------------------------------------------")
            # 获取每一张表的表结构
            tb = metadata.tables[table]
            print("表结构: ", end=' ')
            for c in tb.columns:
                print(f"{c.name}: {c.type}", end='\t')
            print("\n====================================================")
            # 打印每张表的行
            result = conn.execute(tb.select())
            rows = result.fetchall()
            if rows:
                for row in rows:
                    print(row)
            print()


# 传入表名, 返回其内容
def get_table_con(tbname:str, limit:int = None) -> any:
    # 先判断表是否存在
    if not has_table(tbname):
        return None
    
    # 映射该表的对象
    table = sqlalchemy.Table(tbname, metadata, autoload_with=engine)
    print(f"表名: {table.name}")
    # 创建会话,使用orm获取表数据
    Session = sessionmaker(bind=engine)
    session = Session()
    # 获取所有行数据
    rows = session.query(table).all()
    if not rows:
        return
    # 打印行列名
    head = []
    for column in table.columns:
        head.append(f"{column.name}:{column.type}")
    data = []
    for c in rows[:limit]:
        # c = str(c).replace("(", "").replace(")", "").replace(",", "\t")
        data.append(c)
    
    # 使用 tabulate 对齐表
    print(tabulate(data, headers=head, tablefmt="grid"))

    # 使用 pandas 对齐表
    # df = pd.DataFrame(data, columns=head)
    # print(df.to_string(index=False))

        

if __name__ == '__main__':
    pass
    table = "city"
    get_table_con(table, 10)
