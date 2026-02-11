from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout

app = QApplication([])
# 初始化一个窗口
widget = QWidget()
# 设置基础窗口的大小
widget.setGeometry(300,300,400,200)

# 父类传参，作为其子类内容，QHBoxLayout，水平布局管理器
Hlayout = QHBoxLayout(widget)
# QVBoxLayout 垂直布局管理器
# Vlayout = QVBoxLayout(widget)

# 定义连个按钮
b1 = QPushButton('button1')
b2 = QPushButton("button2")

# addWidget 添加组件方法
Hlayout.addWidget(b1)
Hlayout.addWidget(b2)
# Vlayout.addWidget(b1)
# Vlayout.addWidget(b2)

widget.show()
app.exec()