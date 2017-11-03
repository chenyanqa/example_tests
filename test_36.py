#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#求100之内的素数。素数又称质数 表示只能被1和本身整除的数，因为因素分解的唯一性，因此规定1 不是质数


for i in range(2,100):
    flag = 1  # 默认当前数为指数
    for j in range(2,i):   #当i取2时，range（2，2） 表示一个空序列，因此循环直接不执行，因此flag为1
        if (i%j == 0):  #注意取模 才表示余数的情况
            flag =0
            break
    if flag ==1:
        print(i)


#print(list(range(2,2)))
