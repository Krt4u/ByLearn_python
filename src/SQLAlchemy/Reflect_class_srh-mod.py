# 映射类的查询与修改
from Reflect_class_insert import engine, Session, Person, Base

def srh():
    # 查询所有记录 result = session.query(classname).all()
    session = Session()
    result_all = session.query(Person).all() # 返回映射对象集合
    for person in result_all:
        print(person.id, person.name, person.birthday)

    # 条件查询 result = session.query(classname).filter(classname.id == 1)
    result_filter = session.query(Person).filter(Person.name == 'kangkang')
    for person in result_filter:
        print(person.id, person.name, person.birthday)

    # 单条记录查询的返回，直接返回记录，而非结果集合
    # first() 返回第一条记录
    result = session.query(Person).filter(Person.name == 'kangkang').first()
    print(result.id, result.name, result.birthday)
    # one() 针对返回的结果集只有一条记录(不能空)，否则报错
    result = session.query(Person).filter(Person.name == 'kangkang').one()
    print(result.id, result.name, result.birthday)
    # scalar() 与 one() 一致，只是多可以返回无查询结果的记录(可为空)
    result = session.query(Person).filter(Person.name == 'kangkang').scalar()
    print(result.id, result.name, result.birthday)
# 查询
srh()

def mod():
    # 单记录修改
    session = Session()
    # result = session.query(Person).filter(Person.name == 'kangkang').one()
    # # 直接获取记录修改, commit, 该方式修改需要在事务之间, 否则无法修改
    # result.name = "tiantian"
    # print(result.id, result.name, result.birthday)
    # session.commit()
    # 查询更新, 执行批量修改只需要修改查询条件, 因此此方法更常用
    session.query(Person).filter(Person.name == "kangkang").update({Person.name: "tiantian"})
    session.commit()


# 修改
mod()