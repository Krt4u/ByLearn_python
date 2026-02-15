[Python开发GUI---PySide6超详细的教程 - 知乎](https://zhuanlan.zhihu.com/p/673903865)

QWidget：基础的用户界面组件，用于构建应用程序的窗口和部件。
QLabel：用于显示文本或图像的标签。
QPushButton：按钮，用于触发用户交互。
QLineEdit：单行文本输入框，用于接受用户的文本输入。
QTextEdit：多行文本输入框，用于接受用户的多行文本输入。
QComboBox：下拉框，用于选择列表中的一个选项。
QCheckBox：复选框，用于表示二进制的选择状态。
QRadioButton：单选按钮，用于在一组中选择一个选项。
QSpinBox 和 QDoubleSpinBox：整数和浮点数的微调框，用于方便地增减数值。
QSlider：滑块，用于通过拖动来选择数值。
QProgressBar：进度条，用于显示操作的进度。
QListWidget 和 QTreeWidget：列表框和树形控件，用于显示和管理项目列表和层次结构。
QTabWidget：选项卡窗口，用于将内容分组到多个选项卡页中。
QFileDialog：文件对话框，用于选择文件和目录。
QMenuBar 和 QMenu：菜单栏和菜单，用于组织和呈现应用程序的菜单选项。
QToolBar：工具栏，用于快速访问应用程序中的常用功能。
QStatusBar：状态栏，用于显示应用程序的状态信息。
QMessageBox：消息框，用于显示提示、警告和错误消息。
QGraphicsView 和 QGraphicsScene：用于处理 2D 图形和图形场景的组件。
QCalendarWidget：日历控件，用于显示和选择日期。

QLabel常用的属性在表格中展示
alignment：标签内容的对齐方式	可以使用 setAlignment()方法设置。对齐方式可以是左对齐、右对齐、居中
indent：标签文本的缩进（以像素为单位）	可以使用 setIndent()方法设置
margin：标签内容周围边距的宽度	可以使用 setMargin()方法设置
pixmap：标签显示的图片	可以使用 setPixmap()方法设置
text：标签的文本内容	可以使用 setText()方法设置
textFormat：标签的文本格式	可以使用 setTextFormat()方法设置
wordWrap：布尔属性，指示标签的自动换行策略	可以使用 setWordWrap()方法设置。如果启用自动换行，文本将根据标签的宽度自动换行显示。