# 进度条
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QProgressBar, QPushButton, QLabel
from PySide6.QtCore import QTimer, Qt

class myBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('bar')
        self.layout:QVBoxLayout = QVBoxLayout(self)
        self.timer = QTimer(self) # 创建一个定时器
        self.timer.timeout.connect(self.simulate_task) # 定时器连接的任务

        self.init_ui()
            
    def init_ui(self):
        self.progress_bar = QProgressBar() # 配置进度条参数
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.lable = QLabel('请开始')
        self.lable.setAlignment(Qt.AlignmentFlag.AlignCenter)
# 这里的 AlignCenter 是 AlignmentFlag 枚举类的一个成员，而 AlignmentFlag 是 Qt 模块下的一个类，加上以后就能访问 AlignCenter
        self.start_btn = QPushButton('start')
        self.reset_btn = QPushButton('reset')
        self.start_btn.clicked.connect(self.start_task) # 设置点击槽函数
        self.reset_btn.clicked.connect(self.reset_task)

        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.lable)
        self.layout.addWidget(self.start_btn)
        self.layout.addWidget(self.reset_btn) # lq1001pl

    def simulate_task(self):
        self.current = self.progress_bar.value() # 模拟任务执行
        self.lable.setText('执行中......')
        if self.current == 100:
            self.timer.stop()
            self.lable.setText('已完成')
        self.newv = self.current + 1
        self.progress_bar.setValue(self.newv)

    def start_task(self):
        self.timer.start(10) # 一秒更新一次

    def reset_task(self):
        self.timer.stop()
        self.lable.setText('请开始')
        self.progress_bar.setValue(0)



if __name__ == '__main__':
    app = QApplication([])
    mybar = myBar()
    mybar.show()
    app.exec()

# 主要的 QProgressBar 方法和属性包括：

# setRange(min, max): 设置进度范围。
# setValue(value): 设置当前的进度值。
# value(): 获取当前的进度值。

# from PySide6.QtCore import QTimer 
# 创建一个定时器 
# self.timer = QTimer(self) # 设置间隔时间（单位：毫秒），比如每隔1000毫秒（1秒）触发一次 
# self.timer.setInterval(1000) 
# 连接定时器的 timeout 信号到一个槽函数 
# self.timer.timeout.connect(self.do_something) 
# 启动定时器 
# self.timer.start(100), 多少秒更新一次，执行一次
# 停止定时器
# self.time.stop()
# 只执行一次
# QTimer.singleShot(2000, self.do_something) # 2秒后执行一次 do_something