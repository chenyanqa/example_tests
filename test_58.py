#!/usr/bin/env python
# -*- coding:utf-8 -*-

#画图，学用rectangle画方形

# from tkinter import *
#
# root = Tk()
#
# cv = Canvas(root,width=500,height=500,bg='gray')
# cv.pack(expand=YES,fill=BOTH)
#
# cv.create_rectangle(100,100,200,200,width=1,fill='red')
# root.mainloop()


if __name__ == '__main__':
	from tkinter import *

	root = Tk()
	root.title('Canvas')
	canvas = Canvas(root, width=400, height=400, bg='yellow')
	x0 = 200
	y0 = 100
	y1 = 275
	x1 = 275  #两个x 相减 为长，两个y相减为宽
	for i in range(19):
		canvas.create_rectangle(x0, y0, x1, y1)
		x0 -= 5
		y0 -= 5
		x1 += 5
		y1 += 5

	canvas.pack()
	root.mainloop()