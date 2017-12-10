#!/usr/bin/env python
# -*- coding:utf-8 -*-


# print('sss','dd','dfadf') #一次性输入多个字符串
#
# print('100+200 = %d' %(100+200))
# print('100+200 = ',(100+200))
#
# a = 'ABC'  #解释器创建了 字符串"ABC"和变量'a'，并把a指向了'ABC'
# b = a      #解释器创建了 变量b，并把b也指向了'ABC'
# a = 'XYZ'  #解释器创建了 字符串"XYZ"，并把a指向了'XYZ'
# print(b)
#
# print(10/3)
# print(10//3)
# print(10%3)
#
#
# print('%02d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)
#
#
# t = ('a','b',[1,2])
# t[2][0] = 'x'
# t[2][1] = 'y'
# print(t)
#
# # sum = 0
# # for i in range(1,101):
# #     sum = sum +i
# #
# # print(sum)
#
# print(sum(list(range(1,101))))
#
#
# sum = 0
# n = 1
# while n < 101:
#     sum = sum +n
#     n = n+1
# print(sum)
#
# L = ['Bart', 'Lisa', 'Adam']
#
# for i in range(len(L)):
#     print('Hello,%s'%(L[i]))
#
#
# list1 = list(range(10))
# print(list1)
#
# print(list1[:5])
# print(list1[-5:])  #可以取到最后一个

# print([x*x for x in range(1,11)]) #列表生成式，生成的元素 x*x,x的取值范围 for循环
#
# # for i  in range(1,11):
# #     print(i*i,end=' ')
# print([x*x for x in range(1,11) if x%2==0]) # 进一步筛选出偶数 来生成
#输出 [4, 16, 36, 64, 100]
# print([m+n for m in 'ABC' for n in 'XYZ'])  #使用2层循环，生成全排列，第一个循环即为外层循环
#
# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# for k, v in d.items():
#     print(k, '=', v)
#
# print([k+'='+v for k,v in d.items()])
#
# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])
#
# x = 'abc'
# y = 123
# print(isinstance(x,str))
# print(isinstance(y,int))
#
# g = (x*x for x in range(1,11))   #生成器
# print(g)   #<generator object <genexpr> at 0x101c2bf10>
# #
# for i in g:
#     print(i)


# f = open('text1.txt','a+')
# #print(dir(f))
# f.write('30\n')
#
#
# f.seek(0)
# print(f.read())

# with open('text1.txt','r+') as f:  #这里只有些 "r+"文件才能被正常读出,因为这段代码 没有写入操作，所以不适合用w+、a+
#     for line in f:
#         print(line)
# '''
# 1、r+ 打开可读写的文件，该文件必须存在。
# 2、w+ 打开可读写文件，若文件存在则文件长度清为零，即该文件内容会消失。若文件不存在则建立该文件
# 3、a+ 以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留
# '''


#生成器函数
# def gensquares(N):
#     for i  in range(N): #当前i = 0 时，执行到yield i**2，先将i**2 的结果返回，同时将函数挂起，然后再次回来从yield后面的代码继续执行
#         yield i**2
#
# print(gensquares(5))  #输出<generator object gensquares at 0x101c2bf10> 一个对象，而不是直接的结果
#
# for i in gensquares(5):
#     print(i)


#生成器列表：
# squares = (x*x for x in range(5))
# print(next(squares))
# print(next(squares))

# print(sum(x*x for x in range(5)))  #对生成器求和
# print(sum([x*x for x in range(5)]))  #对列表求和

#enumerate(seq,start)函数
# seq = ['s','dsf','1','dafdsfsf','1']
#
# for i in enumerate(seq,1):  #enumerate(可跌打序列，起始位置) 函数将返回seq序列中 对应的元素及下标
#     print(i)


#生成器只能遍历一次
# '''
# 10
# 20
# 30
#
# '''
#
# def get_province_population(filename):
#     with open(filename) as f:   #filename 是形参
#         for line in f:
#             #print(int(line))   #仅仅是输出，但是没法讲line每次取到的值聚合，如果要聚合的话 还需要先定义一个空列表，然后每次调用append（）
#             yield (int(line)) #将每行数字返回并聚合，然后挂起函数
# gen = get_province_population('text1.txt')
# all_population = sum(gen)
# print(all_population)
#
# for i in gen:  #由于生成器 在一个程序中只能执行一次，所以第二次无任何内容输出
#     print(i)

