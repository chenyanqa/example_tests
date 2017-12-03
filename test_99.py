#!/usr/bin/env python
# -*- coding:utf-8 -*-

#题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
fp1 = open('a.txt','w+')
fp2 = open('b.txt','w+')
fp3 = open('c.txt','w+')

fp1.write('dsaffkasjfakf')
fp2.write('xcnjsdfjhfslfdsfdffsdf')

fp1.seek(0)
s1 = fp1.read()
print(s1)  #print(fp1.read())  不输出任何内容

fp2.seek(0)
s2 = fp2.read()
print(s2)

s3 = s1 + s2
print (s3)
list1 = list(s3)
list1.sort()  #sort()方法只针对序列
s4 = ''.join(list1)
#print (s4)
fp3.write(s4)
fp3.seek(0)
print (fp3.read())

