#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#题目：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
def str_length(str):
    n = len(str)
    return n

if __name__ =='__main__':
    s = input('请输入字符串：')
    print(str_length(s))