# def triangles(n):
#     L = [1]
#     while len(L) < n:
#         yield L
#         L.append(0)
#         L = [L[i - 1] + L[i] for i in range(len(L))]
#
# for i in triangles(5):   #triangles(n)是可一个生成器对象，可迭代，类似list 这样的
#     print(i)


# list1 = [1,2,3,4,5,6,7,8,9]
#
# def f(x):
#     return x*x
#
# g = map(f,list1)   #map() 函数接收两个参数 函数名和可迭代集合，会将函数一一作用在集合的每一个元素上，并返回一个迭代器
# print(list(g))  #迭代器 是一个惰性序列

#
# from functools import reduce
# def add(x,y):
#     return x+y
#
# print(reduce(add,[1,2,3,4]))
#
# print(list(map(str,[1,2,3,4])))  #['1', '2', '3', '4']


#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# list1 = []
# for  i in range(3):
#     s = input('请输入姓名：')
#     list1.append(s)
# print(list1)
#
# #list1 = [s for s in  ]
#
# def name_uapper(s):
#     return s.capitalize()
#
# print(list(map(name_uapper,list1)))


# #Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# from functools import reduce
# def prod(x,y):
#     return x*y
#
# print(reduce(prod,list(range(1,5))))
#

# #利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# from functools import reduce
#
# def str2float(s):
#     def fn(x,y):  #定义一个适合reduce的函数参数
#         return x*10 + y
#
#     def char2int(c): #通过字段将字符转换为整数
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
#
#     dot_index = 0  #定义小数点的初始值
#     for i in s:   #这里的i 的取值是字符串s中的值的迭代,这个循环主要为了获取小数点的位置
#         if i == '.':
#             break
#         dot_index += 1  #i=1的时候，dot_index=1，i=2的时候 dot_index=1，i=3的时候 dot_index=3，i= . 的时候 跳出循环，后面代码不执行
#
#     s1 = s[:dot_index]   #截取整数部分   [0,3]取0,1,2
#     s2 = s[dot_index +1:] #截取小数部分  [4,~]取4,5,6
#
#     #print(list(map(char2int, s1)))  #这个语句如果放在return上 将不会被执行
#     return reduce(fn,map(char2int,s1)) + reduce(fn,map(char2int,s2))/pow(10,len(s2))
#     # map(char2int,s1) 返回一个迭代器（数据流）
#
# print(str2float('123.456'))
#
# #print(float('123.456'))


# #filter
# def not_empty(s):
#     return s and s.strip()   #s.strip() 表示删除空白符，包括'\n','\r','\t','',None等，s='123abc' s.strip('12') 标书删除s中的'12'
#
# print(list(filter(not_empty,['A  ',' ','B',None,''])))  #输出 ['A  ', 'B']
# #filter(函数，序列)，将函数一一作用于序列的每个元素，若符合则返回，不符合的元素不返回
#
# print(filter(not_empty,['A  ',' ','B',None,'']))  #<filter object at 0x101c46358> filter（）函数也是以迭代器的形式返回，返回的是一个惰性序列
#
#
# #用filter 求素数：
# def _odd_iter():
#     n =1
#     while True:
#         n = n +1
#         yield n   # 输出一个 从2 开始的无限序列，且数据以迭代器数据流的方式存储（惰性序列），需要使用list（）强制转换为序列
#
# def _not_divisible(n):
#     return lambda x:x % n >0 #筛选处所以不能被整除的数
#
# def primes():
#     #yield 2  #因为2是素数 ，先返回
#     it = _odd_iter()  #初始序列（2 ，~）
#     while True:
#         n = next(it)  #第一次循环：n =2
#         yield n  #将 2返回 并挂起程序，然后在继续执行yield后面的代码
#
#         it = filter(_not_divisible(n),it)
#         #此时 it为一个（2，~）的序列，_not_divisible(n)此处的n为2 ，将不能被2整除的数保留并返回，由于此处n是动态变化的，因此函数参数中需要指定n
#         # primes（）是一个生成器函数，因此会返回一个可迭代的数据流
#
# for n in primes():  # 打印迭代器中小于20的素数
#     if n < 20:
#         print(n)
#     else:
#         break

#
# def main():
#     for n in primes():
#         if n < 1000:
#             print(n)
#         else:
#             break
#
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)
#
# if __name__ == '__main__':
#     main()


