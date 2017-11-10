#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#输出一个随机数。

import random

print(random.random())   #输出【0，1）之间的随机数
print(random.randint(0,9))  #输出【0，9】之间的随机整数
print(random.uniform(0,9))  #输出【0，9】之间的随机浮点数
print(random.randrange(10,20)) #输出【10，20）之间的随机整数

print(random.choice([1,2,'a','dd']))  #从序列中随机选择一个元素 作为随机数输出


p = ['python','is','a','b','b',2,5]
random.shuffle(p)   # 将序列打乱
print(p)

s = random.sample(p,5)  #从list中随机选取5个元素，作为一个片段返回
print(s)



