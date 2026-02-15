# QInputDialog 对话框类，用于访问不同的接口函数，能够较为便捷的获取用户输入
from PySide6.QtWidgets import QApplication, QWidget, QInputDialog, QLabel, QPushButton, QHBoxLayout

class inputdialog(QWidget):
    def __init__(self):
        super().__init__()

        # 添加控件
        self.layout:QHBoxLayout = QHBoxLayout(self)
        self.setGeometry(100, 100, 300, 300)
        self.label = QLabel()
        self.btn_edit = QPushButton('edit')
        self.btn_cls = QPushButton('clear')
        self.container = '内容：'
        # 配置控件
        self.label.setText(self.container)
        # 绑定槽函数
        self.btn_edit.clicked.connect(self.edit)
        self.btn_cls.clicked.connect(self.clear_text)

        self.init_ui()
        
    def init_ui(self):
        # 布局控件
        self.layout.addWidget(self.label)
        self.layout.addStretch()
        self.layout.addWidget(self.btn_edit)
        self.layout.addWidget(self.btn_cls)

    def edit(self):
        txt = self.label.text().strip(self.container)
        text,ok = QInputDialog.getText(self, 'change', 'text', text=txt)
        if ok and text:
            self.label.setText(self.container+text)

    def clear_text(self):
        self.label.setText(self.container)

if __name__ == '__main__':
    app = QApplication([])

    t = inputdialog()
    t.show()

    app.exec()

