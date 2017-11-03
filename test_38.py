#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#求一个3*3矩阵对角线元素之和。
'''
1 2 3
4 5 6
7 8 9
'''

#方法1：定义一个固定的矩阵
list = [[1,2,3],[4,5,6],[7,8,9]]

sum = 0

for i in range(3):
    sum = sum +list[i][i]

print(sum)


#方法2：动态生成一个二维矩阵（错误）
# list = [][]  # 二维序列 不能直接这样定义
# for i in range(3):
#     for j in range(3):
#         list = list.append(list[i][j])
#
# print(list)


#定义二维序列： 定义两个空序列a,b，然后让一个序列a.append(b) 即可
# tmp = []
# for i in range(3):
#     tmp.append(i)
# a = []
# for j in range(3):
#     a.append(tmp)
# print(a)


# count = 1
# a = []
# for i in range(3):
#     b = []
#     for j in range(3):
#         b.append(count)
#         count = count +1
#
#     a.append(b)
# print(a)


# a = []
# b = [1,2,3,4,5,6,7,8,9]
# c = str(b)
# print(c)
#
# print(c.split(',',3))  #['[1', ' 2', ' 3', ' 4, 5, 6, 7, 8, 9]']








