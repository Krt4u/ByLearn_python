# 表单布局管理器，用于将标签和输入字段配对显示。适用于创建表单式的用户界面。

from PySide6.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt

app = QApplication()
widget = QWidget()

# 创建表单布局管理器
layout = QFormLayout(widget)

# 创建标签和单行文本框
label1 = QLabel('name:')
label2 = QLabel('age:')
line_edit1 = QLineEdit()
line_edit2 = QLineEdit()

# 添加标签和字段对，每一对称为布局中的一行，还有相应设列的函
layout.addRow(label1, line_edit1)
layout.addRow(label2, line_edit2)

# 田间水平和垂直间隔
layout.setHorizontalSpacing(15)
layout.setVerticalSpacing(10)

widget.show()
app.exec()