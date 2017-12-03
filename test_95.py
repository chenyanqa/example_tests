#!/usr/bin/env python
# -*- coding:utf-8 -*-

#题目：字符串日期转换为易读的日期格式。

import time
from dateutil import parser

print(time.ctime(time.time()))
dt = parser.parse('Dec  3 18:41:45 2017')  #将各种字符串形式的时间转换为datetime格式
print (dt)