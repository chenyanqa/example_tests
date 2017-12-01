#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
'''
注：list 比字符串的优势，取值方便
切片  即list取值的一种方式,  取值是顾头不顾尾，注：切片的步长默认为1，不可为0
num2 = [1, 2, 3, 4, 5, ["a", "b", "c", ["d", "e"]]]
print(num2[3:6]) # 这个切片表示获取从第三个元素到第六个元素的值，当前列表中只有5个元素，由于切片的性质顾头不顾尾，
所以要取的最后一个值，就必须是6
#>>>[4, 5, ['a', 'b', 'c', ['d', 'e']]]
print(num2[:3])#从头开始取，取到第二个元素
#>>>[1, 2, 3]
print(num2[1:5:2]) #取 索引为1 到 4的值，步长为2
# print(num2[::2]) #表示取所有的值，步长为2
print(num2[::-1])#切片步长为负数，从后面往前面取值，相当于翻转了
#>>>[['a', 'b', 'c', ['d', 'e']], 5, 4, 3, 2, 1]
注：步长为负数，前面为正数的，取出来为空

print(num2[1:5:-1])  #从索引位置1-4 然后取反

list = [1,2,3,4]
list.insert(2,10)
print(list)    # [1, 2, 10, 3, 4]

'''

# if __name__ == '__main__':
#     n = int(input('整数 n 为:\n'))
#     m = int(input('向后移 m 个位置为:\n'))
#
#
#     def move(array, n, m):
#         array_end = array[n - 1]
#         for i in range(n - 1, -1, - 1):
#             array[i] = array[i - 1]
#         array[0] = array_end
#         m -= 1
#         if m > 0: move(array, n, m)
#
#
#     number = []
#     for i in range(n):
#         number.append(int(input('输入一个数字:\n')))
#     print('原始列表:', number)
#
#     move(number, n, m)
#
#     print('移动之后:', number)


from random import randint

# #list1 = [randint(1,110) for i in range(7)]
# list1 = [1,2,3,4]
# print(list1)
# n = len(list1)
# m = int(input('请输入移动位数：'))
#
# list2 = []
#
# #list1[0:m],list1[m:n] = list1[m:n],list1[0:m]
# print(list1)



#方法2： 通过移动的过程 拼接出 新的序列
# a=[]
# n=int(input('您想输入几个整数：'))
#
# for i in range(1,n+1):
#     s=int(input('请输入第%d位数：'%i))
#     a.append(s)     #形成原始序列
#
# m=int(input('您想将列表移动几位：'))
# print('排序前列表：%s'%a)
# b=a[-m:]                #获取后面的m个数
# c=a[:-m]                #获取前面除了m的数
# a=b+c                   #拼接成新列表
# print('排序后列表：%s'%a)



# a = [1,2,3,4,5,6,7]
# #b = a[:]  #表示复制
# #b = a[1:3] #表示取序列索引位置1-2的元素  序列是顾头不顾尾
#
# # b = a[::-1]  #表示整个列表取反
# # b = a[1:5:-1]   #表示从序列索引1-4的位置元素 开始取反，输出为[5,4,3,2]
#
# #b = a[:-1]   # 表示从序列的开头取到序列结尾 但是不包括结尾 输出[1, 2, 3, 4, 5, 6]
#
# b = a[-2:]   # 表示从序列倒数第二个开始取，取到无穷大，因此最后一位可以被取到 取 输出[6, 7]
# print(b)


