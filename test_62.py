#!/usr/bin/env python
# -*- coding:utf-8 -*-

#查找字符串。

str = 'abcsdjfk483453b'
str1 = 'jfk5'
print(str.find('b',1))  #从下标为1的位置 开始顺序查找，返回待查找字符串第一个字符的位置
print(str.find(str1))   #返回str1在str中第一个字符的位置，若不能完全匹配 则返回-1
print(str.index('53'))  #查看字符串'53'第一次出现的位置







