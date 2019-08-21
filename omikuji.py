#!/usr/bin/env python3

# import
import sys
from tkinter import *
import tkinter.messagebox as mb
from random import *

# おみくじの結果
def omikuji():
    omikuji_list = ['大吉', '中吉', '小吉', '吉', '凶', '大凶']
    random_list = choice(omikuji_list)
    mb.showinfo('結果', random_list)

# おみくじ画面
root = Tk()
root.title('おみくじ')

label1 = Label(text='下のボタンを押してください')
label1.pack()

# おみくじボタン
omikuji_button = Button(
    text='おみくじ',
    width=10, height=5,
    command=omikuji
)
omikuji_button.pack()

root.mainloop()
