from PySide6.QtWidgets import (
    QApplication, QWidget, QListWidget, QVBoxLayout,
    QPushButton, QLineEdit, QListWidgetItem, QLabel, QHBoxLayout,
    QInputDialog
)

class myListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self) # 主控件是竖直
        self.list_widget = QListWidget()
        self.input_text = QLineEdit()
        self.add_btn = QPushButton('Add Item')

        self.input_text.setPlaceholderText('Enter text to add')
        self.layout.addWidget(self.list_widget)
        self.layout.addWidget(self.input_text)
        self.layout.addWidget(self.add_btn)

        self.add_btn.clicked.connect(self.add_item)

    def add_item(self):
        text = self.input_text.text().strip()
        if not text:
            self.input_text.clear()
            return

        # 创建列表项和自定义部件
        item = QListWidgetItem()
        widget = QWidget() # 用来存放布局
        layout = QHBoxLayout(widget)
        label = QLabel(text)
        btn = QPushButton("X")
        btn_edit = QPushButton('O')
        # 固定控件宽度
        btn_edit.setFixedWidth(30)
        btn.setFixedWidth(30)

        # 点击按钮时删除对应的列表项
        btn.clicked.connect(lambda: self.remove_item(item))
        btn_edit.clicked.connect(lambda: self.edit_item(item))
        
        layout.addWidget(label)
        layout.addStretch()  # 推动按钮靠右, 相当于添加一个弹簧在前面这个控件后
        layout.addWidget(btn) # btn前面有一个弹簧，被推倒了最右边
        layout.addWidget(btn_edit)
        layout.setContentsMargins(5, 2, 1, 2) # 设置 margin 值
        widget.setLayout(layout) # 相当于把水平布局放进这个容器，再把这个容器放进主框架的竖直里
        # 一定要在该函数 add_item 设置，这样就是在编辑item而不影响主框架

        self.list_widget.addItem(item)
        self.list_widget.setItemWidget(item, widget) # btn+label > widget(QHBoxLayout) > item > list
        self.list_widget.setCurrentItem(item) # 添加完后，选中该项
        self.input_text.clear()

    def edit_item(self, item):
        widget = self.list_widget.itemWidget(item) # 获取传入项中的容器
        label = widget.findChild(QLabel)    # 查找容器中的label控件
        if label:
            current_text = label.text()
            new_text, ok = QInputDialog.getText(self, "编辑项目", "修改文本：", text=current_text) # gettext 返回输入框的内容和是否点击了ok的元组
            if ok and new_text.strip():
                label.setText(new_text.strip())


    def remove_item(self, item):
        row = self.list_widget.row(item)
        self.list_widget.takeItem(row)


if __name__ == '__main__':
    app = QApplication([])
    window = myListWidget()
    window.show()
    app.exec()
