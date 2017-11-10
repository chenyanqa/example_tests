#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#学习使用按位与 & 。

# print(bin(3))  #将整数转换为二进制
# print(bytes(3))  #将整数转换为字节流


if __name__ =='__main__':
    a = 5
    b = a & 3   # 与运算：按二进制位 取相同的 为1
    print(b)
    print(a | 3)   # 或运算：按二进制位 取不同的 为1

