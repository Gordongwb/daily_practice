# -*- coding: UTF-8 -*-

from PIL import Image,ImageDraw,ImageFont

resource = input('请输入图片位置:')
#只能用绝对路径···
# 处理windows文件位置中'\'的问题
for i in resource :
    if i == '\\' :
        i = '/'
num = input('请输入数字:')
im = Image.open(resource)
draw = ImageDraw.Draw(im)

(width, height) = im.size
size = int(width/6)
myfont  = ImageFont.truetype('arial.ttf', size = size )
#画圆
draw.ellipse(( width*5/6, 0 ,width,width/6),fill="red",outline="red")      
#写字
draw.text( (int(width*21/24),0 ),num,font=myfont,fill='white')

im.save('0000+.jpg')
