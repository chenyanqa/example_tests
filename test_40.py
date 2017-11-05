#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 题目：将一个数组逆序输出。程序分析：用第一个与最后一个交换。


# list = [1,3,4,5,68,100]
# list.reverse()
# print(list)


# list = [1,3,4,5,68,100]
#
# n = len(list)
# for i in range(int(n/2)):  #注意，两两交换时，循环次数为序列总长度的一半即可
# 	list[i],list[n-1-i] = list[n-1-i],list[i]
# print(list)

list = [1,3,4,5,68,100]
print(list[::-1])
