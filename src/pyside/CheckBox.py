from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox

app = QApplication([])
window = QWidget()
window.setWindowTitle('QCheckBox')
window.setGeometry(100, 100, 200, 200)

# 创建一个复选框
checkbox = QCheckBox('check box')

# 在布局QVBoxLayout中添加一个checkbox并放入window
QVBoxLayout(window).addWidget(checkbox)

# isChecked()：返回一个布尔值，表示复选框的当前状态是否被选中
# setChecked(bool)：设置复选框的选中状态
# stateChanged：槽函数，与按钮的触发函数类似。当复选框的状态发生变化时触发。可以连接到一个槽函数来处理状态变化
# text：复选框显示的文本
# isChecked：读写属性，表示复选框的当前状态。可以用于获取或设置复选框是否被选中

window.show()
app.exec()