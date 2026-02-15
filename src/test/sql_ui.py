from sqlalchemy import create_engine, ForeignKey, String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column,Session
from typing_extensions import Annotated
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QListWidget,QListWidgetItem, QPushButton, QHBoxLayout,QLineEdit, QInputDialog, QMessageBox

engine = create_engine('mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb', echo=False)
Base = declarative_base()

id_int = Annotated[int, mapped_column(primary_key=True)]
name_str = Annotated[str, mapped_column(String(128), nullable=False)]

class Test(Base):
    __tablename__ = 'test'

    id:Mapped[id_int]
    name:Mapped[name_str] = mapped_column(unique=True)

    def __repr__(self):
        return f"{self.id},{self.name}"
    
Base.metadata.create_all(engine)

def insert(_name):
    t = Test(name=_name)
    with Session(engine) as session, session.begin():
        session.add(t)

def is_name(_name):
    with Session(engine) as session:
        if session.query(Test).filter(Test.name == _name).count(): # 查询返回对象，无论是否存在，因此需要用count来判断，而不是直接查询的结果
            return True
    return False


def delete(_name):
    with Session(engine) as session, session.begin():
        obj = session.query(Test).filter(Test.name == _name).one()
        session.delete(obj)


def srh():
    with Session(engine) as session:
        results = session.query(Test).all()
        for r in results:
            _ = r.id        # 事先访问一遍数据，防止懒加载和DetachedInstanceError问题,也有其他方法
            _ = r.name
        return results


class ui(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 300)
        self.layout:QVBoxLayout = QVBoxLayout(self)
        self.list = QListWidget()
        self.btn_add = QPushButton('add')
        self.btn_flush = QPushButton('flush')
        
        self.input_text = QLineEdit()

        self.input_text.setPlaceholderText('enter text')
        self.btn_add.clicked.connect(self.add_data)
        self.btn_flush.clicked.connect(self.flush)

        self.init_ui()
        self.load_data()

    def init_ui(self):
        self.layout.addWidget(self.list)
        self.layout.addWidget(self.input_text)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.btn_flush)

    def load_data(self):    # 从数据库中加载数据并添加进入list
        contents = srh()
        for line in contents:
            self.additem(line)

    def add_data(self):     # 自定义添加数据
        name = self.input_text.text()

        if name.strip():
            if self.list.count()> 0:
                widget = self.list.itemWidget(self.list.item(self.list.count()-1))  # 获取最后一个item的widget
                label = widget.findChild(QLabel)
                id = label.text().split(',')[0].strip()     # 获取其id
            else:
                id = 0

            if  not is_name(name):  # 先判断是否同名
                self.additem(f"{int(id)+1},{name}")
                insert(name)    # 添加进入数据库
        self.input_text.clear()

    def flush(self):
        if self.list.count() > 0:
            self.list.clear()
            self.load_data()    # 刷新输出


    def additem(self, text):    # listItem 的添加函数
        widget = QWidget(self.list)
        layout = QHBoxLayout(widget)
        label = QLabel(str(text))
        btn_del = QPushButton('X')
        btn_mod = QPushButton('O')

        # 点击按钮时先选中该项
        btn_del.clicked.connect(lambda:self.list.setCurrentItem(item))
        btn_mod.clicked.connect(lambda:self.list.setCurrentItem(item))

        # 绑定槽函数
        btn_del.clicked.connect(self.remove_data)
        btn_mod.clicked.connect(self.mod_data)

        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(btn_del)
        layout.addWidget(btn_mod)
        layout.setContentsMargins(5,2,1,2)

        item = QListWidgetItem()
        self.list.addItem(item)
        self.list.setItemWidget(item, widget)

    # 删除item
    def remove_data(self):
        if self.ask_() == QMessageBox.Yes:
            item = self.list.currentItem()
            widget = self.list.itemWidget(item)
            label = widget.findChild(QLabel)
            name = label.text().split(',')[1].strip()
            delete(name)
            self.list.takeItem(self.list.row(item))
        else:
            return

    # 修改item - 未能同步到数据库
    def mod_data(self):
        item = self.list.currentItem()
        widget = self.list.itemWidget(item)
        label = widget.findChild(QLabel)
        text,ok = QInputDialog.getText(self, "modify", 'text', text=label.text())
        if text.strip() and ok:
            label.setText(text)

    # 如何解决数据库主键自增的跨度问题？或者先搞一下登录界面，或者改成本地存储？数据库乱序
         

    def ask_(self):
        result = QMessageBox.question(self, "question","do you want to del?", QMessageBox.Yes | QMessageBox.No)
        return result

            
if __name__ == '__main__':
    app = QApplication([])
    T = ui()
    T.show()
    app.exec()
