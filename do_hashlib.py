#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# import hashlib
# md5 = hashlib.md5() #Returns a md5 hash object; optionally initialized with a string
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())


#设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
import hashlib

# 这类全局数据 不应该放在某个函数里面
# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
#
# def calc_md5(password):
#     md5 = hashlib.md5() #创建一个 空的 md5-哈希对象
#     md5.update(password.encode('utf-8')) #使用参数(必需是bytes类型)password.encode('utf-8') 来更新md5哈希对象
#     return md5.hexdigest() #返回被更新后的md5哈希对象的摘要，hexdigest()方法比digest（）方法 要更安全些，使用十六进制展示摘要
#
#
# def login(user,password):
#     if db[user] == calc_md5(password):
#         return True
#     else:
#         return False
#
#     # 当时的想法试讲db 字典的数据 放在login函数中，因此可以逐个访问，通过枚举的手法，但是其实 因为调用login函数被调用时 会传进来
#     #对应的 user 和password  因此只需要对比调用时传进来的password计算出来的摘要 是否跟数据库存储的一致即可
#
#     # if db['michael'] == calc_md5(password):
#     #     return 'michael ok'
#     # if db['bob'] == calc_md5(password):
#     #     return 'bob ok'
#     # if db['alice'] == calc_md5(password):
#     #     return 'alice ok'
#
# assert login('michael', '123456')   #assert +表达式，只要表示返回true 即表示断言成功，否则失败
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')




#根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
import hashlib,random

def get_md5(s):  #根据传过来的byte 返回生成的十六进制摘要
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):  #如果没啥可继承的 默认继承object类
    def __init__(self,username,password): #创建构造函数，并定义实例属性username 等
        self.username = username
        self.salt = ''.join([chr(random.randint(48,122)) for i in range(20)])  #生成一个长度为20的随机字符串。例如h58Gn:;x[8`K`@WfPC?m
        self.password = get_md5(password+self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username,password):
    user =db[username]  #将db字典中的 key为 username的值取出来赋给user，其实是一个User（）实例
    return user.password == get_md5(password+user.salt) #返回表达式的真假

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')



#1、random.randint(48,122) 表示在数字48-122之前随机取值  chr() 表示序号i所表示的的ASCII/unicode值
#2、[chr(random.randint(48,122)) for i in range(20)] 列表生成式，其中表达式 chr(random.randint(48,122))表示每次需要生成且
#元素，其中for i in range(20) 表示用来控制循环次数或者表达式中相关元素的取值
#3、[x * x for x in range(1, 11) if x % 2 == 0]   x * x 表示每次循环所需要生成的元素，for x in range(1, 11) if x % 2 == 0
#用于筛选元素x

g = [chr(random.randint(48,122)) for i in range(20)]
print(g) #['h', '5', '8', 'G', 'n', ':', ';', 'x', '[', '8', '`', 'K', '`', '@', 'W', 'f', 'P', 'C', '?', 'm']
print(''.join(g)) #h58Gn:;x[8`K`@WfPC?m
print(chr(65))  # 输出 A




'''
help(list.append)
Help on method_descriptor:
append(...)
    L.append(object) -> None -- append object to end
'''
l = []
print(l.append('1'))  #返回None
print(l)




