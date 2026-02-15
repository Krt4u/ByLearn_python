from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QAction

class ToolbarExample(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建主窗口和布局
        self.setWindowTitle("Toolbar Example")

        # 创建工具栏
        self.toolbar = QToolBar("Main Toolbar")

        # 添加工具按钮
        action_open = QAction("Open", self)
        action_save = QAction("Save", self)
        action_cut = QAction("Cut", self)
        action_copy = QAction("Copy", self)
        action_paste = QAction("Paste", self)

        # 将按钮添加到工具栏
        self.toolbar.addAction(action_open)
        self.toolbar.addAction(action_save)
        self.toolbar.addSeparator()  # 添加分隔符
        self.toolbar.addAction(action_cut)
        self.toolbar.addAction(action_copy)
        self.toolbar.addAction(action_paste)

        # 将工具栏添加到主窗口
        self.addToolBar(self.toolbar) # 注意 toolbar 不是 widget 类


if __name__ == "__main__":
    app = QApplication([])

    example = ToolbarExample()
    example.show()

    app.exec()

# window > toolbar > qaction

'''
关键的 QToolBar 方法和属性包括：
addAction(action): 向工具栏添加一个操作按钮。
addSeparator(): 向工具栏添加一个分隔符。
addWidget(widget): 向工具栏添加自定义的小部件。
setIconSize(size): 设置工具栏上图标的大小。
setToolButtonStyle(style): 设置工具栏按钮的样式，如图标在文字上方、下方、只显示图标等。
'''