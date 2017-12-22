#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：d = dict(name='Bob', age=20, score=88)
可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，
下次重新运行程序，变量又被初始化为'Bob'。我们把变量从内存中变成可存储或传输的过程称之为序列化

2、序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化
，即unpickling。

3、pickle提供了一个简单的持久化功能。可以将对象以文件的形式存放在磁盘上。python中几乎所有的数据类型（列表，字典，集合，类等）都可以
用pickle来序列化，序列化后的数据以二进制流的形式展示，可读性查
4、pickle.dump(obj, file, [,protocol])
　　注解：将对象obj保存到文件file中去。
　　　　　protocol为序列化使用的协议版本，0：ASCII协议，所序列化的对象使用可打印的ASCII码表示；1：老式的二进制协议；2：2.3版本引入的新二进制协议，较以前的更高效。其中协议0和1兼容老版本的python。protocol默认值为0。
　　　　　file：对象保存到的类文件对象。file必须有write()接口， file可以是一个以'w'方式打开的文件或者一个StringIO对象或者其他任何实现write()接口的对象。如果protocol>=1，文件对象需要是二进制模式打开的。

　　pickle.load(file)
　　注解：从file中读取一个字符串，并将它重构为原来的python对象。
　　file:类文件对象，有read()和readline()接口。
5、序列化：
pickle.dumps(obj,protocal)     #以字节对象形式返回封装的对象，不需要写入文件
pickle.dump(obj,file,protocal)  #该序列化方法 要求必须将obj 序列化后的数据写入文件  ，且file 必须以'wb'先打开

6、反序列化
pickle.loads()-- > 直接将一个Bytes对象反序列化
pickle.load(f)---> 打开一个保存了bytes的文件，然后反序列化文件里面的内容。

7、如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个
字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
Python内置的json模块提供了非常完善的Python对象到JSON格式的转换


8、总结：python中 序列化的两种方法
1）内置的pickle （序列化为Bytes）、json模块（序列化为标准JSON串）
2）序列化：pickle.dumps(obj)-- 传入一个待序列化对象即可，返回一个bytes对象（字节流），无需进行文件操作
          pickle.dump(obj,file)  -- 需要先打开一个文件，然后将序列化后的bytes流写入到文件中（需要同文件操作结合）
3）反序列化：即将bytes对象或者JSON串 转化为 python对象
4) 类实例 不能通过json直接序列化或者反序列化，而是分别需要通过default 和object_hook 参数来定制
例如：
std_data = json.dumps(s, default=lambda obj: obj.__dict__) #类序列化为json串

rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score'])) #json串反序列化为对象



'''
import pickle  # 实现序列化模块
  #序列化
#dict={"name":"python","english":33,"math":35}
d = dict(name = 'Bob',age=20,score=88)   #将一个元祖字典化

# print(pickle.dumps(d,0))   # 0 表示本次使用的协议版本为ASII ，1表示老式的二进制，2 为新的二进制，效率更高 ,目前py3 中默认选中了 3协议
#print(pickle.dumps(d,2))
#print(pickle.dumps(d,3))  #返回值为：  b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\0scoreq\x04KXu.'

#通过将序列化后的内容写入文件和从文件读取操作

# f = open('dump.txt','wb+')
# print(pickle.dump(d,f))   # 返回值为None
# f.close()
#
# #反序列化：
# f = open('dump.txt','rb') #打开一个'rb'模式文件
# d = pickle.load(f)  #直接从一个file对象中反序列化
# f.close()
#
# print(d)


#直接通过Bytes对象操作

# b = pickle.dumps(d) # 将字典d 序列为Bytes对象，并赋给b
# print(b)
# print(type(b)) # <class 'bytes'> 字节流对象
# d = pickle.loads(b) #将Bytes对象b 反序列化
# print(d)
# print(type(d))  #<class 'dict'>




#使用内置的json模块实现序列化1
# import json
# d = dict(name='Bob',age=20,score=88)
# json_str = json.dumps(d)
# print(json_str)  #'{"name": "Bob", "age": 20, "score": 88}' ,json.dumps(d)返回一个字符串，字符串里面的内容是标准JSON
# print(type(json_str)) #<class 'str'>,json模块将对象序列化后返回一个字符串，但这个字符串里面包含很多内容（例如，字典、序列等），试想下平时抓包接口返回
#
# dict = json.loads(json_str)
# print(dict)
# print(type(dict)) #json模块将JSON串 反序列化后，返回一个python对象，例如dict等


#通过文件的方式保存序列化结果
# import json
# # d = dict(name='Bob',age=20,score=88)
# # f = open('json_str.txt','w+')
# # json.dump(d,f)
# # f.close()
#
# f = open('json_str.txt','r')
# d = json.load(f)
# print(d)
# f.close()


# python中一般的dict等对象可以直接转换为JSON串，但是类实例默认是无法直接序列化为JSON串
#类对象转换为JSON串：
# import json
# class Student(object):
#     def __init__(self,name,age,score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# s = Student('Bob',20,88)
# #print(s) #<__main__.Student object at 0x101464d68>  " _main__.Student"表示类Student的全称
# #print(json.dumps(s))  #直接转换时 会报错,因为默认情况下dumps（）方法不知道如何将实例转换为{} ：TypeError: Object of type 'Student' is not JSON serializable
#
# def student2dict(std):
#     return {
#         'name':std.name,
#         'age':std.age,
#         'score':std.score
#     }
#
# #json.dumps(obj,default=None)
# #If specified, default should be a function that gets called for objects that can’t otherwise be serialized. It
# # should return a JSON encodable version of the object or raise a TypeError. If not specified, TypeError is raised.
#
# #方法一：通过 函数实现 类实例的序列化
# print(json.dumps(s,default=student2dict))  #通过定义个 student2dict函数来实现将实例转换为{}，然后将该函数当成参数传递给dumps（），相当于一个高阶函数
#
#
# #方法二：通过lambda 函数及实例本身的__dict__ 属性 提取为{}的形式
# g = lambda obj:obj.__dict__    #这个匿名函数 前面的obj 表示形参对象，后面的 obj.__dict__ 表示将该达表示的内容返回
# print(g(s))
#
# # g = lambda x:x+2    #这个匿名函数实现的功能是 将传入的参数+2 后返回，冒号前面的x 表示形参，冒号后的（x+2）表示具体操作的表达式
# # print(g(3))   #通过将匿名函数赋值给 g 然后通过g(3) 调用函数并传入参数3




#反序列化：将JSON串或者dict 转换为类的实例

import json
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score


json_str ='{"name": "Bob", "age": 20, "score": 88}'
#d = {"name": "Bob", "age": 20, "score": 88}

def dict2student(d):  #传入一个字典，并将字典值 转换为类的实例
    return Student(d['name'],d['age'],d['score'])

print(json.loads(json_str,object_hook=dict2student))   #object_hook函数先会把传入的字符串转换为dict 然后传给函数dict2student

#TypeError: the JSON object must be str, bytes or bytearray, not 'dict'



#练习题
import json

obj = dict(name ='小明',age=20)
#s = json.dumps(obj,ensure_ascii=True)  #{"name": "\u5c0f\u660e", "age": 20}
s = json.dumps(obj,ensure_ascii=False)  #{"name": "小明", "age": 20}
#s = json.dumps(obj)  #{"name": "\u5c0f\u660e", "age": 20}
print(s)