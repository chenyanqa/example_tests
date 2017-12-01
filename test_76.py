#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
def test_oushu(n):
    i = 0
    s = 0.0
    for i in range(2,n+1,2):   #初始值为2及间隔2 来表示偶数
        s +=1.0/i
    return s


def test_jishu(n):
    i = 0
    s = 0.0
    for i in range(1, n + 1, 2):  # 初始值为1及间隔2 来表示奇数
        s += 1.0 / i
    return s

def test(n):
    if n % 2 ==0:
        print(test_oushu(n))  #调用函数时，如果直接return的数据 还需要在print 一下才能显示出来
    else:
        print(test_jishu(n))


if __name__ == '__main__':
    n = int(input('请输入一个数：'))
    test(n)




