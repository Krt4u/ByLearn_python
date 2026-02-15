# QListWidget 是 Qt 中用于显示列表的部件，它允许用户显示和选择项目，列表部件的内容是 item 对象是 QListWidgetItem. list的内容必须是item，item的内容必须是widget，widget可以有控件和布局要求不高
from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidgetItem, QInputDialog

class myListWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 添加控件
        self.layout:QVBoxLayout = QVBoxLayout(self)
        self.list_widget = QListWidget()
        self.add_btn = QPushButton('add item')
        self.remove_btn = QPushButton('remove item')
        self.clear_btn = QPushButton('clear item')
        self.input_text = QLineEdit()
        # 配置配置控件
        # self.add_btn.setShortcut('Ctrl+C')
        self.input_text.setPlaceholderText('Enter text to add')
        # 添加控件到布局
        self.layout.addWidget(self.list_widget)
        self.layout.addWidget(self.input_text)
        self.layout.addWidget(self.add_btn)
        self.layout.addWidget(self.remove_btn)
        self.layout.addWidget(self.clear_btn)
        # 按钮绑定槽函数
        self.add_btn.clicked.connect(self.add_item)
        self.remove_btn.clicked.connect(self.remove_selected_item)
        self.clear_btn.clicked.connect(self.clear_all)
        # 列表部件点击内容的item是的槽函数
        self.list_widget.itemClicked.connect(self.item_clicked)

    # 添加内容
    def add_item(self):
        text = self.input_text.text().strip() # 清除开头结尾空格，并获取内容
        if text:
            item = QListWidgetItem(text)
            self.list_widget.addItem(item)  # 如果内容存在，则向列表部件添加item
        self.input_text.clear()         # 添加完以后，清除输入框内容

    # 移除列表部件中选中的item
    def remove_selected_item(self):
        select_item = self.list_widget.currentItem()    # 获取当前的item
        if select_item:
            self.list_widget.takeItem(self.list_widget.row(select_item))
            # self.list_widget.row(select_item) 意为获取当前选中item的行号(索引)，takeItem(index) 从列表中移除指定的项，只是移除，并不会自动将其删除
            del select_item # 删除移除的项

    # 清除列表部件的所有item
    def clear_all(self):
        self.list_widget.clear()

    # item被点击时执行的槽函数
    def item_clicked(self, item):
        print(f"clicked on item: {item.text()}")

if __name__ =='__main__':
    app = QApplication([])
    example = myListWidget()
    example.show()
    app.exec()


# 关键的 QListWidget 方法和属性包括：
# addItem(item): 将项目添加到列表。
# insertItem(index, item): 在指定位置插入项目。
# takeItem(index): 从列表中移除指定位置的项目。
# clear(): 移除所有项目。
# count(): 返回列表中的项目数。
# currentItem(): 返回当前选中的项目。
# setCurrentItem(item): 设置当前选中的项目。
# CurrentItem() 获取当前选中的项目
# item(index): 返回指定位置的项目。
# itemAt(x, y): 返回给定坐标处的项目。
# selectedItems(): 返回当前选中的所有项目。
# setSelectionMode(mode): 设置选择模式。
# QListWidgetItem 默认是来显示纯文本
# QListWidget.setItemWidget() 方法，替换成你自定义的控件 用法QListWidget.setItemWidget(QListWidgetItem(), 你的控件) 注意必须创建一个item容器QListWidgetItem()并添加进list 来存放你的控件, 相当于把你的控件方进这个item盒子里，然后itme再放进list中
# itemWidget(item) 获取item容器中的控件，与上面叙述关联
# 例子
# widget = self.list_widget.itemWidget(item)  获取item容器中的控件，不只有一个
# label = widget.findChild(QLabel)  在获取的控件中查找指定控件