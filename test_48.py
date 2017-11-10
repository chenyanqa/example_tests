#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#数字比较。

def compare(a,b):
    if a > b:
        print('%d > %a'%(a,b))
    elif a == b:
        print('%d = %a' % (a, b))
    else:
        print('%d < %a' % (a, b))

compare(3,10)
