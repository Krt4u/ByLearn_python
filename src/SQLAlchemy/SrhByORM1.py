from SrhByORM import Department, Employee, Session, engine
from sqlalchemy import select, update, delete, Subquery, insert, values
from sqlalchemy.orm import outerjoin, aliased
# outerjoin 外连接, aliased 别名

def insert():
    d1 = Department(Name='it')
    d2 = Department(Name='pc')
    d3 = Department(Name='sc')

    e1 = Employee(Name="Jack", Birthday="2020-1-1", department=d1)
    e2 = Employee(Name="Tom", Birthday="2020-1-1", department=d1)
    e3 = Employee(Name="Amy", Birthday="2020-1-1", department=d2)
    e4 = Employee(Name="Brand", Birthday="2020-1-1", department=d3)

    session = Session()
    session.add_all([e1,e2,e3,e4])
    session.commit()

def select_single_target():
    query = select(Department).order_by(Department.Name)
    session = Session()
    # session 也有和engine.connection().execute()的方法来执行构建好的sql语句, 当然也有insert批量插入方法
    results = session.execute(query)
    for result in results:
        print(result)

def select_join_target():
    # 基于relationship关联的属性来连接查询, 使用类名代表查询所有字段
    query = select(Department, Employee).join(Employee.department)
    session = Session()
    results = session.execute(query)
    for result in results:
        print(result)

def select_with_alised():
    emp_cls = aliased(Employee, name="emp") # 变量emp_cls只是方便使用，真正的别名是“emp”
    dep_cls = aliased(Department, name="dep")

    query = select(dep_cls, emp_cls).join(emp_cls.department.of_type(dep_cls))
    # emp_cls.department.of_type(dep_cls) 既然双方都有别名，一方使用别名连接另一方时也需要用别名，of_type(dep_cls) 就是在告诉，连接时连接该别名
    session = Session()
    results = session.execute(query)
    for result in results:
        print(result)

def select_field():
    query = select(Department.ID, Employee.Name).join(Employee.department, isouter=False)
    # 假设没有关联属性时，用 select_from() 关联两表的类即可
    query1 = select(Department.ID, Employee.Name).join_from(Department,Employee)
    session = Session()
    results = session.execute(query)
    for result in results:
        print(result)

def select_out_join():
    query = select(Department.ID, Employee.Name).outerjoin(Employee.department)
    # 因为join默认是 inner join交集，out join 代表两表的并集。拓展的 outjoin_from 的用法和join_from一样
    # 也可以在join参数中使用 isouter=True 也可以实现外连接

def select_select_from():
    query = select(Department.Name).select_from(outerjoin(Department,Employee))
    print(query)
    session = Session()
    results = session.execute(query)
    for result in results:
        print(result)
# select_from 用于显示指定主表，连接他表时默认left join
# query = select(Employee.name, Department.name).select_from(Employee).join(
#     Department, Employee.department_id == Department.id
# )

def select_subquery():
    subquery = select(Department).where(Department.ID==1).subquery()
    sub = select(subquery.c.Name)
    print(sub)

def batch_insert():
    data = [
        {"Name": "张三", "Birthday": "1995-03-15", "Department_id":1},
        {"Name": "李四", "Birthday": "1998-07-22", "Department_id":1},
        {"Name": "王五", "Birthday": "1992-11-30", "Department_id":2},
        {"Name": "赵六", "Birthday": "1996-05-18", "Department_id":2},
        {"Name": "孙七", "Birthday": "1994-09-12", "Department_id":3}
    ]
    session = Session()
    session.bulk_insert_mappings(Employee, data)
    session.commit()

def relate_insert_orm():
    session = Session()
    inserts = Employee.__table__.insert() # __table__属性获取类对象的表空间，这样就能调用insert()方法
    session.execute(inserts, [
        {
            "Name":"haha", 
            "Birthday":"2000-1-1",
            "Department_id":session.query(Department.ID).filter(Department.Name=='it').scalar()
        },
    ])
    session.commit()

# def batch_update_orm():
#     session = Session()
#     # updates = Employee.__table__.update()
#     session.execute(update(Employee.__table__).where(Employee.ID==1), [
#         {"Name":"kk"},
#     ])
#     session.commit()

def batch_delete_orm():
    session = Session()
    # 除了between还有，in_ 
    session.execute(delete(Employee.__table__).where(Employee.Birthday.between('1992-1-1','1994-1-1')))
    session.commit()

if __name__=='__main__':
    pass
    # insert()
    # select_single_target() 单查询
    # select_join_target() 连接查询
    # select_with_alised() 别名
    # select_field() 指定字段
    # select_select_from() 指定主表
    # select_subquery() 子查询
    # print(Session().get(Employee, 2)) 直接获取Employee类创建的表的第二条数据
    # batch_insert() 批量插入数据最好的办法
    # insert_orm() 关联关系插入
    # batch_update_orm()
    batch_delete_orm() # 批量删除


