#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
1、文件读写普通程序是无法操作的，只有操作系统有权限，而且文件的读写需要使用操作系统特点的接口
2、读文件：
1）使用内置的open（）函数，传入文件名（即文件路径）和标志符（即可读写模式，'r' 只读，'rw'可读写）
f = open('/Users/user/Desktop/test.rtf','r')
2）如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
f.read()-- 一次性读取全部内容，适合文件内容不是特别大的情况
f.read(size) --- 读取size个字节
f.readline() ---读取一行内容
f.readlines()--- 一次性读取所以内容并按行返回  如果 x = f.readlines() 将从文件f读取的内容保存在x 后，x也自动可以实现按行读取

3)f.close()

3、with机制下的文件读取
with open('/Users/user/Desktop/test.rtf','r') as f:
    print(f.read())

4、像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义
流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。

5、一般的文件读取都是针对文本文件，但是也有图片，视频等二进制的文件读取，读取模式为'rb'

6、一般文件默认读取utf-8编码格式的，如果需要读取非utf-8模式的文件，需要给open（）函数 额外传一个encoding 参数
open('/Users/user/Desktop/test.txt','r','encoding = gbk')

7、可能有些文件编码并不规范，因此可能会吹按UnicodeDecodeError的报错，可以通过open（）函数的 errors参数 设置遇到错误的出来方式
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

8、文件读写默认
1）r表示 打开只读文件，但是文件必需存在
2）w 表示打开只写文件，若文件不存在则创建，若文件中含有内容，则覆盖原有内容
3）a 表示以追加的方式打开只写文件，文件不存在则创建，存在，则追加内容
4）r+ 表示可读写文件，但文件必需存在
5）w+ 表示可读写
6）a+ 表示可读写
7）rb 表示打开二进制文件（图片、视频等）
8）wb 表示可写的二进制文件
'''
#
# f = open('/Users/user/Desktop/test.rtf','r') #如果文件不存在的话：FileNotFoundError: [Errno 2] No such file or directory: '/Users/user/Desktop/test1.rtf'
# print(f.read()) #read() 表示可以一次读取文件全部内容，并保持到一个str对象中
# f.close() #文件使用后需要关闭，以免浪费资源，占用内存


#文件读写时 一旦出错，后面的文件 close（）就不会被调用到，因此可以引入with 异常处理机制，确保不论中间代码段是否出错，都能正确关闭文件,且
#由于with的异常处理机制，会自动执行上下文管理器的 __exit__()方法，所以无需调用f.close()代码
# with open('/Users/user/Desktop/test.rtf','r') as f:
#     #print(f.read())
#     for line in f.readlines():
#         print(line.strip())


#二进制文件读取，文件模式为默认的 UTF-8

# with open('/Users/user/Desktop/image004.png','rb') as f:
#     print(f.read())  #输出 b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00  十六进制字节流
#
#
# #读取非UTF-8编码，需要给open（）函数 传入encoding参数
# with open('/Users/user/Desktop/text.txt','r',encoding = 'gbk') as f:
#     print(f.read())
#
#
#
# #如果在读取文件过程中 遇到错误，可以使用open（）函数的 errors 指定出来方式
# with open('/Users/user/Desktop/text.txt','r',encoding = 'gbk',errors='ignore') as f:
#     print(f.read())

#
# #写文件
# with open('/Users/user/Desktop/test1.txt','w') as f:  #如果该文件不存在，则会按照指定路径创建
#     f.write('sajdfshfsahfshdfshf')



#练习题：请将本地一个文本文件读为一个str 并替换某些字符然后重新写入
filename ='/Users/user/Desktop/test1.txt'
with open(filename,'r+') as f:  #注意可读写模式为r+  而不是rw
    x = f.readlines()  #将源文件读取的全部内容存放在x 中,且后续可以按行返回内容
    #x = f.read()  #一次性返回全部内容，没有按行返回的特点
    with open(filename,'w'): #以写的默认打开文件 即可清空原文件
        pass

    for line in x:  #实现替换过程  替换一行然后立马写入
        s = line.replace('hello','hi')
        with open(filename,'a') as f:
            f.write(s)






