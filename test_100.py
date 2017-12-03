#!/usr/bin/env python
# -*- coding:utf-8 -*-

#题目：列表转换为字典。

# list1 = ['name','age']
# list2 = ['chenyan','30']
#
# # print (dict([list1,list2]))  #dict([x])
# print (dict(zip(list1,list2)))
# print (zip(list1,list2)) #zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表


l1=[1,2,3,6,87,3]
l2=['aa','bb','cc','dd','ee','ff']
d={}
for i in range(len(l1)): #字典一般优先对key进行操作
    d[l1[i]]=l2[i] # 注意，key 若重复，则新值覆盖旧值   将key-value一一对应起来
print (d)