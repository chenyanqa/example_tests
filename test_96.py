#!/usr/bin/env python
# -*- coding:utf-8 -*-

#计算字符串中子串出现的次数。
# s = 'is ansfd dfdfj iifdfdkjfa sdfj'
# print (s.count('d'))


if __name__ == '__main__':
    str1 = input('请输入一个字符串:\n')
    str2 = input('请输入一个子字符串:\n')
    ncount = str1.count(str2)
    print (ncount)