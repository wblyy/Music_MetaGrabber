# -*- coding: utf-8 -*- 
import PIL
from PIL import Image
basewidth = 500
img = Image.open('ju.jpg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
img.save('ju2.jpg')
