#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def get_grade(self):  #这种含判断区间的 已定要把取值范围限定到具体的区间，且需要考虑异常取值
        if 60<= self.score < 80:
            return 'B'
        elif 100>= self.score >= 80:
            return 'A'
        elif 0 <= self.score <60:
            return 'C'
        else:
            raise ValueError('分数输入错误，应该在0-100之间')


