#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、定长：
1）\d  匹配一个数字， \w 匹配任意一个字母或者数字
2）. 表示匹配任意一个字符--- 'py.' 可以匹配'pyc'、'py!'
3）\s 表示匹配一个空格
4) \_ 表示匹配下划线
5）\- 表示匹配 '-' 符号


2、匹配可变长字符：
1）* 表示匹配任意个字符，包括0个
2）+ 表示匹配至少一个字符
3）？表示匹配0个或者1个字符
4）{n} 表示匹配n个字符
5）{n,m} 表示匹配n-m个字符

3、限定取值方位 []
1）[0-9a-zA-Z\_] 表示匹配一个数字、字母或者下划线 例如 'a'
2）[0-9a-zA-Z\_]+ 表示至少匹配一个由数字、字母或者下划线组成的字符串，例如'Py300'
3）[a-zA-Z\_][0-9a-zA-Z\_]* 表示匹配由字母或者下划线开头 后接任意一个由数字、字母或者下划线组成的字符串
4）[a-zA-Z\_][0-9a-zA-Z\_]{0,19}  表示前面一个字符，后面最多跟19个字符 (这里的0-19仅仅对[0-9a-zA-Z\_]生效)

4、其他：
1）A|B 表示匹配A或者匹配B ，'(P|p)ython'
2) ^ 表示行的开头    '^\d' 表示以数字开头
3）$ 表示行的结束    '\d$' 表示以数字结束  ，例如'^py$'  只能匹配'py'
4）'ABC\\-001'  表示匹配'ABC\-001'  中间是一个转义符号, 但是若在正则前面加个r 则表示不用考虑转义， r'ABC\-001'


re.match(r'正则'，str)  -- 如果匹配的话，则返回一个Match对象，否则返回为None

'''


import re  #这里引入模块时，如果当前用户子定义的文件中有同名的文件  系统会有优先引入这个，因此会报错，提示引入的模块不适合

#re.match()
# print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))  #如果当前匹配失败，则返回None
# # print(re.match(r'^\d{3}\-\d{3,8}$','000-123'))  #匹配成功，则输出<_sre.SRE_Match object; span=(0, 7), match='000-123'>
# print(re.match(r'[a-zA-Z][0-9\_]{3,5}','a12_'))  #这里的{3-5} 仅仅限制靠它最近的[]
# #print(re.match(r'[0-9a-zA-Z\_]','aa')) #这里如果匹配了部分时，仍会返回一个Match（）对象，并提示 <_sre.SRE_Match object; span=(0, 1), match='a'>

# test = '用户输入的字符串'
# if re.match(r'用户输入的字符串', test):
#     print('ok')
# else:
#     print('failed')


#re.split()
# print(re.split(r'[\s\,]+', 'a,b, c  d'))  #分割字符串，r'[\s\,]+' 表示匹配至少一个由空格或者逗号组成的字符串

#re.group()   ----用正则表达式中 使用（）表示要提取的分组
# m = re.match(r'^(\d{3})\-(\d{3,8})$', '010-12345')
# print(m.groups())   #('010', '12345')  元祖的形式
# print(m.group(0))   #010-12345  分组后的索引位置为0 的元素是 字符串本身
# print(m.group(1)) #010
# print(m.group(2)) #12345


#贪婪匹配 '?'
'''
1、正则默认是贪婪匹配的，也就是匹配尽可能多的字符
2、将贪婪变成非贪婪模式 只需要价格"？" 即可，例如：'^(\d+)(0*)$'  --> r'^(\d+?)(0*)$'
'''
# m=re.match(r'^(\d+)(0*)$', '102300')  #贪婪匹配，\d+ 表示至少匹配一个数字，而后面的0* 匹配任意个0，包含（0个）
# print(m.groups())  #('102300', '')
#
# #加上？可以让贪婪匹配变成非贪婪模式，^（\d+?）表示行开头为数字串（该数字串至少有一个数字组成）0个或者1个 ，因此后面的0*$  就可以生效了
# m=re.match(r'^(\d+?)(0*)$', '102300')
# print(m.groups()) #('1023', '00')


#正则编译 re.compile()
'''
1、在python中使用正则时，re模块会干两件事情 ：编译正则表达式-> 拿编译后的表达式去匹配字符
2、如果一个表达式需要重复利用很多次，可以提前预编译表达式，则后面可以直接用来匹配字符串即可  系统就无需再次编译，提升效率。

'''
# import re
# re_telephone = re.compile(r'^(\d{3})\-(\d{3,8})$')   #compile() 编译正则
# print(type(re_telephone))  #<class '_sre.SRE_Pattern'>
# print(re_telephone.match('010-123456').groups())
# #print(re_telephone.match('010-80').groups())  #因为当前没有匹配到结果，所以返回了None，因此提示 AttributeError: 'NoneType' object has no attribute 'groups'
# print(re_telephone.match('010-8086').groups())



#练习题：请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
#someone@gmail.com      bill.gates@microsoft.com

import re

# s = r'[\w]+[\.]?[\w]*\@[\w]+\.com'
# print(re.match(s,'someone@gmail.com'))
# print(re.match(s,'bill.gates@microsoft.com'))


def is_valid_email(addr):
    s = r'[\w]+[\.]?[\w]*\@[\w]+\.com'
    if re.match(s,addr) == None:
        return False
    else:
        return True

print(is_valid_email('someone@gmail.com'))
print(is_valid_email('mr-bob@example.com'))


def name_of_email(addr):
    s = r'([\w]+[\.]?[\w]*)\@([\w]+\.com)'
    print(re.match(s,addr).groups())
    #print(re.match(s, addr).group(1))

name_of_email('someone@gmail.com')











