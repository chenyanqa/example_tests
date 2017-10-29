#!/usr/bin/env python
# -*- coding:utf-8 -*-

#按逗号分隔列表。

# s = input('请输入字符串：')
# s.split(' ')  #.split()是字符串方法，不是list的
# print(s)

'''
1, .join()方法 里面的函数可以是序列，元素，字典，字符串等，但是如果序列里面是纯数字，纯int型的元素，则该方法会报错
TypeError: sequence item 0: expected str instance, int found，

2、解决办法：将list 中数字用引号括起来 转化成数字，或者，使用' '.join(str(n) for n in L)  将里面的纯数字转换成字符型

'''

#list = ['a','b','c','d','e']
list =['1','2']
#list = list(range(5))  #
s1= ' '.join(list)  #通过该方法可以将list 转化为字符串
print(s1)

# L = [1,2,3,4,5]
# s1 = ' '.join(str(n) for n in L)
# print(s1)