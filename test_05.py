#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 输入三个整数x,y,z，请把这三个数由小到大输出。
import math

x = int(input('请输入第一个整数：'))
y = int(input('请输入第二个整数：'))
z = int(input('请输入第三个整数：'))

# if x < min(y,z):
# 	if y <=z:
# 		print(x,y,z)
# 	else:
# 		print(x, z, y)


# max = max(x,y)
# min = min(x,y)
#
# if z >max:
# 	print(min,max,z)
# elif min<z <max:
# 	print(min,z,max)
# elif z <min:
# 	print(z,min,max)

l =[x,y,z]  #直接将键盘接收到的3个数 赋值给 列表l
l.sort()
print(l)
