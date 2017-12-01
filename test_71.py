#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#编写input()和output()函数输入，输出5个学生的数据记录。，主要包括 学号，姓名， 分数即可
'''
name = ''
age = 0
score = 0

def input():

    name = input('请输入学生姓名:')
    age = input('请输入学生年龄:')
    score = input('请输入学生分数:')

 def output():
     print('学生姓名为：%s'%(name))

1、当时没写出来，因为函数input（）里面的参数只能在函数内部使用，output（）函数没法调用，所以就没法读取用户的输入并输出
2、下方列出两种解题思路：
1）将输入函数的输入数据保存在一个全局列表里面，这样输出函数 就可以直接读取列表了
2）利用类变量相关的关系来读取
'''

#方法1：列表的思路

# #首先通过for 循环创建一个二维数组
# stu = []
# for i in range(5):
#     stu.append(['', '', []])
# #print(stu)  #[['', '', []], ['', '', []], ['', '', []], ['', '', []], ['', '', []]]
#
# def input_stu(stu):
#     for i in range(3):
#         print('请输入第%d个同学的信息：'%(i+1))
#         stu[i][0] = input('学号：')
#         stu[i][1] = input('姓名：')
#
#         for j in range(3):
#             stu[i][2].append(int(input('学分%d：'%(j+1))))
#
# def output_stu(stu):
#     for i in range(3):
#         print('第%d个同学的学号，姓名，学分分别为：%s,%s,%s'%((i+1),stu[i][0],stu[i][1],[x for x in stu[i][2]]))
#
# if __name__ == '__main__':
#     input_stu(stu)
#
#     print('学生信息输出为：')
#     output_stu(stu)



#方法2：类变量的方式

class Student:
    name = ''    #name、age这些都是类变量，被整个类所共有
    age = 0
    score = ['']*2  # 这里[]*N 都是[],如果里面有内容的话 才会翻倍

    def input(self):
        self.name = input('name:')      #self.name表示一个实例变量 一旦与等号连用即被重新赋值，变成了实例变量
        self.age = input('age:')
        for i in range(len(self.score)):
            self.score[i] = int(input('score:'))

    def output(self):
        print('output name :%s'%(self.name))
        print('output age :%s' % (self.age))
        for i in range(len(self.score)):
            print('output %d score:%d'%((i+1),self.score[i]))


if __name__ == '__main__':

    stuArray = [Student(),Student()]
    #stuArray = [Student()]*2    # 这样写的话 会导致 output一直输出结果是一样的，因为self.name,self.age 的取值固定在了第二次输入中。

    for i in range(len(stuArray)):
        stuArray[i].input()

    for i in range(len(stuArray)):
        stuArray[i].output()



















