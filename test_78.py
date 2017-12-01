#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#找到年龄最大的人，并输出。请找出程序中有什么问题。

# #方法1：使用序列
# list = []
#
# for i in range(5):
#     list.append(int(input('请输入年龄：')))
#
# list.sort()
# print(list)
# print('年龄最大的为：%d'%(list[-1]))



#方法2：使用字典
'''
# dict.keys= input('请输入姓名：') 会报错
Traceback (most recent call last):
File "/Users/user/Documents/python/example_tests/test_78.py", line 23, in <module>
dict.keys= input('请输入姓名：')
AttributeError: 'dict' object attribute 'keys' is read-only
'''

dict = {}  #创建一个空字典

for i in range(3):  #通过循环控制用户5次输入
    key= input('请输入姓名 %d：'%(i+1))   #将输入的姓名 赋值给key变量
    value = int(input('请输入年龄 %d：'%(i+1)))  #将输入的年龄，赋值给value变量
    dict[key] = value   #组装key、value 成为一个字典

print(dict)
print(dict.keys())   #dict.keys()、dict.values() 单独取出来时 相当于序列
print(dict.values())
print(type(dict.values()))  #输出 <class 'dict_values'>

print(max(dict.keys()))
print(max(dict.values()))






