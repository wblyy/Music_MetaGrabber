# encoding: UTF-8
import re
string1=u'戊In厦门'
#p = re.compile(r'(www|http[s])?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
p = re.compile(ur'[\u4e00-\u9fa5]')
str=p.findall(string1)#.decode('utf-8'))
 
print str

for word in str:
	print word

