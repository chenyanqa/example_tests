#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
# >>> conn = sqlite3.connect('test.db')  #连接数据库
# >>> cursor = conn.cursor()  #创建游标
# # 执行查询语句:
# >>> cursor.execute('select * from user where id=?', ('1',))  #执行sql语句 但是不返回具体结果，仅仅是执行动作
# <sqlite3.Cursor object at 0x10f8aa340>
# # 获得查询结果集:
# >>> values = cursor.fetchall()  #获取执行结果集
# >>> values
# [('1', 'Michael')]
# >>> cursor.close()
# >>> conn.close()
使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。

使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。

使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。

如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：

cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
SQLite支持常见的标准SQL语句以及几种常见的数据类型。具体文档请参阅SQLite官方网站。

小结
在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。

要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。

如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？请回忆try:...except:...finally:...的用法。

'''

#练习 ：请编写函数，在Sqlite中根据分数段查找指定的名字：

def count():
    fs = []
    for i in range(1,4):
        def f():
            print(i)
            return i*i
        fs.append(f)
    return fs

f1,f2,f3= count()
# print(count())
# print(f1)
# print(f1())
# print(f2)
# print(f2())


a,b,c = [1,2,3]
print(a)