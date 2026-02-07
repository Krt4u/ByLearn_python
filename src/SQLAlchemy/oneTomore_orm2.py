from oneTomore_orm1 import Session, Department, Employee

# 插入关联数据
def insert(session):
    d1 = Department(name="hr", create_time="1999-1-1")
    e1 = Employee(department=d1, name="jack", birthday="2000-1-1")
    session.add(e1)
    session.commit()
    # department=d1 通过关联属性关联，自动捕获其关联的表，并同时创建他们，且关联的字段值自动赋值一致(由主表确定)


    # d1 = Department(name="hr", create_time="1999-1-1")
    # # session.add(d1)
    # # session.commit()
    # # # # 关键方法在提交数据后刷新一下，然后再再其关联数据库的字段写入数据时就能成功，但对于批量处理，此方法不推荐
    # # # session.flush()
    # e1 = Employee(dep_id=d1.id, name="jack", birthday="2000-1-1")
    # session.add(e1)
    # session.commit()

session = Session()
# insert(session)

emp = session.query(Employee).filter(Employee.dep_id == 1).all()
# 只打印查询表的信息
print(emp)
# 通过查询连接表字段，可以获取其外键与其对应的值
# 不用则不查，用则查 -> 称为懒查询，当关联函数 relationship() 中有参数 lazy=False 时则在只查询query语句后数据库并没有执行真正的查询，而是在使用是才被查询，如果需要遍历，则应该预加载，使用 session.query(Department).options(selectinload(Department.employee)).all()，加载去关联表的内容
# print(emp.department)

dep = session.query(Department).filter(Department.id==1).all()
print(dep)



