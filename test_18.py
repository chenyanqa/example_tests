#!/usr/bin/env python
# -*- coding:utf-8 -*-

#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，
# 几个数相加由键盘控制。

import math
a = int(input('请输入数字a：'))
n = int(input('请输入相加数的数量：'))

list = []
c = 0

for i in range(n):
	c = c + a*pow(10,i)  #pow(x,y) 表示x的y次幂
	list.append(c)
print(sum(list))


'''
1、lambda 表达式：是一种将函数精简为表达式的方式，例如
def ds（x）：
	return 2*x +1
ds(5)

等价于：
g = lambda x ：2*x+1 （g为函数名，x为定义一个变量，2*x+1 表示具体操作，后面还可跟操作对象）
g（5） =》调用函数


2、reduce（）函数--是一个python内建函数。
list = [1,2,3,4,5]
print(reduce(lambda x,y:x+y,list)) -->整个表达式的意思为：依次对list序列 进行加法加法操作，例如1+2得到的结果在加3.。。

'''








