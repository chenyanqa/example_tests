#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、Tkinter是python内助的图形界面处理库，它会调用操作系统提供的本地HUI接口，完成最终的GUI，且对外提供封装好的接口已完成对应的GUI需求
2、在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
3、pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
4、在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出。
5、在GUI系统中，一般按钮、滚动条、文本框等都是控件widget，包括窗口也使一个特殊控件，不过窗口可以容纳其他控件，而Frame就表示窗口
所以所有的widget 都默认从Frame继承

6、class Application(Frame):
    def __init__(self,master=None): #第一个self 表示Application对象本身，第二个master表示当前控件的父控件，一般默认为None
        Frame.__init__(self,master) #调用Application的父类Frame的构造函数初始化Application类的Frame类部分（由于是初始化自身的一部分，因此
        #需要传入self，同时传入了Application.__init__的master参数，作为Frame.__init__的master。），这样设置的好处试讲当前对象的父控件初始化为frame
        self.pack() #把当前对象所表示的控件添加到父容器里面
        self.createWidgets()
7、http://blog.chinaunix.net/uid-29578485-id-5776737.html
http://www.cnblogs.com/collectionne/p/6885066.html

8、Help on module tkinter.messagebox in tkinter:  tkinter是一个库， tkinter.messagebox 等是里面的模块
9、子类调用父类构造方法的作用：如果子类定义了自己的__init__构造方法函数，当子类的实例对象被创建时，子类只会执行自己的__init__方法函数，
如果子类未定义自己的构造方法函数，会沿着搜索树找到父类的构造方法函数去执行父类里的构造方法函数。如子类定义了自己的构造方法函数，如果子
类的构造方法函数内没有主动调用父类的构造方法函数，并以子类自身（self等相关参数）作为参数传递给父类构造函数，那父类的实例变量在子类不会在刚刚创建子类实例对象时出现了。
'''

# 导入tkinter包，为其定义别名tk
# import tkinter as tk

# # 定义Application类表示应用/窗口，继承Frame类
# class Application(tk.Frame):
#     # Application构造函数，master为窗口的父控件
#     def __init__(self, master=None):
#         # 初始化Application的Frame部分
#         tk.Frame.__init__(self, master)
#         # 显示窗口，并使用grid布局
#         self.grid()
#         # 创建控件
#         self.createWidgets()
#
#     # 创建控件
#     def createWidgets(self):
#         # 创建一个文字为'Quit'，点击会退出的按钮
#         self.quitButton = tk.Button(self, text='Quit', command=self.quit)
#         # 显示按钮，并使用grid布局
#         self.quitButton.grid()
#
#
# # 创建一个Application对象app
# app = Application()
# # 设置窗口标题为'First Tkinter'
# app.master.title = 'First Tkinter'
# # 主循环开始
# app.mainloop()




# #第一步引入模块内容
# from tkinter import *  #导入tkinter包的所有内容
#
# #第二步 从Frame派生一个Application类，这是所有Widget的父容器
# class Application(Frame):   # 所有的窗口小部件（Widget）都是从Frame类派生的
#     def __init__(self,master=None):  #__init__(self, master=None, cnf={}, **kw)，master表示当前控件的父控件，默认值为None
#         Frame.__init__(self,master) #表示将当前控件构造函数的self（对象本身）+master（父控件）都传给父类Frame 通过他的构造函数初始化
#         self.pack() #将当前类对象显示并使用pack（）布局
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLabel = Label(self,text='Hello,world!',padx=200,pady=200) #这里其实是相当于创建了一个helloLabel属性
#         #self.helloLabel = Label(self, text='Hello,world!',height=10,width=20)
#         self.helloLabel.pack()
#         self.quitButton = Button(self,text='Quit',command=self.quit) #这里的self 其实只是当前self对应的master参数
#         self.quitButton.pack()
#
# #实例化Application，并启动消息循环：
# app = Application()
# app.master.title('Hello World') #给当前窗口设置标题
# app.mainloop() #进入主循环（GUI程序中默认会有一个主循环一直监控是否有用户输入、退出或者按钮的commmand等事件触发）



from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)#因为子类的构造函数会自动覆盖父类的，如果子类想要调用父类的属性及函数的话，必须主动将类自身当做参数传递给父类构造函数，以生存父类对应的属性
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get()
        messagebox.showinfo('Message','Hello,%s'%name) #showinfo(title=None, message=None, **options)
app = Application()
app.master.title('Hello World')
app.mainloop()