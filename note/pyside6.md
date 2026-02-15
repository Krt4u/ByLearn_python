[Python开发GUI---PySide6超详细的教程 - 知乎](https://zhuanlan.zhihu.com/p/673903865)

signal和emit

命令行可用 pyside6-desinger 打开图形化qt 

ui文件转换成py文件
pyside6-uic your_ui_file.ui -o ui_your_ui_file.py

运行时直接加载ui文件
loader = QUiLoader() 
ui_file = QFile("your_ui_file.ui") 
ui_file.open(QFile.ReadOnly) 
window = loader.load(ui_file) 
ui_file.close()

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

补充的常用 Qt 控件和组件
容器类（布局相关）
QGroupBox：带标题的容器，用于分组控件。
QFrame：可自定义边框的空白容器，常用于分隔区域。
QSplitter：可拖动分隔的容器，用于调整子控件大小。
QStackedWidget：多个页面叠在一起，只显示一个，适合做“页面切换”。
QScrollArea：滚动区域，适合放置超出可视范围的内容。

输入与显示
QPlainTextEdit：类似 QTextEdit，但更适合处理纯文本（性能更好）。
QTextBrowser：可显示富文本（HTML）、支持超链接的文本浏览器。
QTimeEdit / QDateEdit / QDateTimeEdit：用于选择时间、日期或两者。
QFontComboBox：专门用于选择字体的下拉框。
QColorDialog：颜色选择对话框。
QFontDialog：字体选择对话框。
QInputDialog：你已经用过啦～用于快速获取用户输入。

图形与绘图
QPixmap / QImage / QPicture：图像处理类。
QLabel（你提过）：也可以用来显示图片（setPixmap()）。
QPainter：绘图核心类，用于自定义绘制图形、文字等。
QOpenGLWidget：用于集成 OpenGL 渲染内容。

数据模型与视图（更高级）
QTableWidget / QTableView：表格控件，适合显示二维数据。
QTreeView / QListView：更灵活的视图控件，配合模型使用。
QStandardItemModel / QAbstractItemModel：数据模型类，用于配合视图控件。
QCompleter：自动补全器，可与 QLineEdit 等配合使用。

其他实用控件
QTimer：定时器，用于定时执行任务。
QSystemTrayIcon：系统托盘图标，适合后台运行的程序。
QClipboard：访问剪贴板内容。
QToolBox：折叠面板控件，类似手风琴菜单。
QDial：旋钮控件，类似音量旋钮。
QLCDNumber：显示数字的 LCD 风格控件。
QKeySequenceEdit：用于设置快捷键的控件。
QWizard / QWizardPage：用于创建多步骤的向导界面。

QLabel常用的属性在表格中展示
alignment：标签内容的对齐方式	可以使用 setAlignment()方法设置。对齐方式可以是左对齐、右对齐、居中
indent：标签文本的缩进（以像素为单位）	可以使用 setIndent()方法设置
margin：标签内容周围边距的宽度	可以使用 setMargin()方法设置
pixmap：标签显示的图片	可以使用 setPixmap()方法设置
text：标签的文本内容	可以使用 setText()方法设置
textFormat：标签的文本格式	可以使用 setTextFormat()方法设置
wordWrap：布尔属性，指示标签的自动换行策略	可以使用 setWordWrap()方法设置。如果启用自动换行，文本将根据标签的宽度自动换行显示。

对于其他很多qt类的布局方法，可在QT模块中的AlignmentFlag枚举类中


信号signal与槽slot的基本概念
信号（Signal）：当对象的状态发生变化时，它会发出一个信号。例如，按钮被点击时会发出 clicked 信号。
槽（Slot）：是一个可以响应信号的函数。当信号被发出时，连接到该信号的槽函数就会被自动调用。
这种机制实现了松耦合的设计：信号的发送者不需要知道接收者的具体实现，只需发出信号即可
在 PySide6 中，连接信号和槽通常使用 .connect() 方法

当按钮被点击时，它会发出 clicked 信号，自动调用 conncet 连接的函数。

一个信号可以连接多个槽，所有槽都会被依次调用。
一个槽也可以连接多个信号，只要参数匹配即可。