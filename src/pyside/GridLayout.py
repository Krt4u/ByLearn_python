# 网格布局管理器
# 网格布局管理器，用于将子组件放置在一个网格中。每个子组件可以占据一个或多个网格单元。这个管理器相当于把窗口划分成多个网格，就像excel表格那样，每个格子可以放一个子组件。
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit
from PySide6.QtCore import Qt

app = QApplication([])

widget = QWidget()

layout = QGridLayout(widget)

b1 = QPushButton('b1')
b2 = QPushButton('b3')
b3 = QPushButton('b3')
# 设置网格占比
layout.addWidget(b1, 0, 0)
layout.addWidget(b2, 0, 1)
layout.addWidget(b3, 1, 0, 1, 2)
# 控件的间隔
layout.setSpacing(10)
# 设置组件在管理器中的对齐方式
layout.setAlignment(b1, Qt.AlignTop | Qt.AlignLeft)
# 水平对齐标志（Qt.AlignmentFlag）：
# Qt.AlignLeft：左对齐
# Qt.AlignRight：右对齐
# Qt.AlignHCenter：水平居中
# Qt.AlignJustify：两端对齐（在水平方向上拉伸以填充网格单元）
# 垂直对齐标志（Qt.AlignmentFlag）：
# Qt.AlignTop：顶部对齐
# Qt.AlignBottom：底部对齐
# Qt.AlignVCenter：垂直居中

# 设置组件的拉伸因子，用于缩放窗口时，组件等比例变化
layout.setRowStretch(0, 1) # 第一个参数是行，第二个是控制空间的分配比例
layout.setColumnStretch(1, 1)

widget.show()
app.exec()