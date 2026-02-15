from PySide6.QtWidgets import QGridLayout, QBoxLayout, QLabel, QLineEdit, QWidget, QApplication, QPushButton

app = QApplication([])
widget = QWidget()
widget.setGeometry(100,100,300,200)

layout = QGridLayout(widget)

label_name = QLabel('name')
label_pwd = QLabel('pwd')
line_edit_name = QLineEdit()
line_edit_pwd = QLineEdit()
b1 = QPushButton('cmit')

layout.addWidget(label_name, 0, 0)
layout.addWidget(line_edit_name, 0, 1)
layout.addWidget(label_pwd, 1, 0)
layout.addWidget(line_edit_pwd, 1, 1)
layout.addWidget(b1, 2, 0)

## QLineEdit 常用属性和方法
# text：获取或设置文本内容
line_edit_name.text()
line_edit_name.setText('new text') # 不常用
# setPlaceholderText：占位符文本
line_edit_name.placeholderText() # 返回占位符值
line_edit_name.setPlaceholderText('enter your name') # 设置占位符值
# setMaxLength 限制最大输入
line_edit_name.setMaxLength(10)
# setReadOnly(True) 限制只读
line_edit_name.setReadOnly(True)
# setAlignment() 设置文本的对齐方式
line_edit_name.setAlignment()
# setEchoMode() 文本内容显示方式, 正常显示, 密码显示等
line_edit_name.setEchoMode(QLineEdit.Password)
# setInputMask("000-00-00") 设置输入掩码, 定义输入格式
# setClearButtonEnabled(True) 设置是有一键清除输入, 旁边有个小x



widget.show()
app.exec()