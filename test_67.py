#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
'''
1、python 中没有专门数组 这个数据结构，但是可以用 列表、元素 字典等数据结构替代
'''

# list1 = []
#
# n = int(input('请输入数组长度：'))
# for i in range(n):
#     a = int(input('请输入数组元素：'))
#     list1.append(a)

list1= [33,6,777,90,100]

print(list1)
list1.sort()
print(list1)
list1[0],list1[len(list1)-1] = list1[len(list1)-1],list1[0]
print(list1)

