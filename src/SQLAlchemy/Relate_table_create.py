import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb", echo=False)
metedate = sqlalchemy.MetaData()
# 定义表空间的映射对象Table
department_table = sqlalchemy.Table(
    "department", metedate,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True, nullable=False),
)
# 该表的department_id是department表的id的外键
employee_table = sqlalchemy.Table(
    "employee", metedate,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("department_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("department.id"), nullable=False),
    sqlalchemy.Column("name", sqlalchemy.String(128), nullable=False),
)
# 判断表是否存在，metedate.create_all(engine) 其实会判断如果表存在则不创建
if not (sqlalchemy.inspect(engine).has_table("department") and sqlalchemy.inspect(engine).has_table("employee")): 
    metedate.create_all(engine)
