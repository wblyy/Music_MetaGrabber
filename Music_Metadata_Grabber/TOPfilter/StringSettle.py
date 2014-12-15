#-*-coding:utf-8-*-
#读取一个文件并将特定标注的pos摘录出来
#
file_object = open('1.json.txt')
try:
  all_the_text = file_object.read( )#读全体内容
finally:
  file_object.close( )

mark = '"s"'   #1.json.txt内的特殊符号，该符号后的第一个|后为歌名，第三个|后为歌手名，第五个|后为专辑名
segment='|'#分隔符

mPos=[0]	#记录特殊符号位置的list，令其第一个值为0


index=0

while(all_the_text.find(mark,mPos[index]+1)!=-1):#读到最后的mark
	mPos.append(all_the_text.find(mark,mPos[index]+1))#继续找下一个，注意+1
	index=index+1

else:
	print 'mPos='
	print mPos
	print len(mPos)

	
	
	


#mPos = all_the_text.find(sStr)   
#mPos1 =all_the_text.find(sStr,mPos+1)
