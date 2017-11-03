#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
题目：对10个数进行排序。
程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

'''

#方法1：利用序列本身的sort（）方法
# list = [1, 4, 6, 7, 85, 33, 23, 8, 11, 99]  #list中 数字加引号就变为了字符，不加 就表示变量或者数字
#
# list.sort()
#
# print(list)

#方法2：选择排序法, 将第一个元素与后面9元元素中选出的最小值 进行交换，然后第二个元素与后面8个元素进行交换
list = [4, 1, 6, 7, 85, 33, 23, 8, 11, 99]

for i in range(len(list)):
    min = i   #这个 min变量不能省，这个变量是用来 存储当前找出来的最小值的索引，而且每次i取新值得时候，默认比较对象
    for j in range(i+1,len(list)):  #该循环的作用是，找出i以后面元素中最小的值
        if list[min] > list[j]:
            min = j
    list[i],list[min] = list[min],list[i]
for i in range(len(list)):
    print(list[i],end=' ')


