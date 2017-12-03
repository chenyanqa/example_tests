#!/usr/bin/env python
# -*- coding:utf-8 -*-

#列表使用实例。

# list
# 新建列表 ，包含字符串，数字，列表
testList = [10086, '中国移动', [1, 2, 4, 5]]

# 访问列表长度
print(len(testList))

# 到列表结尾
print (testList[1:])

# 向列表添加元素
testList.append('i\'m new here!')
print (testList)

print (len(testList))
print (testList[-1])
# # 弹出列表的最后一个元素
print (testList.pop(-1))
print (len(testList))
print (testList)

# # 后面有介绍，暂时掠过
matrix = [[1, 2, 3],
		  [4, 5, 6],
		  [7, 8, 9]]
print (matrix)
print (matrix[1])

col2 = [row[1] for row in matrix]  # for row in matrix将分别返回3行数据，然后每行里面取第二个数据，因此相当于取了第二列
print (col2)

col2even = [row[1] for row in matrix if row[1] % 2 == 0]
#for row in matrix if row[1] % 2 == 0 每次先取一行数据，然后判断row[1] % 2 == 0是否符合，如果符合则返回row【0】，否则 不返回
print (col2even)