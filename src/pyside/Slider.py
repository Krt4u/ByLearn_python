# QSlider 是 Qt 中用于选择范围值的部件，通常用于允许用户通过拖动滑块来选择数值。

from PySide6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class MyQSlider(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,300,300)
        self.setWindowTitle('QSlider')
        self.layout:QVBoxLayout = QVBoxLayout(self)
        
        self.init_ui()

    def init_ui(self):
        self.hslidef = QSlider(Qt.Horizontal) # 水平滑块
        self.hslidef.setRange(0, 100)
        self.hslidef.setValue(50)
        self.hslidef.setSingleStep(1)

        self.vslidef = QSlider(Qt.Vertical) # 水平滑块
        self.vslidef.setRange(0, 100)
        self.vslidef.setValue(50)
        self.vslidef.setSingleStep(1)

        self.hlabel = QLabel('Horizontal Slider Value: ')
        self.vlabel = QLabel("Vertical Slider Value: ")

        self.hslidef.valueChanged.connect(lambda value: self.hlabel.setText(f"Horizontal Slider Value: {value}"))
        self.vslidef.valueChanged.connect(lambda value: self.vlabel.setText(f"Vertical Slider Value: {value}"))

        self.layout.addWidget(self.hslidef)
        self.layout.addWidget(self.hlabel)
        self.layout.addWidget(self.vslidef)
        self.layout.addWidget(self.vlabel)

if __name__ =='__main__':
    app = QApplication([])
    window = MyQSlider()
    window.show()
    app.exec()

# 关键的 QSlider 方法和属性包括：

# setRange(min, max): 设置滑块的范围。
# setValue(value): 设置滑块的当前值。
# setSingleStep(step): 设置每次单步增减的数值。
# value(): 获取当前的滑块值。
# valueChanged.connect(slot): 连接数值变化的信号。