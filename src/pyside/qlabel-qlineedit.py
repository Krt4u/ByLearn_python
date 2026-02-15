# QLabel用于显示文本或图像的标签。QLineEdit用于单行文本输入框，用于接受用户的文本输入

from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QWidget, QHBoxLayout, QGridLayout, QPushButton

app = QApplication([])
# 创建父窗口
widget = QWidget()
# 设置父窗口大小
widget.setGeometry(100, 100, 300, 200)
# 创建网格布局
layout = QGridLayout(widget)
# 创建控件
label1 = QLabel('name')
label2 = QLabel('passwd')
line_edit1 = QLineEdit()
line_edit2 = QLineEdit()
b1 = QPushButton('cmit')
# 放置控件
layout.addWidget(label1, 0, 0)
layout.addWidget(label2, 1, 0)
layout.addWidget(line_edit1, 0, 1)
layout.addWidget(line_edit2, 1, 1)
layout.addWidget(b1, 2, 0)

b1.clicked.connect(lambda:print(line_edit1.text()))


widget.show() # 显示窗口
app.exec() # 进入程序事件循环