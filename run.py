# coding:utf-8
import tkinter as tk
from PIL import ImageTk

_: int = 0

# 创建窗口
window = tk.Tk()
window.resizable(_, _)
window.title('A.U.A for {settings}')


# 创建储存图片的类
class imgs():
    settingsPassage = ImageTk.PhotoImage(file='img/A.U.A for SettingsPassage.png')


class label():
    settingsPassageLabel = tk.Label(window, image=imgs.settingsPassage)


# 定义显示方法
def show():
    label.settingsPassageLabel.pack()


# 调用显示方法
show()

tk.mainloop()















