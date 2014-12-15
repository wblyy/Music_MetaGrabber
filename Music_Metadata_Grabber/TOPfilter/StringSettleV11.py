#-*-coding:utf-8-*-  
#V7根据甲方需求抓QQ音乐本期榜
import urllib2# 使用库: urllib2


from mydbV1 import MydbV1

dbV1 = MydbV1.instance()

Top_dict={'1':'QQ音乐巅峰榜·港台',
		  '2':'QQ音乐巅峰榜·内地',
		  '6':'QQ音乐巅峰榜·欧美',
		  '7':'QQ音乐巅峰榜·流行指数',
		  '9':'QQ音乐巅峰榜·韩国',
		  '10':'QQ音乐巅峰榜·日本',
		  '11':'QQ音乐巅峰榜·民谣',
		  '10':'QQ音乐巅峰榜·摇滚',
		  }

for key in Top_dict:#从第1类TOP到第12类TOP  
		print 'Top='
		print top
		print 'Volum='
		print volume
		request = urllib2.Request(url="http://music.qq.com/newframe/static/toplist/json/h5/top/"+key+".json")
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
		while(all_the_text.find(mark,mPos[index]+1)!=-1):#读到最后的mark
			mPos.append(all_the_text.find(mark,mPos[index]+1))#继续找下一个，注意+1
			startPos=all_the_text.find(segment,mPos[index])#起始位
			endPos=all_the_text.find(segment,startPos+1)#结束位置
			Songname.append(all_the_text[startPos+1:endPos])
			
			startPos=all_the_text.find(segment,endPos+1)#下一个空挡位
			endPos=all_the_text.find(segment,startPos+1)#下一个空挡位
			Artistname.append(all_the_text[startPos+1:endPos])
				
			startPos=all_the_text.find(segment,endPos+1)#下一个空挡位
			endPos=all_the_text.find(segment,startPos+1)#下一个空挡位
			Album.append(all_the_text[startPos+1:endPos])
				
			index=index+1

		else:	
			print 'mPos='
			print mPos
			print len(mPos)
				

		for i in range(0,len(Songname)):
			key_value=Songname[i]+Artistname[i]
			if db.get_id(Songname[i],Artistname[i]):
				print "Duplicated!!!"#发现重复的
			else:
				print "inserting...."#这才入库
				dbV1.insert_song(Songname[i],Artistname[i],Album[i],Top_dict[key])


