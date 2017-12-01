#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#反向输出一个链表。

n = int(input('请输入序列长度：'))

list1 = []
for i in range(n):
    list1.append(int(input('请输入：')))

list1.reverse()
print(list1)


