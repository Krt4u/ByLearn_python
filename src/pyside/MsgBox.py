# QMessageBox：消息框，用于显示提示、警告和错误消息。

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox


class MessageBoxExample(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建主窗口
        self.setWindowTitle("MessageBox Example")

        # 创建按钮
        self.show_info_button = QPushButton("Show Info Message")
        self.show_warning_button = QPushButton("Show Warning Message")
        self.ask_question_button = QPushButton("Ask Question")

        # 创建垂直布局
        layout = QVBoxLayout()

        # 将按钮添加到垂直布局
        layout.addWidget(self.show_info_button)
        layout.addWidget(self.show_warning_button)
        layout.addWidget(self.ask_question_button)

        # 将布局设置为主窗口的中央部分
        central_widget = QWidget()
        central_widget.setLayout(layout) # 将该容器的内容设置为垂直布局
        self.setCentralWidget(central_widget) # 将该容器设置为中心布局到主窗口

        # 连接按钮的点击信号到槽函数
        self.show_info_button.clicked.connect(self.show_info_message)
        self.show_warning_button.clicked.connect(self.show_warning_message)
        self.ask_question_button.clicked.connect(self.ask_question)

    def show_info_message(self):
        # 创建信息消息框
        QMessageBox.information(self, "Info", "This is an information message.")

    def show_warning_message(self):
        # 创建警告消息框
        QMessageBox.warning(self, "Warning", "This is a warning message.")

    def ask_question(self):
        # 创建询问消息框
        result = QMessageBox.question(self, "Question", "Do you want to proceed?", QMessageBox.Yes | QMessageBox.No)

        if result == QMessageBox.Yes:
            print("User clicked Yes.")
        else:
            print("User clicked No.")


if __name__ == "__main__":
    app = QApplication([])

    example = MessageBoxExample()
    example.show()

    app.exec()

'''
关键的 QMessageBox 静态方法包括：
information(parent, title, text, buttons, defaultButton): 显示信息消息框。
warning(parent, title, text, buttons, defaultButton): 显示警告消息框。
question(parent, title, text, buttons, defaultButton): 显示询问消息框，返回用户的选择。
'''