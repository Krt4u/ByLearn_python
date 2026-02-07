from one2one1 import E, C, Session

def insert(s):
    c1 = C(name="c1")
    c2 = C(name="c2")
    c3 = C(name="c3")

    e1 = E(name="e1", cx=c1) # 通过关联属性来创建关联，所有通过属性关联的表都需要属性来打印，而不是外键
    e2 = E(name="e2", cx=c2) # 注意需要是外键关联属性 = 主键，是主键约束外键，不能反过来
    e3 = E(name="e3", cx=c3)

    s.add_all([e1,e2,e3])
    s.commit()

def select(s):
    e = s.query(E).filter(E.id==1).one()
    if e:
        print(e)
        print(e.cx) # 查询e关联c的属性

def update_1(s):
    s.query(E).filter(E.id==1).update({E.c_id: None}) # 这里使用Core的方法，只能使用字段而非属性
    s.commit()
def update_2(s):
    c = s.query(C).filter(C.id == 3).scalar() # 查询主键id为3的数据
    e = s.query(E).filter(E.id == 1).scalar() # 查询子键id为3的员工
    if c and e:
        print("yes")
        e.cx = c        # 通过关联属性约束子键的值
        s.commit()


session = Session()
# insert(session)
# select(session)
# update_1(session)
# update_2(session)



