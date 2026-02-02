from Relate_table_create import engine, department_table, employee_table

# ps ：注意数据值插入一次
with engine.connect() as conn:
    conn.execute(department_table.insert(), [
        {"name":"hr"},
        {"name":"it"}
    ])
    conn.execute(employee_table.insert(), [
        {"department_id":1, "name":"jack"},
        {"department_id":1, "name":"tom"},
        {"department_id":1, "name":"alice"},
        {"department_id":2, "name":"KK"},
        {"department_id":2, "name":"liam"},
        {"department_id":2, "name":"lihua"}
    ])

    conn.commit()