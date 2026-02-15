# QTextEdit多行文本输入框，用于接受用户的多行文本输入
from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QApplication

app = QApplication([])
window = QWidget()

text_edit = QTextEdit()

QVBoxLayout(window).addWidget(text_edit)

# 剪切，复制和粘贴
text_edit.cut()
text_edit.copy()
text_edit.paste()

window.show()
app.exec()

