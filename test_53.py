#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#学习使用按位异或 ^
if __name__ == '__main__':
    a = 77
    b = a ^ 3
    print('The a ^ 3 = %d' % b)
    b ^= 7
    print('The a ^ b = %d' % b)