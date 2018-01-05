#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。
由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变为4的
倍数，就可以正常解码了。

ASCII就是编码英文的26个字母和一些常见的符号，之后扩展了一半。总之是一个字节来做编码，大于128的部分是一些特殊符号。但ASCII是无法编码别的
东西的，比如说是不存在“中文的ascii码需要2个字符”这种说法的。ASCII就只有一个字节。Unicode是足够编码地球上所有的语言了，所以ASCII中所能
表示的，Unicode当然全部包括了。Unicode本身是只有2个字节的，之所以出现UTF-8,UTF-16等等之类，那是为了针对不同的应用环境，提高整体编码效
率，比如如果某篇文章里绝大部分是英语（单字节就能表示），就比较适合使用utf-8，而如果绝大部分是中文（需要双字节），可能就utf-16比较合适了


1、ASCII 码是最早期的编码方式 用一个字节来表示字符，因此能代表的字符范围有限，因此后面出现了unicode 编码，用两个字节来表示编码，而utf-8
utf-16 是由于unicode 编码演变而来，即根据不同情况，例如英文等 用一个字节就够了，遇到汉字用2个字节等。
2、一个字节（Byte）等于8个bit（比特位，二进制位），一个比特只能表示一个0 或者1

3、对python3的感受就是python3对文本以及二进制数据做了比较清晰的区分。文本总是Unicode,由str类型进行表示，二进制数据使用bytes进行表示，
不会将str与bytes偷偷的混在一起
str->bytes:encode编码
bytes->str:decode解码
字符串通过编码成为字节码，字节码通过解码成为字符串。

字节码：https://www.cnblogs.com/hello2764/p/5459758.html
Python 程序的执行过程就是，它先把代码编译成 bytecode （字节码）指令，交给虚拟机，逐条执行 bytecode 指令。

def double(a):
    return a*2

double.__code__.co_code
b'|\x00d\x01\x14\x00S\x00'

'''

import base64

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)


#请写一个能处理去掉=的base64解码函数：

# def safe_base64_decode(s):
#     if type(s) is bytes:
#         n = len(s)%4
#         s = s + b'='*n
#     if type(s) is str:
#         s = s.encode('utf-8')  # 'YWJjZA=='.encode('utf-8')  --->b'YWJjZA=='
#
#         n = len(s) % 4
#         s = s + b'='*n
#     return base64.b64decode(s)  #TypeError: a bytes-like object is required, not 'str'
#
# assert b'abcd' == safe_base64_decode(b'YWJjZA==')
# assert b'abcd' == safe_base64_decode('YWJjZA==')
# assert b'abcd' == safe_base64_decode(b'YWJjZA')
# assert b'abcd' == safe_base64_decode('YWJjZA')
# print('ok')

