#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
1\读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源的一个方法是使用try...finally：
2\写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，所以上面的代码可以简化为：
with open('/path/to/file', 'r') as f:
    f.read()
3\并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句
4\实现上下文管理是通过__enter__和__exit__这两个方法实现的。
__enter__()：主要执行一些环境准备工作，同时返回一资源对象。如果上下文管理器open("test.txt")的__enter__()函数返回一个文件对象。

5、要想使用with xxxx() as x: 这种格式， 可以用@contextmanager 装饰一个生成器xxxx() 这个生成器里包含相关的上下文处理
6、所以closeing上下文管理器仅使用于具有close()方法的资源对象。例如，如果我们通过urllib.urlopen打开一个网页，urlopen返回的request有
close方法，所以我们就可以使用closing上下文管理器
6、 @contextmanager
        def some_generator(<arguments>):  #定义一个生产器
            <setup>
            try:
                yield <value>   #yield 之前的部分相当于是__enter__()函数，yield中的value 相当于__enter__()函数的返回值
            finally:
                <cleanup>   #yield后的部分相当于__exit__()函数

    with some_generator(<arguments>) as <variable>:  #这个<variable> = <value> （相当于是一个迭代器实例）

            <body>


'''

class Query(object):
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self   #返回一个对应资源的实例

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

#会先执行__enter__（）方法 打印出"Begin"，然后执行 query()方法，最后执行 __exit__（）方法-如果with语句有报错，则抛出错误，否则正常关闭程序
with Query('Bob') as q:  #由于Query()类实现了上下文管理，因此可以使用with 语句
    q.query()



#改良版，不用手动编写__enter__（）和__exit__（）方法，利用@contextmanager装饰器
from contextlib import contextmanager

class Query(object):

    def __init__(self,name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager #这个装饰器 接受一个generator ，用yield语句把with 。。as var 把变量输出出去，然后with语句就可以正常工作了
def create_query(name):
    print('Begin')
    q = Query(name)  #yield 之前的这两句代码相当于是__enter__()函数的代码
    yield q   #相当于 __enter__()函数的返回值，即返回对应资源的实例
    print('End')  #相当于__exit__()函数


with create_query('Bob') as q:
    q.query()

print('---------------------------')

#@contextmanager
def tag(name):
    print('<%s>'%name)
    yield name*2
    print('<<%s>>'%name)
    print('<<<%s>>>' % name)

# with tag('hi'):  #with语句先调用tag()函数，先输出'<hi>'，然后遇到yield 先阻塞当前函数，因此就开始输出hello，world 然后在返回当前函数输出'hi'
#     print('hello')
#     print('world')


o = tag(1)  #先初始化一个生成器
print(next(o))  #生成器是通过next(generator)来读取函数，若当前遇到yield 后，执行完 yield语句后 跳出函数，然后下次在执行时，从上次yield后面开始执行
# <1>
# 2
#print(next(o))
# <<1>>
# <<<1>>>



#closing()   可以将没有实现上下文的对象 变成上下文对象。
from contextlib import closing
from urllib.request import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context  #如果不加这句的话 会报错：ssl证书认证失败
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        # print(line.decode('utf-8')) #将bytes类型数据解码为str
        print(line) #输出bytes 类型 ：b'    <meta charset="utf-8">\n'


#closing()函数也是一个由@contextmanger装饰的迭代器
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
