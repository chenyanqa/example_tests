#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
其中time.time()返回的一个float型，是从1970年1月1日0时起到当前经过的秒数，注意这里是分时区的
time.localtime()返回的是一个time结构体，其中包括tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec,tm_wday,
tm_yday,tm_isdst=0（夏令时间标志）
time.ctime() 作用  接收一个时间戳 并返回一个可读的模式
'''

#题目：时间函数举例1。
import time
print (time.ctime(time.time()))  #将当前时间戳格式化,float型数据
#print (time.asctime(time.time())) TypeError: Tuple or struct_time argument required
print (time.asctime((time.localtime((time.time()))))) #将当前的localtime 元组 格式化