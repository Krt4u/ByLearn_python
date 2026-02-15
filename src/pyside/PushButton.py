from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout

app = QApplication([])
widget = QWidget()
layout = QVBoxLayout(widget)
button = QPushButton('按钮')
layout.addWidget(button)

# 设置按钮图标
button.setIcon('url')
# 设置按钮状态
button.setEnabled(bool)
# 设置按钮快捷键
button.setShortcut('Ctrl+C')
# 连接按钮的点击事件到槽函数
button.clicked.connect(function)
# 设置按钮样式
button.setStyleSheet('QPushButton { background-color: red; }')
# 设置按住是否重复多次执行按钮功能
button.setAutoRepeat(bool)
button.setAutoRepeatDelay(200) # 按住重复间隔

widget.show()
app.exec()
