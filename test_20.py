#!/usr/bin/env python
# -*- coding:utf-8 -*-

#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？


#方法1：纯属从规律的角度去解的
sum = 0
x = 0
#在计算实际应用题时，次数默认从1 开始 比较容易理解
for i in range(1,11):  #这里的i 按照回弹来看，例如当i =1时，表示求第一次回弹，sum的计算也先按照回弹数来算
	x = 50/pow(2,i-1)
	sum = sum +3*x   #这个统计出来的结果是算了 第10次的回弹的，最终结果需要去掉

print('第10次落地时 共经过：%s米'%(sum - x))
print('第10次反弹：%s米'%x)

#方法2：从规律+序列的角度
# hei = 100         # 总高度
# tim = 10          # 次数
# height = []       # 每次反弹高度
# for i in range(2,tim+1):  # 计算第二次落地到第十次落地
#     hei /= 2
#     height.append(hei)
# print('第10次落地时，反弹%s高'%(min(height)/2))        # 第十次反弹为第十次落地距离的一半
# print('第10次落地时，经过%s米'% (sum(height)*2+100))