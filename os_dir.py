#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、python内置的os模块也可以直接调用操心系统提供的接口函数，进入操作系统文件及目录
2、操作文件和目录的函数一部分放在os模块，一部分放在os.path模块中
3、os模块提供了对目录或者文件的新建/删除/查看文件属性，还提供了对文件以及目录的路径操作。比如说：绝对路径，父目录……  但是，
os文件的操作还应该包含移动 复制  打包 压缩 解压等操作，这些os模块都没有提供。这些由shutil模块补充
4、dst是destination的缩写，表目的   src是source的缩写，表源

'''

# import  os
# # print(os.name) #获取操心系统类型，'posix' 表示linux、max os
# # print(os.uname()) #获取系统 详细信息
#
# # print(os.environ) #查看全部环境变量
# # print()
# # print(os.environ.get('PATH')) #查看path环境变量
#
# print(os.path.abspath('.'))  #获取当前目录的绝对路径
# print(os.path.abspath('test_01.py')) #获取文件'test_01.py'的绝对路径
#
# #在某个目录下创建一个新目录，首先把新目录的完整路径表示出来，仅仅用来显示join后的路径
# print(os.path.join('/Users/user/Documents/python/','testdir')) #路径合成
# print(os.path.split('/Users/user/Documents/python/example_tests/test_01.py')) #拆分路径 ('/Users/user/Documents/python/example_tests', 'test_01.py')
# print(os.path.splitext('/Users/user/Documents/python/example_tests/test_01.py'))#从文件后缀名开始分割，('/Users/user/Documents/python/example_tests/test_01', '.py')
# #print(os.mkdir('/Users/user/Documents/python/testdir1')) # 创建指定的路径
# #print(os.rmdir('/Users/user/Documents/python/testdir')) #被删除的这个路径不能是已存在的
#
#
# print(os.path.abspath('test1.txt'))
# #print(os.rename('text1.txt','test111222.py'))
#
# #print(os.rename('test111222.py','text1.txt')) #对文件重命名
#
# #print(os.remove('test111222.py')) #删除文件
#
#
#
# #shutil模块 提供系统文件及目录的 复制、打包、压缩、解压等操作，对os模块进行补充
#
# import shutil
# #f复制文件内容到另一个文件 src->dst
# # shutil.copyfile('test.txt','test_copy.txt')
# #
# # #列出当前目录下的所有目录
# # g = [x for x in os.listdir('.') if os.path.isdir(x)] # 变量x 的取值范围为os.listdir('.')，然后看x且符合os.path.isdir(x) 若符合则返回x
# # print(g)
# #
# # #列出当前目录下的所有python文件，os.path.splitext(x)[1]--》这个函数会将传过来的x目录或者路径从后缀名开始分割一个元祖，然后元祖的第二个元素存放后缀名
# # g1 = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# # print(g1)
#
# print(os.listdir('.'))   #累出当前目录下的所有内容：包括文件夹和文本文件 ['.DS_Store', '.git', '.idea', 'a.txt', 'b.txt', 'c.txt'...]
#


# 练习题1：利用os模块编写一个能实现dir -l输出的程序。
# import os
# def findfile(dir):
#     sourcePath = dir
#     for dirN in [x for x in os.listdir(dir)]:
#         newPath = os.path.join(sourcePath,dirN)
#         if os.path.isdir(newPath):
#             findfile(newPath)
#         if os.path.isfile(newPath):
#             if os.path.splitext(newPath)[1] == '.py':
#                 print(newPath)
#
# findfile('.')

# import os
# from datetime import datetime
#
# print('   Size  Owner id  Group id     Modes           Last Modified  Name')
# print('============================================================')
# for i in os.listdir('.'):
#     size = os.path.getsize(i)
#     owner = os.stat(i).st_uid
#     group = os.stat(i).st_gid
#     mode = os.path.stat.filemode(os.stat(i).st_mode) # Convert a file's mode to a string of the form '-rwxrwxrwx'
#
#     #lastmodify = datetime.fromtimestamp(os.stat(i).st_mtime).strftime('%Y-%m-%d %H:%M:%S')
#     lastmodify = datetime.fromtimestamp(os.stat(i).st_mtime)
#     name = i
#     print('%10d %s         %s         %s %s %s'%(size,owner,group,mode,lastmodify,name))



# import os
# g1 = [x for x in os.listdir('.') if os.path.isdir(x)]
# print(g1)
#
# g2 = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1].find('.txt')]
# print(g2)

# #获取文件的系统状态信息：权限模式(mode)，节点、设备、link（链路）、用户id、group id、大小、修改、创建时间等
# print(os.stat('/Users/user/Documents/python/example_tests/test_01.py')) #获取文件的系统状态信息
# print(os.stat('test_01.py'))
#
# print(os.listdir())
# print(os.listdir('.')) #二者 都表示当前文件所在的文件路径下
# print(datetime.fromtimestamp(1509356702))


#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

import os
# 实现文件查找功能
# des_path目标目录，keyword查找关键词
# def file_search(des_path, keyword, result=[]):
#     if os.path.isdir(des_path):  #先判断des_path 是否为文件目录
#         for x in os.listdir(des_path): #遍历这个目录下所有文件和目录
#             sub_path = os.path.join(des_path, x)  #拼接路径（）
#             # 如果是目录，递归
#             if os.path.isdir(sub_path):
#                 file_search(sub_path, keyword, result)
#             # 如果是文件，进行筛选
#             elif keyword in x:
#                 result.append(sub_path)
#     else:
#         print('文件错误，请输入一个可遍历的目录！')
#     return result
#
#
# print('开始文件搜索．．．')
# for file in file_search('/Users/user/Documents/python/example_tests/', 'text'):
# #for file in file_search('text1.txt', 'text'):
#     print(file)


def traversal_dir(current_path, str):  #传入一个路径和一个待查找字符串
    #print('current path %s' % current_path)
    files = []
    dirs = []
    try:
        files = [x for x in os.listdir(current_path) if os.path.isfile(os.path.join(current_path, x))] #获取目录所有文件
        dirs = [x for x in os.listdir(current_path) if os.path.isdir(os.path.join(current_path, x))] #获取目录所有目录
        #print(files)
        #print(dirs)
    except Exception as e:
        pass

    for x in files:
        if x.find(str) >= 0:  #x.find(str)返回的是一个index 就是首先找到这个str的索引位置，如果没有找到 则返回 -1
            print(os.path.join(current_path,x))

    for x in dirs:
        nextpath = os.path.join(current_path, x)
        #print('next path %s' % nextpath)
        traversal_dir(nextpath, str)  #递归调用，因为当前参数也是一个路径，然后在调用一下 函数本身，找到其下一层

traversal_dir('/Users/user/Documents/python/example_tests/', 'text')

#print('abcdefg'.find(''))





