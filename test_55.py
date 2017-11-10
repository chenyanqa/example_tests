#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#学习使用按位取反~。
if __name__ == '__main__':
    a = 234
    b = ~a
    print('The a\'s 1 complement is %d' % b)
    a = ~a
    print('The a\'s 2 complement is %d' % a)

    print(~5)  # 5的二进制位 00000101  取反为11111010    https://www.cnblogs.com/piperck/p/5829867.html

    '''
    11111010  取反 0000 0101 ＋ 1 ＝ 0000 0110 加上符号- 0000 0110 = -6
    '''

