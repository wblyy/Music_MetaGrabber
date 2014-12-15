# -*- coding: utf-8 -*- 
import PIL
import os
from PIL import Image
#G:\320K-meta\Downloader3\Kugoo
#F:\Kugoo
#G:\320K-meta\Downloader3\BaiduMusic\QQ_Songs\song
path = '/home/pogo/Music_MetaGrabber/Meta_sort/cover/' 
for file in os.listdir(path): 
	basewidth = 500
        if file.find('.jpg')>0:
                print file
                try:
                        img = Image.open(path+file)
                        if img.size[0]<500 or img.size[1]<500:
                                wpercent = (basewidth/float(img.size[0]))
                                hsize = int((float(img.size[1])*float(wpercent)))
                                img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
                                img.save(path+r'500'+'/'+file)
                except Exception,e:a=1
