#!/usr/bin/env python
# -*- coding:utf-8 -*-

#利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

#自己的思路 没做出来
# def out_put(n):
# 	list2 = []
# 	if n ==1:
# 		list2[0] = list[n-1]
# 		return list2
# 	elif n ==2:
# 		list[0] = list[n-1]
# 		list[1] = list[n-2]
# 		return list2
# 	else:
# 		list2[n-1] = out_put(list[1])
# 		return list2
#
# list = ['a','b','c','d','e']
# print(out_put(list))


#递归的做法：
# def output(s,l):
# 	if l == 0:
# 		return
# 	print(s[l-1])
# 	output(s,l-1)
#
# s = input('input a string:')
# l = len(s)
# output(s,l)


# #方法2：利用列表的reverse特性
# s = input('请输入：')
# list = list(s)  #利用list（s）、list（range（10）） 都可以把list（）函数里面的参数列表化
# #list2 = list.reverse()  #由于list.reverse()方法的无返回值，因此 此时输出list2 显示为none
# list.reverse()
# print(list)


#方法3：利用列表 步长特性
'''
1、range(1,6,1) 输出[1,2,3,4,5]  -->正序步长1
2、range(5,0,-1) 输出[5,4,3,2,1]  -->倒序取，步长1
'''
s = input('请输入字符：')
for i in range(len(s)-1,-1,-1):
	print(s[i],end='')

list = list(s)
list2 = list[::-1]
print(list2)




