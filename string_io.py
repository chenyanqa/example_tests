#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、StringIo表示内存中读写，且只能读写str，可以使用 .getvalue()获取数据流中的数据，也可以通过.readlines()读取
f = StringIO('Hello\nHi\nGoodbye')
print(f.getvalue())
s = f.readlines()  #['Hello\n', 'Hi\n', 'Goodbye']，

2、BytesIO  在内存中读取二进制文件
StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。

'''

# from io import StringIO
# f = StringIO()  #<_io.StringIO object at 0x101a5b5e8>
# print(f)
# f.write('hello')
# f.write(' ')
# f.write('world')
# print(f.getvalue()) #该方法将获取写入后的str
#

# from io import StringIO
# f = StringIO('Hello\nHi\nGoodbye')
# print(f.getvalue()) # 这个方法 可以直接获取StringIO流中的数据
# s = f.readlines()  #['Hello\n', 'Hi\n', 'Goodbye']，
# #print(s)
# for i in s:
#     print(i)



#BytesIO  在内存中读取二进制文件
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8')) #经过utf-8 编码为bytes
#f.write(b'hello')
print(f.getvalue())  #b'\xe4\xb8\xad\xe6\x96\x87'


from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87') #<_io.BytesIO object at 0x101316f10>,f 为BytesIO类的一个对象 、实例
print(f)
print(f.read())





