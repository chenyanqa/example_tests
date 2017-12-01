#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#列表排序及连接。 排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。


list1 = [1,55,6,3,99]
list2 = [100,5,88,40,9]

list1.sort()
print(list1)

# list1.extend(list2)
# print(list1)

print(list1+list2)
