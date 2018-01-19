#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、virtualenv 主要用例创建一个独立的python运行环境，使得各python相互互不干扰

步骤：
1、创建文件夹
Mac:~ michael$ mkdir myproject
Mac:~ michael$ cd myproject/
Mac:myproject michael$

2、创建一个独立的Python运行环境，命名为venv：
Mac:myproject michael$ virtualenv --no-site-packages venv
Using base prefix '/usr/local/.../Python.framework/Versions/3.4'
New python executable in venv/bin/python3.4
Also creating executable in venv/bin/python
Installing setuptools, pip, wheel...done.

3、激活该虚拟环境
Mac:myproject michael$ source venv/bin/activate
(venv)Mac:myproject michael$

4、在该虚拟环境中按照模块或者库
(venv)Mac:myproject michael$ pip install jinja2
...
Successfully installed jinja2-2.7.3 markupsafe-0.23

5、运行python文件
(venv)Mac:myproject michael$ python myapp.py

6、退出当前的venv环境，使用deactivate命令
(venv)Mac:myproject michael$ deactivate
Mac:myproject michael$


...


'''