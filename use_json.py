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
pickle.dump(obj,file,protocal)      #该序列化方法 要求必须将obj 序列化后的数据写入文件


'''
import pickle  # 实现序列化模块

#dict={"name":"python","english":33,"math":35}
d = dict(name = 'Bob',age=20,score=88)
# print(pickle.dumps(d,0))   # 0 表示本次使用的协议版本为ASII ，1表示老式的二进制，2 为新的二进制，效率更高 ,目前py3 中默认选中了 3协议
# print(pickle.dumps(d,2))
print(pickle.dumps(d,3))  #返回值为：  b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\0scoreq\x04KXu.'

f = open('dump.txt','wb+')
print(pickle.dump(d,f))   # 返回值为None
print(f.read())
f.close() 



