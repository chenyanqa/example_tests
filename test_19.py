#!/usr/bin/env python
# -*- coding:utf-8 -*-
#一个数如果恰好等于它的因子(这里的因子是只要能整除的都算，跟质因子做区别)之和，这个数就称为"完数"。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。

k = 0
for i in range(2,1001):  #因为因子不能是他本身，因此1排除掉
	list =[1,]   #默认因子1

	for j in range(2,i):  #遍历找出（2-i）之间所有能被i整除的数
		if i%j == 0:
			list.append(j)

	if i ==sum(list):  #程序无法得到正常的结果 可能是此时的i 已经在while循环中重新被赋值了，因此已经不是第一层for循环中的值了
		print(i,end=' ')
		print(list)
		k= k+1
	else:
		continue

print('1000内完数的个数为：%d'%k)


'''
这里误将因子和质因子概念混淆了，例如求n的因子的话，只需要在（2，n）之间遍历找到可以被整除的数即可。质因子的话 每次找打n的第一个
因子后，还需要将此时的商n1，拿来继续从（2-n1）之间遍历
'''
# from functools import reduce
# k = 0
# for i in range(2,1001):  #因为质因子不能是他本身，因此1排除掉
# 	list =[1,]
# 	while i !=1:
# 		for j in range(2,i+1):
# 			if i%j == 0:
# 				list.append(j)
# 				i = int(i/j)
# 				break
# 	if reduce(lambda x,y:x*y,list) ==sum(list):  #程序无法得到正常的结果 可能是此时的i 已经在while循环中重新被赋值了，因此已经不是第一层for循环中的值了
# 		print(reduce(lambda x,y:x*y,list))
# 		k= k+1
# 	else:
# 		continue
#
# print('1000内完数的个数为：%d'%k)

# i = int(input('input:'))
# list =[1,]
# while i !=1:
# 	for j in range(2,i+1):
# 		if i%j == 0:
# 			list.append(j)
# 			i = int(i/j)
# 			break
# print(list)
