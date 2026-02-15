from sqlalchemy import create_engine, ForeignKey, String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column,Session
from typing_extensions import Annotated
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QListWidget,QListWidgetItem, QPushButton

engine = create_engine('mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb', echo=False)
Base = declarative_base()

id_int = Annotated[int, mapped_column(primary_key=True)]
name_str = Annotated[str, mapped_column(String(128), nullable=False)]

class Test(Base):
    __tablename__ = 'test'

    id:Mapped[id_int]
    name:Mapped[name_str]

    def __repr__(self):
        return f"{self.id}, {self.name}"
    
Base.metadata.create_all(engine)

def insert():
    ps = [
        Test(name="kangkang"),
        Test(name="jiahao")
    ]
    with Session(engine) as session, session.begin():
        session.add_all(ps)

def srh():
    with Session(engine) as session, session.begin():
        results = session.query(Test).all()
        return results




class ui(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 500, 300)
        self.layout:QVBoxLayout = QVBoxLayout(self)
        self.list = QListWidget()

        self.btn = QPushButton('add')

        self.btn.clicked.connect(self.additem)

        self.init_ui()

    def init_ui(self):
        self.layout.addWidget(self.list)
        self.layout.addWidget(self.btn)


    def additem(self):
        texts = srh()
        for r in texts:
            item = QListWidgetItem(str(r))
            self.list.addItem(item)



if __name__ == '__main__':
    app = QApplication([])
    T = ui()
    T.show()
    app.exec()