#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
题目：取一个整数a从右端开始的4〜7位。
程序分析：可以这样考虑：
(1)先使a右移4位。
(2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4)
(3)将上面二者进行&运算。
'''

if __name__ == '__main__':
    a = int(input('input a number:'))
    b = a >> 4# a = list(str(123456789))[::-1]
    c = ~(~0 << 4)# print(a)
    d = b & c  
    print('%o\t%o'%(a,d))# b = []
#
# for i in range(len(a)):
#     if i in range(3,7):
#         b.append(str(i))
#
# print(b)
#
# print(''.join(b))



#字符串转换为序列

# str1 = '12345'
# print(list(str1))   #['1', '2', '3', '4', '5']
#
# str2 = "123 dfgg resf"
# print(str2.split(' '))    #['123', 'dfgg', 'resf']
#
# str3 = "www.google.com"
# print(str3.split('.'))    #['www', 'google', 'com']
#
#
# #序列转换为str
# list1 = [1,2,3,4,5]
# list2 = ['www', 'google', 'com']
# str4 = ''.join(list1)   #会报错：TypeError: sequence item 0: expected str instance, int found

'''
 1、 ' '.join() 用于连接字符串数组，可以将字符串，元组，序列中的字符串元素按照指定的格式 连接生成一个新的字符串
 其中 join（）中参数中的所有元素 都需要为字符串格式才行， 常见的数值型序列 需要先进行单个元素转换 才能调用join（）方法
 2、 .split(' ') 用于拆分字符串 ，按照指定的格式对字符串进行切片，并返回一个字符串序列
'''




