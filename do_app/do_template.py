#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、运行python app.py，Flask自带的Server在端口5000上监听
2、一般这类框架类的文件 最好通过命令行运行，不要直接在pycharm中运行，然后使用app.run(debug=True) 启动服务，
然后使用 ctrl+c 停止服务，关闭flask服务器 可以使用先1）ps -fA |grep 'python' （这里的f表示full，A表示All的意思） 2）kill ***
3、Jinja2是基于python的模板引擎
4、{{ ... }}：装载一个变量，模板渲染的时候，会使用传进来的同名参数这个变量代表的值替换掉。
{% ... %}：装载一个控制语句。
{# ... #}：装载一个注释，模板渲染的时候会忽视这中间的值。

'''
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html') #渲染指定模块，例如渲染加载home.html


@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password =='password':
        return render_template('signin_ok.html',username=username,password=password)

    return render_template('form.html',message='Bad username or password',username=username)

if __name__ =='__main__':
    app.run()