# # 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
# def is_palindrome(num):
#     num_str = str(num)  #将整数转换为字符串
#     str_len = len(num_str)  #求某个数的长度
#     '''
#     1、当字符串长度为1时，k只能取0，如果num_str[0] != num_str[1-1-0] 则返回false
#     2、当字符串长度为2时，k可以取0，1，取1时 如果num_str[0] != num_str[2-1-0]，
#     取1时，如果num_str[1] != num_str[2-1-1]
#     '''
#     for k in range(str_len):   #这里的思路是拿到一个具体的数字去判断是否为回数
#         if num_str[k] != num_str[str_len - 1 - k]: #通过分析可以找到一个数字字符串左边的下标和右边下标的规律
#             return False
#     return True
# # 调用
# output = filter(is_palindrome, range(1, 1000))  #给filter（）的两个参数，一个是用来判断某个数 是否为回数的函数，另外一个参数为一个序列
# print('1~1000以内的回数:', list(output))  #由于filter（）函数返回一个可迭代的对象 因此需要使用list（）将其强制输出


#请sorted（）函数对列表按照姓名进行排序：
#方法1：使用函数定义
# L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
# def by_name(t):
#     return t[0]

# def by_score(t):
#     #return t[1]
#     return -t[1]  #在元素或者列表前面加个“- ” 表示排序反转，及从高到低排序
#
# print (sorted(L,key=by_name))
# #print (sorted(L,key=by_score,reverse=True))  #排序默认从低到高 ，将翻转参数设为true，则改为从高到低
# print (sorted(L,key=by_score))

#使用 operator.itemgetter()方法
# import operator
# L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
# print(sorted(L,key=operator.itemgetter(0))) ##itemgetter(0)用于获取对象L的第1个维度的数据 用来排序
# print(sorted(L,key=operator.itemgetter(1),reverse=True))

#使用lambda表达式
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L2 = sorted(L, key=lambda x : x[1],reverse=True)
# print(L2)

# import operator
# #operator  模块下的 itemgetter（）函数用于获取对象那些维度的数据
# a = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'C', 10)]
# print (sorted(a, key=operator.itemgetter(2),reverse=True))  #itemgetter(2)用于获取对象a的第三个维度的数据 用来排序

#利用闭包返回一个计数器函数，每次调用它返回递增整数：
#
# def createCounter():
#     fs = [0]  #定义一个序列，并赋一个初值
#     def counter():
#         fs[0] = fs[0]+1   #函数没执行一次 序列的值加1
#         return fs[0]
#     return counter    #createCounter()最后会返回一个函数
#
# print (createCounter()) #输出 <function createCounter.<locals>.counter at 0x000002BD08F08598>
# f = createCounter()
# # createCounter() 会得到一个counter（）的函数及相关参数，但并不是最终结果，只有再次调用f（）的时候 才是相当于在调用counter（）函数计算结果
# print(f(),f(),f(),createCounter())

# def createCounter():
#     n = 0
#     def counter():
#         '''
#         在python中 内存函数对外层作用域的变量只有可读权限，而nonlocal 可以是我们自由操作
#         外层作用域的变量，包括修改
#         '''
#         nonlocal n
#         n = n+1
#         return n
#     return counter
# f = createCounter()
# print (f(),f())
#


# gcount = 0
# def global_test():
#     print (gcount)
#
# def global_counter():
#     global gcount
#     gcount += 1
#     return gcount
#
# def global_counter_test():
#     print(global_counter())
#     print(global_counter())
#     print(global_counter())
#
# print (global_counter_test())
# print (global_counter_test())
# print (gcount)

# def make_counter():
#     count = 0
#
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter
#
# def make_counter_test():
#     mc = make_counter()
#     print(mc())
#     print(mc())
#     print(mc())
#
# print (make_counter_test())


# def lazy_sum(*args):
#     ax = 0
#     def sum():
#         nonlocal ax
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# f = lazy_sum(1,2,3,4)
# print (f())


#将匿名函数作为函数返回
# def build(x, y):
#     return lambda: x * x + y * y  #lambda 参数：对参数操作的表达式，这里如果用作返回值的话，参数默认使用外层函数的
#
# f = build(2,3)
# print (f())

#也可以将参数放在 匿名函数中
# def build():
#     return lambda x,y: x * x + y * y
# f = build()
# print (f(2,3))


# def is_odd(n):
#     return n % 2 == 1
#
# L = list(filter(is_odd, range(1, 20)))

L = list(filter((lambda n: n%2 ==1),range(1,20)))
print(L)