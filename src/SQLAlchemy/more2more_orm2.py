from more2more_orm1 import Session, User, Role, association_table

def insert(s):
    role1 = Role(name='Admin')
    role2 = Role(name='Guest')

    user1 = User(name='Jack',pwd='111')
    user2 = User(name='Tom',pwd='222')
    user3 = User(name='Amy',pwd='333')

    user1.roles.append(role1)
    user1.roles.append(role2)
    
    user2.roles.append(role1)
    user3.roles.append(role2)

    s.add_all([user1, user2, user3])
    s.commit()

def srh(s):
    u = s.query(User).filter(User.id == 1).one()
    print(u)
    print(u.roles)

session = Session()
# insert(session)
srh(session)
