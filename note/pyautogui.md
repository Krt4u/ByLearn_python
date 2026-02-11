import pyautogui
import pygetwindow as gw
import time
# https://zhuanlan.zhihu.com/p/30917919257

# pyautogui.moveTo(500, 500, duration=0.5, tween=pyautogui.linear)

# pyautogui.mouseDown(x=None, y=None, button='left', duration=0.0)

# pyautogui.moveTo(700, 700, duration=1, tween=pyautogui.linear)

# pyautogui.click(1600, 0,clicks=1, interval=0.0, button='right', duration=0.1, tween=pyautogui.linear)

#获取屏幕尺寸
screen_width, screen_height = pyautogui.size()
print(screen_width, screen_height)

# #当前鼠标位置
# while 1:
#     x,y = pyautogui.position()
#     print(x,y)
#     time.sleep(0.5)

#键盘输入
# pyautogui.hotkey('win', 'd') 组合
# pyautogui.press('') 单个

# pyautogui.click(screen_width //2, screen_height //2, clicks=1, interval=0.0, button='right', duration=0.5, tween=pyautogui.linear)

# pyautogui.click((screen_width //2)+10, (screen_height //2)+125, clicks=1, interval=0.0, button='left', duration=0.5, tween=pyautogui.linear)

# #全屏截图
# scshot = pyautogui.screenshot()
# # region指定截图区域
# #返回PIL.image 对象 可用PIL库进行处理
# scshot.save("scshot.png")

# #像素原色获取与匹配
# pixel_color = pyautogui.pixel(screen_width // 2, screen_height // 2)
# #检查指定坐标的像素颜色是否匹配特定颜色
# is_match = pyautogui.pixelMatchesColor(
#     screen_width // 2, 
#     screen_height // 2,
#     expectedRGBColor=(255,255,255), #比较 rgb 颜色元组
#     tolerance=0 #颜色匹配容差
# )

# #图像识别
# location = pyautogui.locateOnScreen(
#     './good.png'
# ) #返回box对象（left，top，width，height）
# #返回识别图像的中心坐标
# locations = pyautogui.locateAllOnScreen('./image.png')
# #返回生成器

# point = pyautogui.center(location)
# print(point)
# pyautogui.click(point)



# while 1:
#     locations = pyautogui.locateAllOnScreen('./good.png')
#     for loc in locations:
#         pyautogui.click(pyautogui.center(loc),duration=0.3)
#     pyautogui.hotkey('pgdn')
#     time.sleep(0.4)


# location = pyautogui.locateOnScreen(
#     'image.png',           # 图像文件路径
#     grayscale=False,       # 是否使用灰度模式匹配
#     confidence=1.0,        # 匹配置信度 (0.0-1.0)，需要OpenCV
#     region=(left, top, width, height),  # 限制搜索区域
#     step=1,                # 像素采样步长，增大可提高速度
#     minSearchTime=0        # 最小搜索时间（秒）
# )


# grayscale：使用灰度图像进行匹配，可提高约30%的速度，但可能降低准确性
# confidence：匹配置信度，1.0表示100%匹配，降低此值可容忍部分差异
# region：限制搜索区域，可显著提高性能
# step：像素采样步长，默认为1（检查每个像素），增大可提高速度但可能降低准确性
# minSearchTime：最小搜索时间，确保在快速匹配时不会因为闪烁而错过


#消息对话框
# 警告/提示框
# pyautogui.alert(
#     text='显示的消息',
#     title='窗口标题',
#     button='按钮文本'
# )

# # 确认框，返回用户点击的按钮文本
# result = pyautogui.confirm(
#     text='请确认操作',
#     title='确认',
#     buttons=['确定', '取消', '重试']
# )

# # 输入框，返回用户输入的文本或None（如果取消）
# user_input = pyautogui.prompt(
#     text='请输入您的名字',
#     title='输入',
#     default='默认值'
# )

# # 密码输入框，返回用户输入的文本或None
# password = pyautogui.password(
#     text='请输入密码',
#     title='密码输入',
#     default='',
#     mask='*'
# )
# 根据标题查找窗口
# windows = gw.getWindowsWithTitle('title')
# windows.active() #激活窗口
# all_win = gw.getAllWindows() # 获取所有窗口
# print(all_win)
# active_win = gw.getActiveWindow() # 获取当前活动窗口
# print(active_win)
# active_win_title = gw.getActiveWindowTitle() #获取当前活动窗口标题
# print(active_win_title)
# 窗口操作
# active_win.maximize() #窗口最大化
# active_win.activate()  # 激活(前置)窗口,保证不是最小化
# active_win.maximize()  # 最大化窗口
# active_win.minimize()  # 最小化窗口
# active_win.restore()   # 还原窗口,之前的位置和大小
# active_win.close()     # 关闭窗口
# 移动和调整窗口大小
# active_win.moveTo(x, y)      # 移动窗口到指定位置
# active_win.resizeTo(w, h)    # 调整窗口大小
# active_win.moveRel(x, y)     # 相对移动窗口
# active_win.resizeRel(w, h)   # 相对调整窗口大小
# active_win.resizeTo(w, h)

# 在特定窗口内执行操作
# window = gw.getAllTitles() #返回完整标题
# print(window)
# win = gw.getWindowsWithTitle("Notepad++")[0] #匹配字符串查找，标题部分查找
# print(win)
# if win.isMinimized:
#     win.restore()
# win.active()

pyautogui.hotkey('win', 'r')
pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(0.2)
win = gw.getWindowsWithTitle('记事本')
print(win)
if win:
    windows = win[0]
    if windows.isMinimized:
        windows.restore()
    pyautogui.write('111')





