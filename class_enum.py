#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#from enum import Enum #引入枚举模块
'''
1、__members__
     |      Returns a mapping of member name->value.
     |
     |      This mapping lists all enum members, including aliases. Note that this
     |      is a read-only view of the internal mapping.
2、


'''
# import enum
# Month = enum.Enum('Month',('Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# print(Month.Jan.value)
#
# #Month = Enum('Month',('Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# # for name,member in Month._member_map_.items():
# #     print(name,'=>',member,',',member.value)


from enum import Enum,unique

@unique  # 这个装饰器 可以帮我们检查保证没有重复值
class Weekday(Enum):  #创建一个Weekday枚举类，继承Enum枚举类（注意enum是模块，不是类）
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    # Sat = 6  如果有重复值的话，会报错 TypeError: Attempted to reuse key: 'Sat'

day1 = Weekday.Mon  #(通过枚举成员访问,此处仅仅返回一个字典，具体值 还需要通过 .name/.value调用)
print(day1.name) #因为枚举默认返回的是name，value键值对，因此可以用name取名称，value取值
print(day1.value)

day2 = Weekday['Tue']  #，通过枚举成员的key访问将枚举类型就相当于是一群键值对，即字典
print(day2.name)
print(day2.value)

day3 = Weekday(6)  #通过枚举成员的值来访问
print(day3.name)
print(day3.value)


#枚举支持迭代器，可以循环遍历
for k,v in Weekday.__members__.items():  #__members__ 返回所有的枚举键值对
    print(k,'=>',v)

for i in Weekday:  #i 每次取值为weekday类的成员变量
    print(i,i.name,i.value)

#print(dir(Weekday))



dict = {'a':1,'b':2}
print(dict.keys())  #返回 dict_keys(['a', 'b'])
print(dict.values()) #返回 dict_values([1, 2])