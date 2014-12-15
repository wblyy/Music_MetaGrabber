#-*-coding:utf-8-*-  
#V7根据甲方需求抓百度音乐本期榜
import urllib2# 使用库: urllib2
import re

from mydbV1 import MydbV1

dbV1 = MydbV1.instance()

Top_dict={'huayu':'百度华语金曲榜',
		  'oumei':'百度欧美金曲榜',
		  'yingshijinqu':'百度影视金曲榜',
		  'lovesong':'百度情歌对唱榜',
		  'netsong':'百度网络歌曲榜',
		  'oldsong':'百度经典老歌榜',
		  'rock':'百度摇滚榜',
		  'dayhot':'百度热歌榜TOP500',
		  'new':'百度新歌榜TOP100',
		 }

for key in Top_dict:#从第1类TOP到第12类TOP  
		print 'Top='
		print Top_dict[key].decode('utf-8')
		request = urllib2.Request(url="http://music.baidu.com/top/"+key)
		# 使用urllib2创建一个访问请求, 指定url为"http://www.baidu.com/", 并且把访问请求保存在request这个变量里面
		all_the_text = urllib2.urlopen(request).read()
		# 使用urllib2打开request这个请求(通过urlopen()函数), 并且读取数据(使用read()函数), 把结果保存在result这个变量里面
		mark = 's:'   #这里的mark变了
		segment='|'#分隔符
		startPos=0
		endPos=0
		Songname=[]
		Artistname=[]
		Album=[]
		mPos=[0]	#记录特殊符号位置的list，令其第一个值为0
		index=0
		
		Songname=re.findall('href="/song/(.*?)">'.decode('utf-8').encode('utf-8'), all_the_text, re.DOTALL)
		Artistname=re.findall('author_list" title="(.*?)">'.decode('utf-8').encode('utf-8'), all_the_text, re.DOTALL)
	    		
		for index in range(0,len(Artistname)):
			if(len(re.split(r'title="', Songname[index]))==2):
				name=re.split(r'title="', Songname[index])[1]
				if dbV1.get_id(name,Artistname[index]):
					print "Duplicated!!!"#发现重复的
				else:
					print "inserting...."#这才入库
					dbV1.insert_baidu_song(name,Artistname[index],Top_dict[key])

		# 	print name.decode('utf-8')

		#for meta in Artistname:
		#	print meta

		#for meta in range(0,len(Songname)):
		#	key_value=Songname[i]+Artistname[i]
		#	if db.get_id(Songname[i],Artistname[i]):
		#		print "Duplicated!!!"#发现重复的
		#	else:
		#		print "inserting...."#这才入库
		#		dbV1.insert_song(Songname[i],Artistname[i],Album[i],Top_dict[key])


