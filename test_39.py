#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

array = [2,6,9,11,33,80,99]

n = int(input('请输入任意数字：'))

array.append(n)

array.sort()
print(array)