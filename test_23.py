#!/usr/bin/env python
# -*- coding:utf-8 -*-

#打印出如下图案（菱形）:
'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''
'''
#方法1：首先将菱形分成上下两部分，上部分时，先用一个外层循环控制行数，然后分析每行中 空格及星花个数与当前行的关系
然后通过2个内层循环控制列，一个控制空格的输出列，一个控制星花的，注意星花所在列的起始位置一般在空格输出结束的位置。

方法2：通过一个外层循环控制行数，然后分析每行空格与星花的个数关系，此时使用字符串的链接方法，控制先输出空格然后输出星花
，print((3-i)*' '+(2*i+1)*'*')

'''
# n = int(input('请输入菱形大小(或者行数)：'))
# t = int(n/2)+1 #定义菱形上半部分行数
#
# for i in range(1,t+1): #依次取值1-t行
# 	for j in range(1,t+1-i): #控制列
# 		print(' ',end='')
# 	for k in range(t+1-i,t+i):
# 		print('*',end='')
#
# 	print()
#
# for i in range(1,n-t+1):   #同一个行数中 用来遍历的循环变量名称可以重复
# 	for j in range(1,i+1):
# 		print(' ',end='')
# 	for k in range(i+1,n+1-i):
# 		print('*',end='')
#
# 	print()


for i in range(4):
    print((3-i)*' '+(2*i+1)*'*')
for i in range(3):
    print((i+1)*' '+(5-2*i)*'*')