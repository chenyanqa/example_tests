#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#练习函数调用。

print('test')

def funa(a,b):

    return a+b

#print(funa(1,2))

if __name__ == '__main__':
    print(funa(1,2))


    '''
    1、该 __name__ 表示 python的内置属性，可以理解为.py文件的调用方式
    2、__main__ 表示其使用方式为 直接调用。（另外一种是作为模块引入）
    
    3、注意该语句并不表示程序入口，仅代表当前程序的执行方式，python 是一种脚本语言（动态逐行解释）
    因此 一般都是从程序第一行开始
    
    '''


