#!/usr/bin/env python
# -*- coding:utf-8 -*-
from html.parser import HTMLParser
from html.entities import name2codepoint
'''1、参考文档http://www.cnblogs.com/zhanghaohong/p/4562127.html'''

# class MyHTMLParser(HTMLParser):
# 	def handle_starttag(self, tag, attrs):
# 		#print('<%s>' % tag)
# 		print('tag:%s ,attrs:%s'%(tag,attrs))
#
# 	def handle_endtag(self, tag):
# 		print('</%s>' % tag)
#
# 	def handle_startendtag(self, tag, attrs):
# 		#print('<%s/>' % tag)
# 		print('tag:%s ,attrs:%s' % (tag, attrs)) #tag:header ,attrs:[('class', 'article-header')]
#
# 	def handle_data(self, data):
# 		print('data:%s'%data)
#
# 	def handle_comment(self, data):
# 		print('<!--', data, '-->')
#
# 	def handle_entityref(self, name):
# 		print('&%s;' % name)
#
# 	def handle_charref(self, name):
# 		print('&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('''<html>
#  <header class="article-header">
#     <h3>from the Python Events Calendar</h3>
# </header>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')


#定义一个MyParser继承自HTMLParser 并将html中包含的手机信息提取出来
'''
该html解析过程如下：
1、收下通过handle_starttag（）函数可以知道 待解析的html 有多少组头tag及属性attrs
2、定义一个继承HTMLParser的类，该类定义了handle_starttag（）方法，用来接收Parse_starttag返回的tag和attrs 并挨个进程处理
3、通过观察 发现在tag 为h3 且class属性为article-header时 可以取到手机信息，因此将该信息取出保存起来
4、my=MyParser()
my.feed(html)

5、html.parser是一个非常简单和实用的库，它的核心是HTMLParser类。从源码来看，它内部封装了一系列regular expression。工作的
流程是：当你feed给它一个类似HTML格式的字符串时，它会调用goahead方法向前迭代各个标签，并调用对应的parse_xxxx方法提取start_tag, 
tag, attrs data comment和end_tag等等标签信息和数据，然后调用对应的方法对这些抽取出来的内容进行处理（当被feed一个html进来以后，程序就开始
 遍历tag 和attrs、data等，，这个时候 遍历出来一组 就开始调用自定义的handle_starttag（）及 handle_data（）开始处理一组）

6、例如该例中 的执行过程：当传过来的第一组数据 一般包含starttag、data等，例如<html>,然后调用自定义类中的方法去处理该标签，保存处理结果以后
在继续执行下一个传过来的标签，例如<header class="article-header">，依次类推 知道html结尾
tag:html ,attrs:[]
bb
bbb
tag:header ,attrs:[('class', 'article-header')]
bb
bbb
tag:h3 ,attrs:[('class', 'article-header'), ('data-title', '【现货增强/标准】MIUI/小米\xa0红米手机2红米2移动联通电信4G双卡')]
aa
aaa

'''
# class MyParser(HTMLParser):
# 	re=[]#放置结果
# 	flg=0#标志，用以标记是否找到我们需要的标签
# 	def handle_starttag(self, tag, attrs):  #这个attrs是每遍历到html文本中的一个标签时生产的tag及a对应属性，例如遍历到<header class="article-header">
# 		print('tag:%s ,attrs:%s' % (tag, attrs))
# 		if tag=='h3':#目标标签
# 			for attr in attrs:  #tag:header ,attrs:[('class', 'article-header')] ，此时attr 就表示attrs中的第一个元素，attr[0],表示第一个元素元组中的第一个元素
# 				if attr[0]=='class' and attr[1]=='article-header':#目标标签具有的属性
# 					self.flg=1#符合条件则将标志设置为1
# 					print('aa')
# 					break
# 		else:
# 			#pass
# 			print ('bb')
#
# 	def handle_data(self, data):
# 		#print('data:%s' % data)
# 		if self.flg==1:
# 			self.re.append(data.strip())#如果标志为我们需要的标志，则将数据添加到列表中
# 			self.flg=0#重置标志，进行下次迭代
# 			print ('aaa')
# 		else:
# 			#pass
# 			print ('bbb')
#
# 	def handle_endtag(self, tag):
# 		pass
# 		#print('</%s>' % tag)
#
# html = '''<html>
#  <header class="article-header">
#     <h3 class="article-header" data-title="【现货增强/标准】MIUI/小米 红米手机2红米2移动联通电信4G双卡">现货增强/标准】MIUI/小米 红米手机2红米2移动联通电信4G双卡</h3>
# </header>
# <body>
#     <h3 class="article-header" data-title="【现货增强/标准】MIUI/小米 红米手机2红米2移动联通电信4G双卡">【金冠现货/全色/顶配版】Xiaomi/小米 小米note移动联通4G手机</h3>
# </body></html>
# '''
# my=MyParser()
# my.feed(html)
# print(my.re)




