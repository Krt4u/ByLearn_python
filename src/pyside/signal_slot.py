from PySide6.QtWidgets import QApplication, QPushButton

def on_button_clicked():
    print("按钮被点击了！")

app = QApplication([])
button = QPushButton("点击我")
button.clicked.connect(on_button_clicked)
# clicked 是信号，当按钮被点击时发送
# connect 是当发送信号时，连接/执行的函数
button.show()
app.exec()
