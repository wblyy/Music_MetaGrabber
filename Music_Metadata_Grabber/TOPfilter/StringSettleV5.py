#-*-coding:utf-8-*-  
#V5加个去重功能，查询数据库，如果歌手名、歌曲名都重复则不如库
#
from mydb import MydbV1

db = MydbV1.instance()

file_object = open('12.json.txt')
try:
  all_the_text = file_object.read( )#读全体内容
finally:
  file_object.close( )

mark = '"s"'   #1.json.txt内的特殊符号，该符号后的第一个|后为歌名，第三个|后为歌手名，第五个|后为专辑名
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
