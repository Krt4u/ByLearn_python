# QTreeWidget 是 Qt 中用于显示树形结构的部件，通常用于展示层次化的数据

from PySide6.QtWidgets import QApplication, QWidget, QTreeWidget, QVBoxLayout, QPushButton,QTreeWidgetItem

class treeWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 创建控件
        self.layout:QVBoxLayout = QVBoxLayout(self)
        self.treewidget = QTreeWidget()
        self.add_btn = QPushButton('add item')
        # 添加控件
        self.layout.addWidget(self.treewidget)
        self.layout.addWidget(self.add_btn)
        # 设置树形控件列数
        self.treewidget.setColumnCount(2)
        # 添加树形部件的列标签
        self.treewidget.setHeaderLabels(["name", "value"])
        # 连接按钮的点击信号到槽函数
        self.add_btn.clicked.connect(self.add_item)

    def add_item(self):
        # 创建顶层节点
        top_item = QTreeWidgetItem(self.treewidget) # 直接继承树形控件
        top_item.setText(0, "Top Item")
        top_item.setText(1, "Value 1")

        # 创建顶层节点的子节点
        chlid_item = QTreeWidgetItem(top_item)  # 如果是子节点，需要继承顶层节点
        chlid_item.setText(0, "child item")
        chlid_item.setText(1, "value 2")

        # 是否展开
        top_item.setExpanded(True)

if __name__ == '__main__':
    app = QApplication([])

    t = treeWidget()
    t.show()

    app.exec()


# 关键的 QTreeWidget 方法和属性包括：
# setColumnCount(count): 设置树形部件的列数。
# setHeaderLabels(labels): 设置树形部件的列标签。
# addTopLevelItem(item): 添加顶层节点。
# setExpanded(expand): 设置节点的展开状态。