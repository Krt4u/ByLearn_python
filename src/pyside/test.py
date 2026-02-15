from sqlalchemy import create_engine, MetaData,Column,Table
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

engine = create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb")
# ORM 对象，直接打印或访问属性，注意automap只会映射基础结构而没有repr方法
Base = automap_base()
Base.prepare(engine, reflect=True)  # 自动映射所有表为 ORM 类，以键值形式, 是一个类字典，类名str：类cls
# table = Base.classes[tablename] 获取特定表对象
# table = Base.classes.tablename 获取的是该表的类 如orm继承decri_base继承的类创建
# tb = table.__table__ # 获取对应的表，一个真正的表而不是类来自core，有行列等数据，是sqlalchemy的Table对象

# Base.classes 包含映射后的类，键是表名，值是类名
mapped_classes = {name: cls for name, cls in Base.classes.items()}

app = QApplication([])
window = QWidget()
window.setGeometry(100, 100, 400, 300)
layout = QVBoxLayout(window)

def get_table_data_by_class(cls):
    with Session(engine) as session:
        return session.query(cls).all()
    
def show_data_for_class(class_name):
    cls = mapped_classes.get(class_name) # 通过类名获取表类对象orm
    if cls is None:
        print("找不到映射类：", class_name)
        return
    # rows = get_table_data_by_class(cls)
    # table:Table = cls.__table__ # 获取表对象core
    # cols_name = [col.name for col in table.columns] # 获取表的字段名，注意遍历出来的col是Column对象，需要调用name获取name，以后都要注意，看类型是否正确在继续
    # 更优雅的方法
    cols_name = cls.__table__.columns.keys() # 对应字段名
    # cols_v = cls.__table__.columns.values() # 对应字段类
    results = get_table_data_by_class(cls) # 返回对应的行数据，每条行都是一个对象
    for result in results:
        row = {col: getattr(result, col) for col in cols_name} 
        # getattr(result, col) 动态获取字段，因为你不能使用 col.result python不会把result当成变量而是col的一个属性，使用了getattr方法，可以让result和col都在动态变换
        print(row)


# 创建按钮（使用映射类的键作为按钮文本）
for class_name in mapped_classes.keys():
    btn = QPushButton(class_name)
    layout.addWidget(btn)
    btn.clicked.connect(lambda checked, cn=class_name: show_data_for_class(cn))

window.show()
app.exec()




# 代码	得到的是什么
# Base.classes	automap 的“类字典”，存 ORM 类
# Base.classes.department	ORM 类（自动生成）
# Dept.__table__	Table 对象（表结构）
# Dept.__table__.columns	列对象（字段）
# 表达式	类型	含义
# Base.classes	特殊容器（类似 dict）	存 ORM 类
# Base.classes.keys()	列表	映射类名（通常是表名）
# Base.classes.department	ORM 类	自动生成的类
# Dept.__table__	Table 对象	表结构
# Dept()	ORM 实例	一行数据（对象）
