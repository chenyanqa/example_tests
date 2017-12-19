#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        s = Student('chenyan',90)
        self.assertEqual(s.name,'chenyan')
        self.assertEqual(s.score, 90)

    # def test_get_grade(self):
    #     s = Student('chenyan',50)
    #     self.assertEqual(s.get_grade(),'C') # 由于get_grade()是被测主类的方法，只有该类的实例可以调用

    def test_80_to_100(self):
        s1 = Student('Bart',80)  #会生成带属性名字和分数的 学生实例s1
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(),'A')  #s1.get_grade() 这个会把s1实例的属性等都传给方法get_grade()，然后这个方法根据自己的逻辑处理，返回对应结果
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart',60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(),'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self): #由于Student类中没有对异常输入进行判断，所以这个测试方法中的输入并没有报错，因此这个测试方法会报：断言失败
        s1 = Student('Bart',-1)
        s2 = Student('Lisa',101)
        with self.assertRaises(ValueError): #with是一种异常处理机制，执行with后面的语句后，会生成一个上下文管理器：带有进入和退出方法，
            s1.get_grade()  #实例s1调用get_grade()方法并会获得一个返回值，然后拿这个返回值跟assert断言对比，看是否一致

        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ =='__main__':
    unittest.main()


