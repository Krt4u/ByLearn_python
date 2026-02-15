from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QStackedLayout, QLineEdit, QFormLayout

app = QApplication([])
widget = QWidget()

# 创建堆叠管理器
stacked_layout = QStackedLayout()
widget.setLayout(stacked_layout)  # 将堆叠布局设置给窗口

b1 = QPushButton('点击登录')

# 需要创建一个QWidget作为表单的容器
form_widget = QWidget()
form_layout = QFormLayout(form_widget)  # 将表单布局设置给容器
label = QLabel('用户名:')
line_edit = QLineEdit()
form_layout.addRow(label, line_edit)

# 组件添加到管理器中
stacked_layout.addWidget(b1)
stacked_layout.addWidget(form_widget)  # 添加容器，而不是布局

# 设置初始显示索引为0的组件
stacked_layout.setCurrentIndex(0)

# 给按钮添加点击事件
b1.clicked.connect(lambda: stacked_layout.setCurrentIndex(1))

widget.show()
app.exec()