#coding=utf-8
import re
s='我的老故事,我的,你的 (？？ ？？？？？)'
s=re.sub('\(.*?\)|\[.*?]|{.*?}|（.*?）','',s)#去括号
print '(no)',s.decode('utf-8')#s表示需要处理的字符串
douhao=re.split(r',',s)
for word in douhao:
	print  word.decode('utf-8')
