#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
题目：模仿静态变量(static)另一案例。
程序分析：演示一个python作用域使用方法
'''

# class test_static():
#     num = 1
#     def test_num(self):
#         self.num = 2
#         print(self.num)  #相当于 又重新创建了一个实例变量
#         print(test_static.num)  #打印静态变量
#
#
# a = test_static() #创建一个对象
# a.test_num()


class Num:
    nNum = 1  #静态变量
    def inc(self):
        self.nNum += 1  #实例变量（因为被重新赋值了，但是第一个self.num是静态变量）
        print('nNum = %d' % self.nNum)


if __name__ == '__main__':  #表示 当前程序 自己执行的时候 执行下列语句，但是被模块引入时不执行
    nNum = 2    #全局变量
    inst = Num()  #生成 类num（）的一个对象
    for i in range(3):
        nNum += 1
        print('The num = %d' % nNum)
        inst.inc()  #由于类的静态变量可以被类中函数直接调用，因此第一次循环时 ：self.nNum = 1+1=2 , 第二次循环时 self.nNum=2+1=3