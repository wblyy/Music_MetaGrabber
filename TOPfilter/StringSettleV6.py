#-*-coding:utf-8-*-  
#V6从QQ的更多json中拿歌,该版本先拿一个json在线读取
##
import urllib2# 使用库: urllib2


from mydb import MydbV1

db = MydbV1.instance()

#file_object = open('')


request = urllib2.Request(url="http://y.qq.com/y/static/toplist/json/global/1/1_1.js?&hostUin=0&format=jsonp&inCharset=GB2312&outCharset=utf-8&notice=0&platform=yqq&jsonpCallback=MusicJsonCallback&needNewCode=0")
# 使用urllib2创建一个访问请求, 指定url为"http://www.baidu.com/", 并且把访问请求保存在request这个变量里面
all_the_text = urllib2.urlopen(request).read()
# 使用urllib2打开request这个请求(通过urlopen()函数), 并且读取数据(使用read()函数), 把结果保存在result这个变量里面
print all_the_text


#try:
#  all_the_text = file_object.read( )#读全体内容
#finally:
#  file_object.close( )

 
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
		if db.get_id(Songname[i],Artistname[i]):
			print "Duplicated!!!"
		else:
			print "inserting...."
			db.insert_song(Songname[i],Artistname[i],Album[i])
		#db.insert_song(Songname[i],Artistname[i],Album[i])#入库跟print不同，不需要转码
		
	#print 'Artistname='	
	
	#for artist in Artistname:
	#	print artist.decode('utf-8').encode('gb18030')
		
	#print 'Album='
	
	
	#for al in Album:
	#	print al.decode('utf-8').encode('gb18030')
	
	
	


#mPos = all_the_text.find(sStr)   
#mPos1 =all_the_text.find(sStr,mPos+1)
