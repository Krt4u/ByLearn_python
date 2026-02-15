from PySide6.QtCore import QObject, Signal, Slot

class Communicator(QObject):
    my_signal = Signal(str)     # 定义一个str的信号类

    @Slot(str)  # 修饰器，修饰该函数是一个槽函数，并接收一个str对象
    def my_slot(self, message):
        print(f"收到信号：{message}")

com = Communicator()
com.my_signal.connect(com.my_slot)  # 连接槽函数
com.my_signal.emit("你好，信号！")  # emit 方法是直接发送信号
# 被Slot修饰的槽函数接收str传入message并执行
