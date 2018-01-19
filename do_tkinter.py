#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、Tkinter是python内助的图形界面处理库，它会调用操作系统提供的本地HUI接口，完成最终的GUI，且对外提供封装好的接口已完成对应的GUI需求
2、在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
3、pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
4、在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出。


'''

#第一步引入模块内容
from tkinter import *  #导入tkinter包的所有内容

#第二步 从Frame派生一个Application类，这是所有Widget的父容器
class Application(Frame):   # 所有的窗口小部件（Widget）都是从Frame类派生的
    def __init__(self,master=None):  #__init__(self, master=None, cnf={}, **kw)

        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self,text='Hello,world!',padx=200,pady=200)
        #self.helloLabel = Label(self, text='Hello,world!',height=10,width=20)
        self.helloLabel.pack()
        self.quitButton = Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()

#实例化Application，并启动消息循环：
app = Application()
app.master.title('Hello World')
app.mainloop()
