#-*-coding:utf-8-*-  
#V8根据甲方整合的百度已有的歌单进行去重
#可以将甲方的需求看做一个二维数组
import urllib2# 使用库: urllib2
import csv
import time

from mydbV1 import MydbV1

dbV1 = MydbV1.instance()


csvfile = file('baidu.csv', 'rb')
reader = csv.reader(csvfile)

for lrow in list(reader):
    #print '\t'.join(lrow[1])
	#time.sleep(1)
	#print lrow[0]
	 

			
		
	if dbV1.get_id(lrow[0].decode('gbk'),lrow[1].decode('gbk')):
		print "Duplicated!!!"#发现重复的不入库
	else:
		print "inserting...."#这才入库
		#print lrow
		#print lrow[0].decode('gbk')
		#print lrow[0].decode('gbk'),lrow[1].decode('gbk'),'unknown',lrow[2].decode('gbk')
		dbV1.insert_song(lrow[0].decode('gbk'),lrow[1].decode('gbk'),'unknown',lrow[2].decode('gbk'))
			#db.insert_song(Songname[i],Artistname[i],Album[i])#入库跟print不同，不需要转码

csvfile.close()