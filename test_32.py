#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#按相反的顺序输出列表的值。

# list= [1,2,3,4,5]
# list.reverse()
# print(list)

# list = ['a','b','c','d','e']
# for i in range(len(list)-1,-1,-1):
# 	print(list[i],end=' ')

list = ['a','b','c','d','e']
for i in list[::-1]:  #[::-1] 表示顺序取反操作 ,同时注意 python 中for循环中的循环遍历 永远取得是待变量内容的元素值，而不是下标
	print(i,end=' ')

for i in list[3::-1]:  #[3::-1] 表示从第三个索引位置开始，顺序取反 ，从list中元素d开始，输出 d,c,b,a
	print(i,end=' ')

	
