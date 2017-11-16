#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#输入3个数a,b,c，按大小顺序输出。

list1= []

# a = int(input('请输入第一个数：'))
# list1.append(a)
# b = int(input('请输入第二个数：'))
# list1.append(b)
# c = int(input('请输入第三个数：'))
# list1.append(c)

for i in range(3):
    a = int(input('请输入一个数：'))
    list1.append(a)


print(list1)

list1.sort()
print(list1)

list1.reverse()
print(list1)

print('a,b,c从大到小的顺序依次为：%d,%d,%d' % (list1[0],list1[1],list1[2]))



