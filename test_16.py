#!/usr/bin/env python
# -*- coding:utf-8 -*-
#输出指定格式的日期。 使用datetime

import datetime  #以后datetime模块的引入优先这样写
#from datetime import datetime  这种引用格式会导致 后面创建date对象时 识别，不识别date（年，月，日）的格式
s = datetime.datetime.now()
#s = datetime.now().date()
print(s)

#时间格式化：
t = s.strftime('%Y/%m/%d %H:%M:%S')  #格式化
print(t)

print(s.strftime('%a')) #输出当前是周几的简称
print(s.strftime('%A')) #输出当前是周几的全称
print(s.strftime('%b')) #输出当前的月份
print(s.strftime('%c')) #输出当前的本地时间 例如Fri Oct 27 12:22:09 2017
print(s.strftime('%d')) #表示当前是一个月的那一天
print(s.strftime('%j')) #表示当前是一年中的那一天
print(s.strftime('%m')) #表示当前是一年中的那一月
print(s.strftime('%M')) #表示当前是一小时中的那一分钟
print(s.strftime('%p')) #表示当前是上午还是下午
print(s.strftime('%U')) #表示当前是一年中的那一周
print(s.strftime('%w')) #表示当前是一周中的第几天

#创建日期对象：
mybirthday_data = datetime.date(1987,11,16)  #date（）里面的格式默认安装年，月，日排列
print(mybirthday_data.strftime('%Y-%m-%d'))

#日期算术运算  timedelta(days=x,hours=x,seconds=x) 该函数表示一个时间差
mybirthday_data_nextday = mybirthday_data + datetime.timedelta(days=1)
print(mybirthday_data_nextday.strftime('%Y-%m-%d'))

#日期替换：
mybirthday_data_new = mybirthday_data.replace(year=mybirthday_data.year +1,month=mybirthday_data.month-1)
print(mybirthday_data_new.strftime('%Y.%m.%d'))
