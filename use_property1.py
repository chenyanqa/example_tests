#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# class Student(object):
#
#     # def get_score(self):
#     #     return self._score
#     #
#     # def set_score(self,value):
#     #     if not isinstance(value,int):
#     #         raise ValueError('score must be an integer')
#     #     if value <0 or value >100:
#     #         raise ValueError('score must between 0-100!')
#     #     self._score = value
#
#     @property  #把一个getter方法变成属性，同时@property本身被调用后，会同时生成一个装饰器 @score.setter,负责把setter方法变成属性
#     def score(self):
#         return self._score
#
#     @score.setter  #这个装饰器如果不定义的话 则表示score方法仅为可度的。否则 则为可读写的@property
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer')
#         if value <0 or value >100:
#             raise ValueError('score must between 0-100!')
#         self._score = value
#
#
# s = Student()
# ##为了程序安全，不让外界随便访问类的属性 因此可以通过设置set 和get方法 供外界调用
# # s.set_score(60)
# # print(s.get_score())
#
# #增加@property及对应的.setter 装饰器，可以让对应的get、set方法变成属性 ，更加方便外界调用
#
# s.score = 100
# #s.score = 1000
# print(s.score)


#习题：请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('值设置出错')
        else:
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('值设置出错')
        else:
            self._height = value


    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print('resolution = ',s.resolution)
if s.resolution == 786432:
    print('测试通过！')
else:
    print('测试失败！')

