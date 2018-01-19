#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import chardet

print(chardet.detect(b'Hello,world'))
#{'encoding': 'ascii', 'confidence': 1.0, 'language': ''} #confidence 置信度

data = '离离原上草，一岁一枯荣'.encode('gbk')
chardet.detect(data)
#{'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}