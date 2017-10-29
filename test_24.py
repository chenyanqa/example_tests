#!/usr/bin/env python
# -*- coding:utf-8 -*-

#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''
1、由于分子和分母 很明显分别是一个菲波那切数列，因此可以定义一个斐波那契额函数
2、我在定义的过程中，分别定义了分子为一个 分母为一个，此时两个不同的函数,注意 由于我在定义的时候 n是从1 开始的，
因此调用的时候  循环遍历i的值 也需要从1开始，否则会报错。
Traceback (most recent call last):
  File "D:/cy/example_tests/test_24.py", line 30, in <module>
    c = fenzi(i)/fenmu(i)
TypeError: unsupported operand type(s) for /: 'NoneType' and 'NoneType'
'''

# def fenzi(n):
# 	if n == 1:
# 		return 2
# 	elif n == 2:
# 		return 3
# 	elif n > 2:
# 		return int(fenzi(n-1)+fenzi(n-2))
#
# def fenmu(n):
# 	if n == 1:
# 		return 1
# 	elif n == 2:
# 		return 2
# 	elif n > 2:
# 		return int(fenmu(n-1)+fenmu(n-2))
#
# list = []
# n = int(input('请输入数列长度：'))
#
# # for i in range(n):
# # 	c = fenzi(i)/fenmu(i)  #若i 默认从0 开始遍历，此时fenzi(0) 函数并没有定义，因此会报错
# # 	list.append(c)
#
# for i in range(1,21):
# 	c = fenzi(i)/fenmu(i)  #此时系统会默认结果为float类型
# 	list.append(c)
# print('求和数列为：%s'%(list))
# print('数列和为：%s'%sum(list))


#方法2：

sum = 0
a = 1
b = 2

for i in range(20):
	sum = sum +b/a   #可以通过找规律，后面每项分子，分母互换，且分子加上了前一项的分母
	b,a = a+b,b

print(sum)