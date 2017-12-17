#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
1、编写单元测试时，我们需要编写一个测试类以Test开头，从unittest.TestCase继承。
2、以test开头的方法就是测试方法，例如：test_xxx()方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
3、由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。
最常用的断言就是assertEqual()，assertTrue(),例如：self.assertEqual(abs(-1), 1) 判断是否相等
4、另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：
例如：with self.assertRaises(KeyError):
    value = d['empty']

5、with 语句是python2.5开启引入的一种异常处理相关的功能，with适用于对资源进行访问，确保不管使用过程中是否发生异常，都会执行
退出以及一些资源的清理，释放过程， 比如说文件使用后自动关闭，线程中锁的自动获取和释放等，参考文档：
http://python.jobbole.com/82494/

with context_expression [as target]:
	with-body

#with语句一旦执行到open(r'somefileName')，就会生产一个上下文管理器，该管理器有个__enter__() 和 __exit__() 方法，通过调用
__enter__()方法，并将返回值赋给 somefile，然后执行for语句，此时不管for语句是否报错，都会执行__exit__()方法，清理和释放资源
with open(r'somefileName') as somefile:
    for line in somefile:
        print line

6、setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()
方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：

7、一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：
if __name__ == '__main__':
    unittest.main()

    另一种方法是在命令行通过参数-m unittest直接运行单元测试：
$ python -m unittest mydict_test

'''

# import unittest
#
# from mydict import Dict #从某个文件（模块）引入待测试的主类
#
# class TestDict(unittest.TestCase):  #定义测试主类，一般以Test开头，默认继承unittest.TestCase类
# 	def test_init(self):  #定义测试方法，一般以test开头，测试被测类的构造方法
# 		d = Dict(a =1,b ='test')  #先调用被测主类生产一个实例，然后使用这个实例去操作被测类，观察响应是否正常
# 		self.assertEqual(d.a,1)  #各种断言
# 		self.assertEqual(d.b,'test')
# 		self.assertTrue(isinstance(d,dict)) #d是父类dict的一个实例
#
# 	def test_key(self): #由于这个测试方法的目的是测试key的情况，所有通过dict['key']的方法赋值，然后通过实例调属性的方式访问
# 		d = Dict()  #每个测试方法都需要创建一个 被测类的对象
# 		d['key'] = 'value' #相当于增加了一个键值对
# 		#print(d)  #{'key': 'value'}
# 		self.assertEqual(d.key,'value')
#
# 	def test_attr(self):#由于这个是测试类属性的情况，因此可以通过实例.属性的方法赋值，然后判断通过dict['key']的方式访问
# 		d = Dict()
# 		d.key = 'value'
# 		self.assertTrue('key' in d) #这里的d 表示一个字典实例
# 		self.assertEqual(d['key'],'value')
#
# 	def test_keyerror(self): #断言如果访问的key值不存在时，是否会报错
# 		d = Dict()
# 		with self.assertRaises(KeyError): #断言是否会抛出指定错误。with是一种异常处理机制
# 			#print(self.assertRaises(KeyError)) #<unittest.case._AssertRaisesContext object at 0x000001F53F9AB630>
# 			value = d['empty']
# 			#d['empty'] = 'value' #这里如果这么写，则抛出AssertionError: KeyError not raised，这是因为这样写 相当于实在赋值
# 			#会生产一个{empty:'value'}的键值对
#
# 	def test_attrerror(self):
# 		d = Dict()
# 		with self.assertRaises(AttributeError): #是AssertRaisesContext类的一个对象
# 			value = d.empty #由于empty这个属性没有被定义过，因此直接访问的时候  肯定会报错
#
# 	def setUp(self):  #setUp()和tearDown()方法会分别在每个测试方法执行前后调用
# 		print('setUp...')
#
# 	def tearDown(self):
# 		print('tearDown...')
#
# if __name__ == '__main__': #执行测试类的一般模式，相当于可以把mydict_test.py当做正常脚本运行
# 	unittest.main()


#练习题：对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：