import sqlalchemy
from Relate_table_create import engine, department_table, employee_table

# 一对多关联表查询
# search_table.join(relate_table, search_table_c_cname == relate_table_c_cname)

with engine.connect() as conn:
    join = employee_table.join(department_table, employee_table.c.department_id == department_table.c.id)
    #employee JOIN department ON employee.department_id = department.id
    # 多表查询需要用sqlalchemy.select(join)来指定连接条件
    # query = sqlalchemy.select(join).where(department_table.c.name == 'hr')
    # print(conn.execute(query).fetchall())
    query = employee_table.select().join(department_table, employee_table.c.department_id == department_table.c.id).where(department_table.c.name == 'hr')
    print(query)
    print(conn.execute(query).fetchall())


