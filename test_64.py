#!/usr/bin/env python
# -*- coding:utf-8 -*-

#利用ellipse 和 rectangle 画图

from tkinter import *

root = Tk()
root.title('矩形')

cv = Canvas(root,width=500,height=500,bg='gray')

cv.create_rectangle(10,100,300,200,width=2)  #例如(50，50)，（200，200）这两个点 画出来是个正方形，因为横坐标差值与纵坐标差值相等

cv.pack(side='top')

root.mainloop()