#练习：找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出
# Python官网发布的会议时间、名称和地点。
'''
总结：
1、先观察待解析的html 欲取出的数据 例如会议发布时间，名称等 都在哪些标签中 这些标签有什么特征
2、通过handle_starttag(self,tag,attrs) 方法 先把所有的标签和属性 打印出来
3、然后由于HTMLParser特有机制会依次将所有tag 挨个传入，然后依次调用类方法去处理一遍 并将处理后的数据保存
4、类变量或者类属性，如果要在类方法中引用的话 必须通过self才行，因为类变量只有类名本身或者实例本身才可以应用，而self 就相当于一个
序列实例
5、该题最重要的思路就是 通过flag 来判断当前传入的tag是否为我们需要的，如果时则标记一下，然后去取这个标签对应的数据，并保存起来，然后
将该flag 重置为0 ，继续去遍历下一个传入的tag
6、待解析的html 可以查看源码后复制粘贴 并赋给一个变量，也可以通过urlopen函数 去打开并读取，例如
with request.urlopen('https://www.python.org/events/python-events/') as f:
	data1 = f.read().decode('utf-8')  #read的内容 一般如果是网页则读取的是html文件，如果是xml 则读出xml文件，提供是接口则直接返回接口的数据
	所有该例中 由于打开的是网页 所有带解析的html可以通过urlopen函数打开并读取内容即可
'''
from html.parser import HTMLParser
from urllib import request

class MyHtmlParser(HTMLParser):
	event = []
	time = []
	location = []
	title = []
	flagtitle = 0
	flagevent = 0
	flagtime = 0
	flaglocation =0

	def handle_starttag(self,tag,attrs):
		#print('tag:%s  attrs:%s'%(tag,attrs))
		if tag == 'h2' or tag =='h3':  #注意这里的标签一定要加引号 不然会当成变量 然后就会找不到
			for attr in attrs:
				if attr[0]=='class' and attr[1]=='widget-title' or attr[1]=='widget-title just-missed':
					self.flagtitle =1  #注意这里flagtitle等 都是类变量，在方法中引用时 只能通过实例变量即self调用
				else:break

		if tag == 'h3':
			for attr in attrs:
				if attr[0]=='class' and attr[1]=='event-title':
					self.flagevent =1
				else:break

		if tag == 'time':
			for attr in attrs:
				if attr[0]=='datetime':
					self.flagtime =1
				else:break

		if tag == 'span':
			for attr in attrs:
				if attr[0]=='class'and attr[1]=='event-location':
					self.flaglocation =1
				else:break


	def handle_data(self,data):
		#print ('data:%s' %data)
		if self.flagtitle ==1:
			self.title.append(data)  #由于event=[]等都是 类变量 在类方法中 只有实例变量self有资格引用，不能直接调用event的话，系统会认为这是一个方法中的局部变量，跟类变量或者属性不相干
			self.flagtitle =0

		if self.flagevent ==1:
			self.event.append(data)
			self.flagevent =0

		if self.flagtime ==1:
			self.time.append(data)
			self.flagtime =0

		if self.flaglocation ==1:
			self.location.append(data)
			self.flaglocation=0

	def handle_endtag(self,tag):
		pass
		#print ('endtag:%s' %tag)

