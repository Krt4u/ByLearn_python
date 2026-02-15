from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QLabel, QTextEdit

class TabWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 创建控件和主布局
        self.layout:QVBoxLayout = QVBoxLayout(self)
        self.tab_widget:QTabWidget = QTabWidget()
        # 创建两个标签下的容器
        tab1 = QWidget()
        tab2 = QWidget()
        # 创建两个控件
        label_tab1 = QLabel('this is tab1')
        label_tab2 = QLabel('this is tab2')

        # 两个控件分别放入两个tab容器
        tab1_layout = QVBoxLayout(tab1)     # qv 布局继承 tab1
        tab1_layout.addWidget(label_tab1)   # 添加控件
        tab2_layout = QVBoxLayout(tab2)     # qv 布局继承 tab2
        tab2_layout.addWidget(label_tab2)

        self.tab_widget.addTab(tab1, "TAB 1")   # tabwidget 添加 tab
        self.tab_widget.addTab(tab2, "TAB 2")

        self.layout.addWidget(self.tab_widget)

if __name__ == '__main__':
    app = QApplication([])

    t = TabWidget()
    t.show()

    app.exec()

# 关键的 QTabWidget 方法和属性包括：
# addTab(widget, label): 向 QTabWidget 添加一个选项卡，参数为选项卡中的子部件和选项卡的标签。
# removeTab(index): 移除指定索引的选项卡。
# setCurrentIndex(index): 设置当前显示的选项卡。
# currentIndex(): 获取当前显示的选项卡的索引。

# TabWidget > QWidget > 布局 > 控件