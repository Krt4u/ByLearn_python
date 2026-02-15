# QSpinBox 是是一个限制选择框,接收整型范围 QDoubleSpinBox 接收浮点型范围

from PySide6.QtWidgets import QApplication, QVBoxLayout,QWidget,QSpinBox,QDoubleSpinBox

# app = QApplication([])
# window = QWidget()
# window.setGeometry(100, 100, 200, 200)
# laoyout = QVBoxLayout(window)

# spinbox = QSpinBox() # 整型
# spinbox.setRange(0, 100) # 设置范围
# spinbox.setSingleStep(1) # 设置步长
# spinbox.setValue(50) # 设置初始值

# double_spin_box = QDoubleSpinBox()
# double_spin_box.setRange(0.0, 100.0)
# double_spin_box.setSingleStep(0.5)
# double_spin_box.setValue(20.0)

# laoyout.addWidget(spinbox)
# laoyout.addWidget(double_spin_box)

# window.show()
# app.exec()

class SpinBoxWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('spinboxwindow')
        self.layout = QVBoxLayout(self)

        self.init_ui()

    def init_ui(self):
        self.spinbox = QSpinBox()
        self.spinbox.setRange(0,100)
        self.spinbox.setSingleStep(1)
        self.spinbox.setValue(0)

        self.dspinbox = QDoubleSpinBox()
        self.dspinbox.setRange(0.0,100.0)
        self.dspinbox.setSingleStep(1.5)
        self.dspinbox.setValue(0.0)

        self.layout.addWidget(self.spinbox)
        self.layout.addWidget(self.dspinbox)


if __name__ == '__main__':
    app = QApplication([])
    window = SpinBoxWindow()
    window.show()
    app.exec()



# 这两个部件的用法非常类似，它们都有以下常见的属性和方法：
# setRange(min, max): 设置数值范围。
# setSingleStep(step): 设置步长。
# setValue(value): 设置初始值。
# value(): 获取当前的值。
# valueChanged.connect(slot): 连接值变化的信号。