html = '''   <div class="shrubbery">
                <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>
                
                <p class="give-me-more"><a href="?page=2" title="More Events">More</a></p>
                
                <ul class="list-recent-events menu">
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/543/">PyCascades 2018</a></h3>
                        <p>
                            
                            
<time datetime="2018-01-22T00:00:00+00:00">22 Jan. &ndash; 24 Jan. <span class="say-no-more"> 2018</span></time>

                            

                            
                            <span class="event-location">Granville Island Stage, 1585 Johnston St, Vancouver, BC V6H 3R9, Canada</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/611/">PyCon Cameroon 2018</a></h3>
                        <p>
                            
                            
<time datetime="2018-01-24T00:00:00+00:00">24 Jan. &ndash; 29 Jan. <span class="say-no-more"> 2018</span></time>

                            

                            
                            <span class="event-location">Limbe, Cameroon</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/594/">FOSDEM 2018</a></h3>
                        <p>
                            
                            
<time datetime="2018-02-03T00:00:00+00:00">03 Feb. &ndash; 05 Feb. <span class="say-no-more"> 2018</span></time>

                            

                            
                            <span class="event-location">ULB Campus du Solbosch, Av. F. D. Roosevelt 50, 1050 Bruxelles, Belgium</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/557/">PyCon Pune 2018</a></h3>
                        <p>
                            
                            
<time datetime="2018-02-08T00:00:00+00:00">08 Feb. &ndash; 12 Feb. <span class="say-no-more"> 2018</span></time>

                            

                            
                            <span class="event-location">Pune, India</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/576/">PyCon Colombia 2018</a></h3>
                        <p>
                            
                            
<time datetime="2018-02-09T00:00:00+00:00">09 Feb. &ndash; 12 Feb. <span class="say-no-more"> 2018</span></time>

                            

                            
                            <span class="event-location">Medellin, Colombia</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/626/">PyTennessee 2018</a></h3>
                        <p>
                            
                            
<time datetime="2018-02-10T00:00:00+00:00">10 Feb. &ndash; 12 Feb. <span class="say-no-more"> 2018</span></time>

                            

                            
                            <span class="event-location">Nashville, TN, USA</span>
                            
                        </p>
                    </li>
                
                </ul>
            </div>
            <h3 class="widget-title just-missed">You just missed...</h3>
            <ul class="list-recent-events menu">
                
                <li>
                    <h3 class="event-title"><a href="/events/python-events/563/">PyCon Pakistan</a></h3>
                    <p>
                        
                        
<time datetime="2017-12-16T00:00:00+00:00">16 Dec. &ndash; 17 Dec. <span class="say-no-more"> 2017</span></time>

                        
                        
                        
                        <span class="event-location">Lahore, Pakistan</span>
                        
                    </p>
                </li>
                
                <li>
                    <h3 class="event-title"><a href="/events/python-events/612/">PyCon Indonesia 2017</a></h3>
                    <p>
                        
                        
<time datetime="2017-12-09T00:00:00+00:00">09 Dec. &ndash; 10 Dec. <span class="say-no-more"> 2017</span></time>

                        
                        
                        
                        <span class="event-location">Surabaya, Indonesia</span>
                        
                    </p>
                </li>
                
            </ul>

'''
with request.urlopen('https://www.python.org/events/python-events/') as f:
	data1 = f.read().decode('utf-8')
	#print(data1)

myhtmlparser = MyHtmlParser()
myhtmlparser.feed(data1)
# print(myhtmlparser.title)
# print(myhtmlparser.event)
# print(myhtmlparser.time)
# print(myhtmlparser.location)
print()
print('PART-1:%s'%myhtmlparser.title[0])
for i in range(6):
	print('Time:%s  Name:%s'%(myhtmlparser.time[i],myhtmlparser.event[i]))
	print('Location:%s'%(myhtmlparser.location[i]))

print()
print('PART-2:%s'%myhtmlparser.title[1])

for i in range(2):
	print('Time:%s  Name:%s'%(myhtmlparser.time[-(i+1)],myhtmlparser.event[-(i+1)]))
	print('Location:%s'%(myhtmlparser.location[-(i+1)]))