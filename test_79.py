#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#字符串排序。

# #当个字符串：
# s = 'sindnfgg'
# print('排序前：%s'% s)
#
# list1 = list(s)  #将字符串转换为列表
# list1.sort()
#
# #print(list1)
#
# print('排序后：%s'%(''.join(list1)))  #将列表转换为字符串
#


#多个字符串：

list = []

for i in range(3):
    list.append(input('请输入字符串：'))

list.sort()

print(list)
