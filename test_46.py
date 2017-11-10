#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#求输入数字的平方，如果平方运算后小于 50 则退出。

import  math

#while(1):   #  while（1)/while True: 可以用来控制让 循环里面的语句一直执行，到时遇到 quit（）、break，exit（）等语句
while True:
    n = int(input('请输入数字：'))

    if(pow(n,2) >= 50):   #pow（2，3） 表示2的3次方
        print('运算结果为：%d' % pow(n,2))

    else:
        print('您本次平方运算结果小于50，需退出')
        #exit()
        break


