#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，然后下一个重新报数，问最后留下的是原来第几号的那位

'''
约瑟夫环（约瑟夫问题）是一个数学的应用问题：已知n个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围。从编号为k的人开始报数，
数到m的那个人出列；他的下一个人又从1开始报数，数到m的那个人又出列；依此规律重复下去，直到圆桌周围的人全部出列。通常解决这类问题时
我们把编号从0~n-1，最后[1]  结果+1即为原问题的解。

1、一群人围在一起坐成[2]  环状（如：N）
2、从某个编号开始报数（如：K）
3、数到某个数（如：M）的时候，此人出列，下一个人重新报数
4、一直循环，直到所有人出列[3]  ，约瑟夫环结束

'''

#输出序列
# n = int(input('请输入人数：'))
# data = []
# for i in range(1,n+1):
#     data.append(i)
# print(data)
#
# data = [i for i in range(1,35)]    #python 列表解析： 表示data 的元素为，但是i的取值由for 循环控制
# print(data)
#
# i = 1  #指定第一个报数的人
# while len(data) > 1:  #判断是否为最后一个
#     if i % 3 == 0:  #如果当前数 可以被3整除 则剔除该数
#         data.pop(0)  #表示删除当前列表第一个元素
#     else:  # 如果不能被整除 则将该数 插入到序列最后一个位置
#         data.insert(len(data),data.pop(0))
#
#     i += 1
# print(data)


# def solve(n,m):
#     #自动身成列表,从0开始 到n-1
#     list1=list(range(n))
#     m-=1
#     k=m%n
#     while(len(list1) >1):
#         del list1[k]
#         k= (k+m) % len(list1)
#     return list1[0]
#
# print(solve(34,3))
#


# n=int(input("输入人数:"))
#
# List=[]
# for i in range(1,n+1):
#     List.append(i)
#
# sum=0
# while 1: # 默认进入无限循环
#     t=0
#     for i in range(1,len(List)+1):  #此循环中i 一直从1，2，3，4，5.。。 遍历到len(list)+1，但是由于list 一直在被pop ，所以序列长度在实时更新
#         sum=sum+1  #用来标便利到到原序列的那个编号了。
#         if (sum)%3==0:  #如果这个编号 为3 则 执行pop 动作
#             List.pop(i-1-t)  # i-1-t 来定位pop前该编号的索引位置
#             t=t+1  #用来记录当前被删除的元素个数，辅助定位下一个被删元素的位置
#
#     if len(List)==1:
#         print("最后留下的是原来第%d号的那位" % List[0])
#         break


# def ysf(n,k,m):
#     list1 = list(range(1,n+1))  #生成一个 序列
#     t = k-1
#     for i in range(n-1):
#         t = (t+m-1)%len(list1)
#         list1.pop(t)
#     print(list1[0])
#
# ysf(34,1,3)   #一共34个人，从1 开始数，数到3 出局

#该方法的解题思路：通过找每次出列人的规律 然后通过循环来删除这些出列元素即可
def joseph(total, begins, count):
  queue = list(range(1, total + 1))
  death = (begins + count - 2) % len(queue)  #定义第一个出列的人的索引位置
  for times in range(total - 1):
    print('out: ', queue[death])  #输出每次循环时出列的编号
    del queue[death]  #将该元素删除，后续元素自动补齐
    death = (death + count -1) % len(queue)
  print('survivor: ', queue[0])

joseph(7,1,3)



