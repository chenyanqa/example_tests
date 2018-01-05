#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
1、python中经常会涉及到datetime 和timestamp，UTCtime 和本地时间的转换。其中 datetime类型 表示一种日期+时间的格式，例如
2017-12-29 14:06:46.135744，  timestamp时间戳类型，即当前时间相对于 1970年1月1日 00:00:00 UTC+00:00 的秒数，是一个纯数字的时间，
UTCtime ： 表示世界协调时间，即将时间时间分为24个时区，中国在东八区，然后
2、timestamp 是一个浮点数，没有时区的概念，但是datetime 有时区。本地时间一般时区当前操作系统的所在时区
北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间

3、datetime 通过 datetime对象调用 timestamp（）方法 转换为时间戳，  时间戳通过datetime类的fromtimestamp（t）转换为datetime
1） dt = datetime(2018,1,3,9,59)
    dt.timestamp()

2）t = 1514944740.0
   datetime.utcfromtimestamp(t)

4、字符串时间与datetime 的转换  #将给定的字符串时间按照指定格式读取为datetime
1）cday = datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S') #将'2015-6-1 18:19:59' 转换为datetime

2）now = datetime.now()
   now.strftime('%a,%b,%H:%M') -- 将datetime类型转换为字符串输出

5、datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。而时间戳可以表示任意时间。所以如果要存储datetime，最佳方
法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。



'''
from datetime import datetime,date,time


#1、datetime.now()

#datetime 是一个模块，该模块里面还包含一个datetime的类
now = datetime.now()  #获取当前的datetime 2017-12-29 14:06:46.135744（返回当前的日期+时间，类型为datetime）
#a = date.ctime(now)
print(now)
#print(a)


# 2、使用参数 构造一个datetime
dt = datetime(2017,12,29,14,31,30)
print(dt)   #输出 2017-12-29 14:31:30


#3、datetime转换为timestamp
#我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0，因此1970年以前的时间timestamp为负数
#当前时间就是相对于epoch time的秒数，我们城市为timestamp ，例如对应的北京时间为：timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
#timestamp 的值 与时区无关，且全球适用，因此计算机时间一般以timestamp表示

from datetime import datetime
dt = datetime(2018,1,3,9,59) #用指定日期 构造一个datetime
print(dt.timestamp())   #转换为时间戳 输出：1514944740.0

#4 timestamp 转换为datetime（本地时间）
from datetime import datetime
t = 1514944740.0
print(datetime.fromtimestamp(t))  #2018-01-03 09:59:00


#5、timestamp 转换成UTC标准时区
from datetime import datetime
t = 1514944740.0
print(datetime.fromtimestamp(t))  #2018-01-03 09:59:00 北京时间
print(datetime.utcfromtimestamp(t))  #2018-01-03 01:59:00  伦敦时间


#str 转换为datetime
from datetime import datetime
cday = datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')  #Y要大写，参数为一个datetime时间和其格式化字符串
print(cday)

print(type(cday))   #<class 'datetime.datetime'>
print(type('2015-6-1 18:19:59'))  #<class 'str'>

#datetime 转换为str
from datetime import datetime
now = datetime.now()
print(now)  #2018-01-03 11:25:07.855048
print(now.strftime('%a,%b,%H:%M'))  #Wed,Jan,11:25


#datetime 加减
from datetime import datetime,timedelta
now = datetime.now()
now1= now + timedelta(hours=10)
print(now1)
now2 = now1 - timedelta(days=1,hours=1)
print(now2)



#练习：假设你获取了用户输入的日期和时间如2015-1-21 9：01：30 以及一个时区信息 如UTC +5：00 均是str ，请编写一个函数将其转换为timestamp

from datetime import datetime,timedelta,timezone
def to_timestamp(dt_str,tz_str):

    tz_utc_5 = timezone(timedelta(hours=tz_str))  #创建一个时区对象
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S').replace(tzinfo=tz_utc_5) #将当前从字符串时间转换来的datetime强制转换为对应时区

    return dt.timestamp()

print(to_timestamp('2015-1-21 9:01:30',5))
print(to_timestamp('2015-6-1 08:10:30',7))

















