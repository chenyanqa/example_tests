#!/usr/bin/env python
# -*- coding:utf-8 -*-
#有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

# array = [2,6,9,11,33,80,99]
#
# n = int(input('请输入任意数字：'))
#
# array.append(n)
#
# array.sort()
# print(array)



# if __name__ == '__main__':
#     # 方法一 ： 0 作为加入数字的占位符
#     a = [1,4,6,9,13,16,19,28,40,100,0]
#     print('原始列表:')
#     for i in range(len(a)):
#         print(a[i],end=' ')
#     number = int(input("\n插入一个数字:\n"))
#     end = a[9]
#     if number > end:
#         a[10] = number
#     else:
#         for i in range(10):
#             if a[i] > number:
#                 temp1 = a[i]
#                 a[i] = number
#                 for j in range(i + 1,11):
#                     temp2 = a[j]
#                     a[j] = temp1
#                     temp1 = temp2  #起到交换变量的作用
#                 break
#     print('排序后列表:')
#     for i in range(11):
#         print(a[i],end=' ')


# 通过序列插入的思路
list = [1,3,5,7,9,11]
print(list)
#我将通过插入数字7来加入按照从小到大排列的列表中
n = int(input("请输入数字:"))
#通过for循环来讲数情书字在列表中定位，然后将数字添加进去就可以了。
if n > list[5]:
	list.append(n)

elif n< list[0]:
	list.insert(0,n)

for i in range(6):
    if list[i] < n < list[i+1]:
        list.insert(i+1,n)
print(u"插入数字后的列表为：\n",list)