# 单选
# QRadioButton 是一种单选按钮，同一个父级下的 QRadioButton 会被分组在一起，而且它们之间是互斥的，用户只能选择其中的一个。这种行为是通过将它们添加到同一个父级部件（通常是同一个布局或窗口）来实现的。
from PySide6.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle('radiobutton')
window.setGeometry(100, 100, 200, 200)
# 支持设置按钮并绑定窗口，直接绑定窗口时，若该窗口没有设置布局，控件将会以浮动形式放置，因此不推荐
# radio1 = QRadioButton('option 1', window)
# radio2 = QRadioButton('option 2', window)
radio1 = QRadioButton('option 1')
radio2 = QRadioButton('option 2')
# 设置一个按钮为选中状态
radio1.setChecked(True)
# 读取属性
print('radio text', radio1.text())
print('is checked', radio1.isChecked())
# 连接信号
def myprint():
    print('Radio Button 1 Toggled')
# 选中是执行的槽函数
radio1.toggled.connect(myprint)
# 设置布局
layout = QVBoxLayout(window)
layout.addWidget(radio1)
layout.addWidget(radio2)

window.show()
app.exec()

# text()：单选按钮显示的文本
# radio_button.setChecked(True)  # 设置为选中状态
# checked_state = radio_button.isChecked()  # 获取当前选中状态
# toggled：信号，当单选按钮的状态发生变化时触发。可以连接到一个槽函数来处理状态变化 radio_button.toggled.connect(my_function)