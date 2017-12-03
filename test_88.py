#!/usr/bin/env python
# -*- coding:utf-8 -*-

#题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,
# 然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。

list1 = list(input('请输入四位数字：'))
#print (list1)

list2 = []
for i in range(4):
	 list2.append(str((int(list1[i])+5)%10)) #str() 可以将int转为字符

#也可以通过循环来调换位置
list2[0],list2[3] = list2[3],list2[0]
list2[1],list2[2] = list2[2],list2[1]

print ('加密后的数字为:%s'%(''.join(list2)))





