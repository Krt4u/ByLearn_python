# QComboBox下拉框，用于列表选择

from PySide6.QtWidgets import QComboBox, QLabel, QApplication, QWidget, QVBoxLayout, QLabel

app = QApplication([])
window = QWidget()
window.setWindowTitle('QComboBox') # 设置窗口标题
window.setGeometry(100,100,200,200)
layout = QVBoxLayout()

# 创建标签
label = QLabel('choose one:')
# 添加下拉控件
combobox =  QComboBox()
# 添加下拉选项, addItems([])，添加多个，参数是一个迭代器
combobox.addItem("choose 1")
combobox.addItem("choose 2")
combobox.addItem("choose 3")

layout.addWidget(label)
layout.addWidget(combobox)

# 控件->容器->窗口
window.setLayout(layout) # 直接将布局容器设置为主窗口的布局

def on_combobox_changed(index):
    select_text = combobox.currentText() # 获取当前文本内容
    label.setText(f"your choose is {select_text}") # 设置标签文本

# 下拉选项的索引改变(选择其他选项时)，绑定的槽函数
combobox.currentIndexChanged.connect(on_combobox_changed)

# 清除下拉框中的所有项 clear()
# 获取当前文本 currentText()
# 获取当前选中项的索引 currentIndex()
# 设置当前选中项的索引 setCurrentIndex(int)
# 连接选项改变时的槽函数 currentIndexChanged.connect(slot_function)
# 连接激活事件到槽函数 激活事件在用户选择项并按下回车键时触发。activated.connect(slot_function)
# 获取下拉框中的项数 count()
# 在指定索引位置插入一个文本项 insertItem(index: int, text: str)

window.show()
app.exec()
