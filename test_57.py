#!/usr/bin/env python
# -*- coding:utf-8 -*-
#画图，学用line画直线。

from tkinter import *

root = Tk()
root.title('test GUI')

cv = Canvas(root,width =300,height =300,bg='green')
cv.pack(expand=YES,fill=BOTH)

x1,y1=50,20
x2,y2=100,20
x3,y3=75,40
x4,y4=75,100
cv.create_line(x1,y1,x3,y3, width=3, fill='red')
cv.create_line(x2,y2,x3,y3, width=3, fill='red')
cv.create_line(x1,y1,x4,y4, width=3, fill='red')
cv.create_line(x2,y2,x4,y4, width=3, fill='red')

root.mainloop()




