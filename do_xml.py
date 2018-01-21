#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
1、XML虽然比JSON复杂，在Web中应用也不如以前多了，不过仍有很多地方在用
2、操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，
边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件
3、在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。
<a href="/">python</a>
会产生3个事件：
start_element事件，在读取<a href="/">时；
char_data事件，在读取python时；
end_element事件，在读取</a>时。

4、总结：解析mxl的要素
1）先定义一个处理器类 里面包含start_element、char_data、end_element三个事件(SAX模式)，其中start_element（）方法中包含xml 标签的name和
attrs 两个属性，分别用来标记标签名字 和标签属性，<query yahoo:lang="zh-CN" yahoo:created="2018-01-13T08:06:22Z"
yahoo:count="1" xmlns:yahoo="http://www.yahooapis.com/v1/base.rng">  name为query, attrs: {'xmlns:yahoo': 'http://www.yahooapis.com/v1/base.rng',
 'yahoo:count': '1', 'yahoo:created': '2018-01-13T08:33:59Z', 'yahoo:lang': 'en-US'}

2）在start_element（）中找出关键节点 并把其attrs中的属性保存起来，例如，我们需要取出待解析的url中的城市，所有需要先找到name=yweather:location
节点，然后 将其attrs中的城市保存起来

3）然后定义一个mxl解析函数，例如def parseXml(xml_str) ，现需要生产一个处理器（handler实例），然后定义一个解析器实例
然后将处理器中自定义的3个时间分别赋值给解析器的3个对应属性，然后用该武装后的解析器去处理待解析的mxl即可


'''

# from xml.parsers.expat import ParserCreate
#
# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
          #<query yahoo:lang="zh-cn" yahoo:created="2018-01-13T07:07:01Z" 中属性是指“yahoo:lang="zh-cn"等
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('sax:end_element: %s' % name)
#
#     def char_data(self, text):
#         print('sax:char_data: %s' % text)
#
#
# xml = r'''<?xml version="1.0"?>
#     <ol>
#         <li><a href="/python">Python</a></li>
#         <li><a href="/ruby">Ruby</a></li>
#     </ol>
#     '''
#
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# #ParserCreate(encoding=None, namespace_separator=None, intern=None)
# #Return a new XML parser object.
#
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)  #解析 Parse XML data


#练习题：请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
# https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml

from xml.parsers.expat import ParserCreate
from urllib import request
import time
class DefaultSaxHandler(object): #定义一个保护start_element（）、end_element()、char_data()方法的处理类
    def __init__(self):  #构造函数，定义了两个实例变量location，forecast
        self.location = {}
        self.forecast = []
    def start_element(self, name, attrs):  #定义start_element（）函数，有两个固定属性name、attrs
        print('sax:start_element: %s, attrs: %s' % (name, attrs))
        if name == 'yweather:location':
            self.location = attrs  #将当前yweather:location对应的属性赋给实例变量location
        if name == 'yweather:forecast':
            data = {}
            #date = time.strftime('%Y-%m-%d', time.strptime(attrs['date'],'%d %b %Y'))
            data['date'] = attrs['date']
            data['high'] = attrs['high'] #将attr字典中的元素值 取出来赋给data字典的对应元素
            data['low'] = attrs['low']
            self.forecast.append(data) #将个字典值 追加到一个lise中

    def end_element(self, name):
        pass
        #print('sax:end_element: %s' % name)
    def char_data(self, text):
        pass
        #print('sax:char_data: %s' % text)


def parseXml(xml_str):
    handler = DefaultSaxHandler()  #定义一个处理器，即解析xml的具体操作实例
    parser = ParserCreate() #创建一个xml解析对象
    parser.StartElementHandler = handler.start_element #相当于给标准解析器的对应属性或者操作赋值
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)  #传入带解析的对象
    return {
        'city': handler.location['city'],
        'forecast': handler.forecast
    }

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()
    #print(data.decode('utf-8'))


result = parseXml(data.decode('utf-8'))
print(result['city'])
for i in result['forecast']:
    print(i)
# assert result['city'] == 'Beijing'
# print('ok')


