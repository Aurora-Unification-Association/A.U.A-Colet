# coding:utf-8
import os

from func.Colet import Colet
import tkinter as tk
from PIL import ImageTk

_: int = 0


# 创建开启Settings页面方法
def settingsPassageShow():
    os.system('python run.py')


# 创建窗口
window = tk.Tk()
window.resizable(_, _)
window.title('A.U.A for {Colet}')


# 创建储存图片的类
class imgs():
    bg = ImageTk.PhotoImage(file='img/A.U.A icon.png')
    settings_img = ImageTk.PhotoImage(file='img/A.U.A Settings icon.png')


class label():
    bgLabel = tk.Label(window, width=696, height=566, image=imgs.bg)
    settings_imgBtn = tk.Button(window, image=imgs.settings_img, bd=0, command=settingsPassageShow)


# 定义显示方法
def show():
    label.bgLabel.pack()
    label.settings_imgBtn.place(x=660, y=1)


# 调用显示方法
show()

tk.mainloop()
