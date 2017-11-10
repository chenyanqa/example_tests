#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#画图，学用circle画圆形。

'''
1、注意tkinter 在python2 和python3中的引用方法不一样 注意区分。
2、import tkinter  则只是引入了tkinter这个库文件（或者类），里面还有很多类或者控件的调用需要使用tkinter.Canvas()
而 from tkinter import *  表示引入全部类，函数及变量到当前文件，因此可以直接调用，不用再加tkinter前缀了 ，例如Canvas（）
'''

import tkinter
from tkinter import *
# #tkinter 练习1：label、button

# root = tkinter.Tk()  #tkinter.Tk()用于生成一个主窗体/主窗口 并赋给root 代表当前窗体实例
# root.title('test GUI')  #给当前窗体设置title
# root.resizable(width=True, height=False)  #root.resizable(1,0) 这两效果不一致
# root.geometry('500x500')  #设置窗体大小
#
# label = tkinter.Label(root,text='Hello,GUI')  #生产一个label标签
# label.pack()  #将该标签添加到主窗口
#
# button1 = tkinter.Button(root,text='Button1')  #生产一个button1
# button1.pack(side=tkinter.LEFT)  #将button1添加到root主窗口的左侧
#
# button2 = tkinter.Button(root,text='Button2')
# button2.pack(side=tkinter.RIGHT)
#
# button3 = tkinter.Button(root,text='test')
# button3.pack(anchor='w')
#
# root.mainloop()  #进入消息循环（必需组件）


# # tkinter 练习2：画矩形
# root = tkinter.Tk()
# cv = Canvas(root,width=500,height=500,bg = 'white')   #在当前窗口上创建一个画布
# #cv.create_rectangle(50,10,200,100,fill='red',outline='blue',width=5)  #(50,10),(200,100)两个坐标 50为画布的左边距，10 为画布的上边距，200为长，100为宽
# rt = cv.create_rectangle(10,10,110,110,outline='red',dash=5,fill='green')  #dash后跟数值 越大，虚线越稀疏
# cv.coords(rt,40,40,220,420)  #移动画布上的某个元素(item)到新的坐标
# cv.itemconfig(rt,fill='blue',dash=10)  #改变item的属性配置
#
# cv.pack()  #把画布添加到窗口即可，画布上带有rt矩形对
# root.mainloop()



# # tkinter 练习3：画圆形
# root = tkinter.Tk()  # 生成一个根窗口
#
# cv = Canvas(root,width=500,height=500,bg='yellow')   #生成一张 画布
# cv.create_oval(50,50,250,250,outline='black',fill='red')   #在画布上穿件一个椭圆类的item，必填参数为两组坐标点（x1，y1）,(x2,y2)
#
# #cv.pack()  #将画布添加到根窗口
# cv.pack(expand=0,fill =Y)   #这里的expand 主要表示side及fill的属性的生效性，为1，则生效，为0 ，则不生效
# root.mainloop()  #根窗口进入消息循环
#


if __name__ == '__main__':

    canvas = Canvas(width=600, height=600, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    k = 1
    j = 1
    for i in range(0, 26):
        canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=2)  #这里的width 表示圆的边界宽度

        k += j   #k = k+j
        j += 0.3  #j = j+0.3

    mainloop()