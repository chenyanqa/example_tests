#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、it而tools 提供了 几个无限迭代器，例如itertools.count(1),itertools.cycle('ABC'),itertools.repeat('A',10)
2、itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。
'''
import itertools

# natuals = itertools.count(2)  #count(start=0, step=1) --> count object
# for n in natuals:
#     print(n)


#通过 takewhile（）-高阶函数截取有限序列
natuals = itertools.count(1,2)  #表示无限迭代器的第一个数为1，步长为2（步长：为前后两个数相减的值）
ns = itertools.takewhile(lambda x:x <= 10,natuals) #takewhile（）的第一个参数为一个匿名函数，表示返回<=10的数，第二个参数，表示取值序列
print(ns) #<itertools.takewhile object at 0x101c4fa88>
print(list(ns))


# chain() 可以把一组迭代对象串联起来，形成一个更大的迭代器
'''
class chain(builtins.object)
 |  chain(*iterables) --> chain object
 |  
 |  Return a chain object whose .__next__() method returns elements from the
 |  first iterable until it is exhausted, then elements from the next
 |  iterable, until all of the iterables are exhausted.

'''
for c in itertools.chain('ABC','XYZ','123'): #chain(*iterables)内置类 首先要求参数是可以跌单对象，然后会将当前参数中的可迭代对象串联起来
    print(c)

print(itertools.chain('ABC','XYZ','123'))  #<itertools.chain object at 0x1014625c0>
print(itertools.chain('ABC','XYZ','123').__next__())
print(list(itertools.chain('ABC','XYZ','123'))) #['A', 'B', 'C', 'X', 'Y', 'Z', '1', '2', '3']


#groupby() 将迭代器中 按照元素分组，例如
'''
A ['A', 'A', 'A']
B ['B', 'B', 'B']
C ['C', 'C']
A ['A', 'A', 'A']
E ['E']

class groupby(builtins.object)
 |  groupby(iterable[, keyfunc]) -> create an iterator which returns
 |  (key, sub-iterator) grouped by each value of key(value).

'''
for key,group in itertools.groupby('AAABBBCCAAAE'):
    print(key,list(group))

print(itertools.groupby('AAABBBCCAAAE')) #<itertools.groupby object at 0x1018b7c78>
print(itertools.groupby('AAABBBCCAAAE').__next__()) #('A', <itertools._grouper object at 0x101c627f0>)

for key,group in itertools.groupby('AaaBBbcCAAa'):
    print(key,list(group))
'''
A ['A']
a ['a', 'a']
B ['B', 'B']
b ['b']
c ['c']
C ['C']
A ['A', 'A']
a ['a']
'''

for key,group in itertools.groupby('AaaBBbcCAAa',lambda a:a.lower()):
    #这个lambda a:a.lower() 函数仅仅影响key值，例如此处将key值都转成小写，然后相邻的A和a 就会分成一组，其子迭代器也会串联成一个
    print(key,list(group))

'''
a ['A', 'a', 'a']
b ['B', 'B', 'b']
c ['c', 'C']
a ['A', 'A', 'a']
'''



#练习：计算圆周率可以根据公式，利用Python提供的itertools模块，我们来计算这个序列的前N项和：
'''
解题思路
1、截取两个整数序列和负数迭代器，然后串联成一个迭代器，然后求和
2、使用cycle(4,-4) 创建一个迭代器去跟对应序列相乘，得到一个正负序列 然后求和

3、需要注意的是，在迭代器中不能让两个迭代器公用一个数据源迭代器，因为迭代器在一个程序中 只能循环读取一次，因为当前一个迭代器读取该
数据源后，第二个迭代器就读不到数据了

'''
import itertools

def pi(N):

    n1 = itertools.takewhile(lambda i: i <= N, itertools.count(1,4)) #截取该序列的前N项，其中需要从natuals中刷选出lambda函数为真的值
    #print(list(n1)) #[1, 5, 9]
    n2 = itertools.takewhile(lambda i: i <= N, itertools.count(3,4))
    #print(list(n2)) #[3, 7]

    n2 = itertools.chain(map(lambda i:4/i,n1),map(lambda i:-(4/i),n2))
    #print(list(n2))  #[4.0, 0.8, 0.4444444444444444, -1.3333333333333333, -0.5714285714285714]
    return sum(list(n2))


print(pi(20))  #3.0418396189294024


# def pi(N):
#     natuals  = itertools.count(1, 2)
#     p = itertools.takewhile(lambda x : x < 2*N, natuals)
#     s = 0
#     a = 4
#     for i in p:
#         s = s + a / i
#         a = -a
#     return s
#
# print(pi(10))  #3.0418396189294032



