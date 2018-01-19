#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
1、PIL提供了操作图像的强大功能，可以通过简单的代码完成复杂的图像处理。
2、im.thumbnail((w//2,h//2))
3、im.filter(ImageFilter.EMBOSS)
4、return chr(random.randint(65,90))


'''
from PIL import Image,ImageFilter

#1、缩放效果
# im = Image.open('test.jpg')  #打开一个图片
# print(type(im))  #<class 'PIL.JpegImagePlugin.JpegImageFile'>
# print(im.size)  #(404, 404)
#
# w,h = im.size
# print('Original image size:%sx%s'%(w,h))
#
# im.thumbnail((w//2,h//2))   #thumbnail(size, resample=3)  （w//2,h//2）代表size参数
#
# print('Resize image to: %sx%s' % (w//2, h//2)) #" / "就表示 浮点数除法，返回浮点结果;" // "表示整数除法。
#
# im.save('thumbnail.jpg')


# 2、模糊 滤镜效果
im = Image.open('test1.jpg')
im2 = im.filter(ImageFilter.EMBOSS) #使用Image模块的成员函数.filter()来调用滤波函数对图像进行滤波，例如ImageFilter.BLUR是一个模糊的滤波
im2.save('me1.jpg')


# 3、绘图，生成字母验证码
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#随机字母
def rndChar():
    return chr(random.randint(65,90))  #chr(97) 表示返回参数97对应的字符串，即ASKII码

#随机颜色1
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#随机颜色2：
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width = 60*4
height = 60

#创建image对象
image = Image.new('RGB',(width,height),(255,255,255))  #new(mode, size, color=0)

#创建font对象
font = ImageFont.truetype('Arial.ttf',36)  #truetype(font=None, size=10, index=0, encoding='', layout_engine=None)
#创建draw对象
draw = ImageDraw.Draw(image)

#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())

# 输出文字:
for t in range(4):  #text(xy, text, fill=None, font=None, anchor=None, *args, **kwargs)
    draw.text((60 * t+10 , 10), rndChar(), font=font, fill=rndColor2()) #这里的x 表示文字的起始位置，y表示距离最上测得距离

# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
print(image.size)
