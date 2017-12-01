#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
def test_oushu(n):


    pass

def test_jishu(n):
    pass

def test(n):
    if n % 2 ==0:
        test_oushu(n)
    else:
        test_jishu(n)


if __name__ == '__main__':
    n = int(input('请输入一个数'))
    test(n)




