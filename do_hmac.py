#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、__init__(self, key, msg=None, digestmod=None)
Note: key and msg must be a bytes or bytearray objects.

2、普通的hashlib 模块的普通/原始哈希算法 为了避免用户设置的密码过于简单而容易被破解，所以会将用户设置的简单密码在'加盐'，然后组合
成一个密码 并存储密码摘要，但是hmac  提供更简单的途径 来给密码等重要message "加盐"，使用方法例如 hmac.new(key,message,digestmod='MD5')

3、hmac.new(key, msg=None, digestmod=None)  -- msg 为原始消息，key相当于随机'加盐'值
    Create a new hashing object and return it.

4、Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，使用hmac算法比标准hash算法更安全，因为针
对相同的message，不同的key会产生不同的hash。

'''

# import hmac
#
# message = b'Hello, world!'
# key = b'secret'
# h = hmac.new(key,message,digestmod='MD5')
# print(h.hexdigest())   #fa4ee7d173f2d97ee79022d1a7355bcf


# 练习：将上一节的salt改为标准的hmac算法，验证用户口令 (先注册，后验证登录)

import hmac,random

def calc_hmac(key,password):
    return hmac.new(key.encode(),password.encode(),digestmod='MD5').hexdigest()

class User(object):
    def __init__(self,username,password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(10)])
        self.password = calc_hmac(self.key,password)

db = {
    'michael': User('michael', '123456'),  #每次调用生成一个User实例的时候，生成一个对应的随机字符串key
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username,password):
    user = db[username]  #现将User（）类的对应的实例 赋值给user （会对应username、key等3个属性）
    if user.password == calc_hmac(user.key,password):
        #user.password 表示数据库中存储的值，calc_hmac(user.key,password) 是根据当前登录用户生成实例时的key 直接调用函数去计算摘要
        return True
    else:
        return False

assert login('michael','123456')
assert login('bob','abc999')
assert login('alice','alice2008')
assert not login('michael','1234567')
assert not login('bob','123456')
assert not login('alice','Alice2008')
print('ok')





