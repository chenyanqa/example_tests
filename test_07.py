#!/usr/bin/env python
# -*- coding:utf-8 -*-

#1、将一个列表的数据复制到另一个列表中。
# list1 = [1,3,4]
# list2 = [5,6,7]
# #list1.insert(1,list2)  # 这个插入是将整个列表当做一个元素插入到list1中
# list1.insert(1,100)  #在索引位置为1的地方插入元素值 100
# list1.extend(list2)  #在列表末尾一次性追加另一个列表的所有元素
# print(list1)
#
# 2、如果直接将list3 赋值给list4的话，那么list3、4 指向同一个内存索引，他俩中间一个改变都会影响另外一个  没有达到复制的功能
# list3 = [1,2,3]
# list4 = list3
# print(list4)
# print(list3)
# list4.insert(3,0)
# print(list4)
# print(list3)

#3、list[:] 复制
# list3 = [1,2,3]
# list4 = list3[:]  #表示复制
# print(list4)
# print(list3)
# list4.insert(3,0)
# print(list4)
# print(list3)

# import copy
# # 4、list.copy()
# list3 = [1,2,3]
# list4 =list3.copy()
# print(list4)
# list4.insert(3,0)
# print(list4)
# print(list3)

#5、list.append()
list3 = [1,2,3]
list4 = []
for i in range(len(list3)):
	list4.append(list3[i])
print(list4)