#!/usr/bin/env python  #这行注释可以让.py文件直接在linux、mac等其他平台上运行
# -*- coding:utf-8 -*-

# 'a test module'   #表示模块的文档注释
#
# __author__ = 'chen yan' #表示模块的作者   以上4行 表示python模块的标准模板
#
# import sys #引入sys模块，就有了sys变量指向该模块， 可以访问sys模块下的所以功能
#
# def test():
# 	args = sys.argv #sys模块下 有个argv的变量，用来存储从命令行接受的所有参数
# 	if len(args) == 1:  #argv至少会有一个元素，为该.py文件的名称，即argv[0]
# 		print('Hell0,world!')
# 	elif len(args) == 2:
# 		print('Hello,%s' % args[1])
# 	else:
# 		print('too many arguments!')
#
# '''
# 该if语句表示，如果当前程序自己在命令行执行时，此时解释器会将该入口设置为main，因此if语句成立，可以执行if里面的操作了，
# 如果程序A被当作模块引入到其他程序B中，此时其他程序B执行时，因为不是A程序的入口，因此if语句不成立，因此不会执行
# 程序A中的if语句中包含的操纵，因此if语句中的内容常用来运行测试，即调用当前函数（或者模块） 看运行是否正常
# '''
# if __name__ =='__main__':
# 	test()
#
# # import sys
# # a = sys.argv[0]
# # print (a)  #输出 D:/cy/example_tests/test_103.py




#函数变量作用域
def _private_1(name):  #私有函数
	return 'Hell0,%s' %name

def _private_2(name):  #私有函数
	return 'Hell0,%s' %name

def greeting(name):
	if len(name)>3:
		return _private_1(name)
	#这里是正常的函数调用，不是函数返回，1、函数返回 仅仅返回函数名，而不是执行结果 2、返回函数一般是返回内层函数，而不是外层函数的同级函数
	else:
		return _private_2(name)

print(greeting('chenyan'))
