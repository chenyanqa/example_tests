#!/usr/bin/env python
# -*- coding:utf-8 -*-
#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

import math
for x in range(1, 10000):
	y1 = int(math.sqrt(100+x))
	y2= int(math.sqrt(268 + x))
	if(x + 100 == y1*y1) and (x + 268 == y2*y2):
		print(x)