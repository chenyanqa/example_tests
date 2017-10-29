#!/usr/bin/env python
# -*- coding:utf-8 -*-

#两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
# 有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
'''
这题可以直接解出来，但是怎么转换为程序的思路：
1、先使用程序打印出所有可能的组合，然后在通过条件的限制 逐一去排除
'''
# for a in ['x','y','z']:
# 	for b in ['x','y','z']:
# 		for c in ['x','y','z']:
# 			if(a!=b)and(b!=c)and(c!=a)and(a!='x')and(c!='x')and(c!='z'):
# 				print(a,b,c)


n=['a','b','c']
m=['x','y','z']
L=[]
for i in range(0,3):
    for j in range(0,3):
        L.append(n[i]+m[j])  #字符串的+号 表示连接符的意思，例如'a'+'b' 输出‘ab’
L.remove('ax')  #题目已知条件
L.remove('ay')  #由于c只能跟y打，因此a，b肯定都不行
L.remove('by')
L.remove('bz')  #由于y已经确定跟c打，a只能和z打，因此排除bz
L.remove('cx') #题目已知条件
L.remove('cz') #题目已知条件
print(L)