#!/usr/bin/env python
# -*- coding:utf-8 -*-

#暂停一秒输出，并格式化当前时间。
import time   #time模块更多的是跟操作系统 底层打交道
#import datetime  #datetime 更多的是跟用户 应用展示层打交道
from datetime import datetime #由于datetime模块中还包含一个datetime类  如果要用到具体类的话。可以采用此模式

# print(time.time())  #输出时间戳
# print(time.localtime(time.time()))  #将时间戳格式化为本地时间
#
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) #对本地时间进行格式化为一个时间元组
#
# print(time.strftime('%Y-%m-%d %H:%M:%S')) #也可以不加参数
# print(time.ctime(time.time())) ##表示接收一个时间戳 并返回一个 可读形式为“Thu Oct 26 13:27:00 2017”的格式
# print(time.asctime(time.localtime(time.time()))) #表示接收一个时间元组 并返回一个 可读形式为“Thu Oct 26 13:27:00 2017”的格式

print(datetime.now().strftime('%Y.%m.%d %H:%M:%S'))  #datetime是模块，里面还包含一个datetime类