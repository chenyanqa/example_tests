#!/usr/bin/env python3
# -*- coding:utf-8 -*

#学习使用按位 或 |   （A 或者B为1时，结果为1，即A，B中只要有一个为1，则结果为1）

if __name__ == '__main__':
    a = 77
    b = a | 3
    print(bin(a))
    print('a | b is %d' % b)
    b |= 7
    print('a | b is %d' % b)
    print(3 | 5)   #A,B 中 只要其中一个为1 则结果为1
    print(3 & 5)   #A，B 两位都为1 ，则结果为1
    print(3 ^ 5)   #A，B两位不同 则为1，相同则为0

