#!/usr/bin/env python
# -*- coding:utf-8 -*-

#画椭圆。
# from tkinter import *
#
# root = Tk()
# cv = Canvas(root,width=500,height=500,bg='green')
# cv.create_oval(100,100,400,200,width=1)
#
# cv.pack()
# root.mainloop()


if __name__ == '__main__':
	from tkinter import *

	x = 360
	y = 160
	top = y - 30
	bottom = y - 30

	canvas = Canvas(width=400, height=600, bg='white')
	for i in range(20):
		canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
		top -= 5
		bottom += 5
	canvas.pack()
	mainloop()












