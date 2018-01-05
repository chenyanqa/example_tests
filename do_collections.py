#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、collections 是python内建的一个集合模块，提供了很多有用的集合类
2、namedtuple('名称'，[属性list])   用来创建一个tuple对象，并规定tuple元素的个数

'''

#内建函数1：namedtuple（）
#引进原因：可以实现类似 类的部分功能，但是代码量少。
from collections import namedtuple

Point = namedtuple('Point',['x','y'])  #通过 namedtuple（）创建一个名字为 Ponit的元祖
p = Point(1,2) #给元组赋初值
print(p.x,p.y)  #通过属性读取元组的值


Circle = namedtuple('Circle',['x','y','r'])
c = Circle(1,2,3)
print(c.r)

#内建函数2：deque（）
#为了解决list（线性存储）数据量大的时候，插入删除效率底下的问题，deque可以实现高效的插入，删除操作的双向列表，适合队列和栈
#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
from collections import deque
q = deque(['a','b','c'])
q.append('x')  #默认从队列的右边即末尾进行追加和删除操作
q.appendleft('y')  #可以最序列左侧进行追加和删除操作
print(q)

#内建函数3：defaultdict（）
#引入理由：使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
#除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。

from collections import defaultdict
dd = defaultdict(lambda : 'N/A')   #lambda 冒号前面为参数，后面为表达式

#dd = defaultdict() #dict的默认值 必需通过调用函数返回
dd['key1'] = 'abc'
print(dd['key1'])

print(dd['key2'])  #key2本身是不存在的，但是因为dd 定义了defaultdict（），则会返回默认值


#内建函数4：OrderedDict
#引入原因：由于普通的dict ，key是无序的，因此做迭代遍历时，Key的顺序无法确定，为了保持Key的固定排序(即 按照插入的顺序返回)，可以用OrderedDict
#其次可以实现先进先出 ，当容量超出限制时，删除最早添加的key
from collections import OrderedDict
d = dict([('b',1),('c',10),('a',5)])
#d = dict('a','b','c')  #TypeError: dict expected at most 1 arguments, got 3
#d = dict((('a',1),('b','c')))
print(d)
od = OrderedDict([('b',1),('c',10),('a',5)])
print(od)
od['z'] =1
od['y'] =2
od['x'] =3
print(od)



#内建函数4：Counter （计数器，统计每个字符出现的个数-以dict的形式展示）
from collections import Counter
# c = Counter()  # 这个对象会将统计的结果（每个元素及对应出现次数） 以字段的形式存储起来
# print(type(c))  #<class 'collections.Counter'>
# print(isinstance(c,dict))  #True ，说明Counter类的实例同时也是一个字典
#
# for s in 'programing':
#     c[s] = c[s]+1  # 由于c 是一个字段，所以可以使用dict['key']的形式类读取元素，并输出元素
#
# print(c)  #Counter({'r': 2, 'g': 2, 'p': 1, 'o': 1, 'a': 1, 'm': 1, 'i': 1, 'n': 1})


c = Counter('programing').most_common(3) #取前3个元素
print(c)  #[('r', 2), ('g', 2), ('p', 1)]



