#!/usr/bin/env python
# -*- coding:utf-8 -*-

#题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。
import time
import random

if __name__ =='__main__':
	isplay = input('想参与猜数字游戏么？y or n:')

	if isplay == 'y':
		number = random.randint(0,50)
		guess = int(input('guess a number:'))
		start = time.time()

		while True:
			if number > guess:
				guess = int(input('guess a bigger number:'))
			elif number < guess:
				guess = int(input('guess a smaller number:'))
			else:
				end = time.time()
				print ('恭喜 猜对了！')

				var = (end - start) / 18.2
				if var < 15:
					print ('优秀')

				elif var < 25:
					print ('良好')
				else:
					print ('较差')
				break
	else:
		print ('谢谢参与')





