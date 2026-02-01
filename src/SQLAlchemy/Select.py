from Create_table import engine, person
# select * from person -> person.select()

#查询所有: select * from person -> person.select()
with engine.connect() as conn:
    query_all = person.select()
    # print(query) # 返回一个迭代器
    result_set = conn.execute(query_all)
#循环提取
    # for row in result:
    #     print(row)
    #     print(row.name)
#函数提取
    # result_li = result.fetchall() # 直接将内容提取为数组而非迭代器
    # row = result.fetchone() # 只提取一条记录

# 条件查询: select * from person where Birthday > '2000-1-1'
# -> person.select().where(person.c.birthday > '2000-1-1')
    query_condition = person.select().where(person.c.Birthday > '2000-1-1')
    result_set = conn.execute(query_condition)
    result = result_set.fetchall()
    print(result)
# 其他: or -> or_(); and -> and_(); where -> where()
