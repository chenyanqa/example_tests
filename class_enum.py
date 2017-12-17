#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#from enum import Enum #引入枚举模块
'''
1、__members__
     |      Returns a mapping of member name->value.
     |
     |      This mapping lists all enum members, including aliases. Note that this
     |      is a read-only view of the internal mapping.

2、http://www.cnblogs.com/ucos/p/5896861.html
3、查看类及实例属性的方法有2中，一种是 调用.__dict__  返回一个属性、值字典，一种是dir（）函数，返回一个list
4、__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了以个由所有父类组成的元组）
__class__ ：表示获取当前对象的类

5、type对象包含了很多关于对象的元信息：类型名字(tp_name)，创建该类型对象时分配内存空间大小的信息(tp_basicsize和tp_itemsize)，
一些操作信息(tp_call, tp_new等)，还有其他如__mro__(tp_mro), __bases__(tp_bases)等。
6、python中类也是一个对象（类即可继续创建实例），而这些类都type元类创建的，例如str是用来创建字符串对象的类，而type就是用来
创建类的类，类本身也是实例，当然，它们是元类的实例。
7、可以把元类称为“类工厂”（不要和工厂类搞混了:D） type就是Python的内建元类，当然了，你也可以创建自己的元类。
8、 # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象

9、一般 如果使用关键字class 定义类后，对解释器来说 仅仅是扫描下class的语法，然后自动调用type（）方法创建该class
因此可以 Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class 的方式手动创建类



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


#枚举支持迭代器，可以循环遍历 (__members__是一个特殊枚举的一个特殊属性)
for k,v in Weekday.__members__.items():  #__members__ 返回所有的枚举键值对
    print(k,'=>',v)

for i in Weekday:  #i 每次取值为weekday类的成员变量
    print(i,i.name,i.value)

#print(dir(Weekday))


dict = {'a':1,'b':2}
print(dict.keys())  #返回 dict_keys(['a', 'b'])
print(dict.values()) #返回 dict_values([1, 2])



#把Student的gender属性改造为枚举类型，可以避免使用字符串：
class Gender(Enum):  #将性别的值枚举出来，也就是实现先定义好，然后后续可以直接拿用户的输入来跟枚举值比较，就可以校验用户的输入了
    Male = 0
    Female = 1

class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

bart = Student('Bart',Gender.Male)
if bart.gender == Gender.Female:
    print ('测试通过')
else:
    print ('测试失败')

#print (type(Student))  #<class 'type'>
print (Student.__class__)  #<class 'type'>
print (type(bart)) #<class '__main__.Student'>
print (bart.__dict__)
print (Student.__dict__)
print (dir(bart))  #查看类及实例属性的方法有2中，一种是 调用.__dict__  返回一个属性、值字典，一种是dir（）函数，返回一个list




print ()
class A:
    def __init__(self,url):
        self.url = url
    def out(self):
        return self.url

a = A('news.163.com')
print (a.out())

b = a.__class__('www.bccn.net')
print (b.out())
print ()
print (A) #<class '__main__.A'> #表示对象A，
print (a) #<__main__.A object at 0x00000128A3E9A2E8> 表示a是A的对象
print ()
print (type(A)) #<class 'type'>
print (type(a)) #<class '__main__.A'>  ##获取当前对象的类
print ()
print (A.__class__) #<class 'type'>
print (a.__class__) #<class '__main__.A'>  #获取当前对象的类