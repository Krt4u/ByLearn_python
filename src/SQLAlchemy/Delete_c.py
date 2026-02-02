import sqlalchemy

engine = sqlalchemy.create_engine(
    'mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb', 
    echo=False
    )
person = sqlalchemy.Table('person', sqlalchemy.MetaData(), autoload_with=engine)

# 删除行 delete from person where id = 6
#   -> person.delete().where(person.c.id == 6)

with engine.connect() as conn:
    delete_query = person.delete().where(person.c.id == 6)
    conn.execute(delete_query)
    conn.commit()