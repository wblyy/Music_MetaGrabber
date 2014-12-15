#-*-coding:utf-8-*-  
#V9根据甲方的需求针对QQ音乐韩国NMET榜进行数据澄清，凡是在QQ音乐韩国NMET榜中某一期出现过的歌曲无论是否已存在数据库，都丰富其榜单信息
import urllib2# 使用库: urllib2


from mydbV1 import MydbV1

dbV1 = MydbV1.instance()

QQ_boundary=[
		[1,179],
		[2,344],
		[4,94],
		[5,355],
		[6,86],
		[7,95],
		[9,306],
		[12,263],
		[13,170],
		[14,55],
		[17,18],
		[18,19]
		]#根据甲方需求出的二维数组
TOP_name=["QQ音乐KTV榜","QQ音乐ChannelV榜","QQ音乐日本公信榜","QQ音乐韩国NMET榜","QQ音乐英国UK榜","QQ音乐美国公告牌-hot100榜","QQ音乐幽浮劲碟榜","QQ音乐ituns榜","QQ音乐香港商业电台榜","QQ音乐中国TOP排行榜","QQ音乐雪碧音碰音榜","QQ音乐MTV光荣榜"]


for top in range(3,4):#从第1类TOP到第12类TOP  
#第一类榜单爬到了112号，手贱把VPN断了，不开VPN确实快很多
#第七类榜单爬到306号,需要一个抛异常机制，同时把漏网之鱼写入日志
		for volume in range(1,QQ_boundary[top][1]):#从第一期到最近一期
			print 'Top='
			print top
			print 'Volum='
			print volume
			request = urllib2.Request(url="http://y.qq.com/y/static/toplist/json/global/"+str(QQ_boundary[top][0])+"/"+str(volume)+"_1.js?&hostUin=0&format=jsonp&inCharset=GB2312&outCharset=utf-8&notice=0&platform=yqq&jsonpCallback=MusicJsonCallback&needNewCode=0")
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
				
				#str="国标舞"
				#print str.decode('utf-8').encode('gb18030')##纠结的编码print问题
				#print 'Songname='
				
				#for song in Songname:
					#print song.decode('utf-8').encode('gb18030')
				for i in range(0,len(Songname)):
					if dbV1.get_id(Songname[i],Artistname[i]):
						print "Duplicated!!!"#发现重复的不入库
					else:
						print "inserting...."#这才入库
						dbV1.insert_song(Songname[i],Artistname[i],Album[i],TOP_name[top])
					#db.insert_song(Songname[i],Artistname[i],Album[i])#入库跟print不同，不需要转码
		

