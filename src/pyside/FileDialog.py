# QFileDialog 是 Qt 中用于显示文件对话框的部件，允许用户选择文件或目录。

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog

class FileDialogExample(QWidget):
    def __init__(self):
        super().__init__()

        # 创建主布局和子部件
        self.layout = QVBoxLayout(self)
        self.open_button = QPushButton("Open File Dialog")

        # 将子部件添加到主布局
        self.layout.addWidget(self.open_button)

        # 连接按钮的点击信号到槽函数
        self.open_button.clicked.connect(self.show_file_dialog)

    def show_file_dialog(self):
        # 创建文件对话框
        file_dialog = QFileDialog(self)

        # 设置文件对话框的标题
        file_dialog.setWindowTitle("Choose a File")

        # 设置对话框模式为打开文件
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        # 显示文件对话框，并获取用户选择的文件路径
        selected_file, _ = file_dialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")

        # 如果用户选择了文件，将文件路径输出到控制台
        if selected_file:
            print(f"Selected file: {selected_file}")


if __name__ == "__main__":
    app = QApplication([])

    example = FileDialogExample()
    example.show()

    app.exec()

'''
关键的 QFileDialog 方法和属性包括：
getOpenFileName(parent, caption, directory, filter): 打开文件对话框，返回用户选择的文件路径和文件过滤器。
getOpenFileNames(parent, caption, directory, filter): 打开文件对话框，允许用户选择多个文件，返回文件路径列表和文件过滤器。
getExistingDirectory(parent, caption, directory): 打开目录对话框，返回用户选择的目录路径。
getSaveFileName(parent, caption, directory, filter): 打开保存文件对话框，返回用户选择的文件路径和文件过滤器。
'''