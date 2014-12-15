# -*- coding: utf-8 -*-
'''
Created on 2013年12月9日
 
@author: hhdys
'''
 
import os
from mydbV2 import MydbV2
import sys
import re
import csv
dbV2 = MydbV2()


reload(sys)
sys.setdefaultencoding('utf-8')


csvfile = file('hotorder.csv', 'rb')
reader = csv.reader(csvfile)
#f = open("hot.txt","r",1)
fw = open('result.txt','w+')

for line in list(reader):    

    #strs = re.findall('\S\S*',line)
    #strs = line.split(" ")
    #if len(line)!=3:
    #    print '某行有异常:',len(line)
    #    continue
    song_id=line[0]
    song=line[1].decode('gbk','ignore').encode('utf-8')
    artist=line[2].decode('gbk','ignore').encode('utf-8')
    print song_id,'song:',song,'artist:',artist
    try:
        id= dbV2.get_id(song,artist)
    except Exception, e:
        print e
    print id
    if id:
        fw.write('已查询到:     '+song_id+','+song+','+artist+'\n')#song+'/t'+artist+'/t'+str(id))
    if not id:
        fw.write('未查询到:     '+song_id+','+song+','+artist+'\n')#song+'/t'+artist+'/t'+str(id))
    #fw.write('hello')
fw.close()
