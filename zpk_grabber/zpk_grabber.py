 # encoding: UTF-8
import re
import urllib2
import urllib
import time
from mydbV2 import MydbV2

dbV2 = MydbV2()
for  url_index in xrange(2505,4830):#抓到2505
	try:
		time.sleep(2)
		zpk_url='http://www.cavca.org/zpk.php?page='+str(url_index)
		print zpk_url
		msg=urllib2.urlopen(zpk_url).read()
	#print msg
		zpk=re.findall('<td height="40" bgcolor="#F4F4F4">(.*?)</td>'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
        #print zpk[2].decode('utf-8')
		#for meta in zpk:

	    #		print meta.decode('gbk')

		for index in range(0,len(zpk)/5):
				dbV2.insert_data(zpk[index*5].decode('gbk').encode('utf-8'),zpk[index*5+1].decode('gbk').encode('utf-8'),zpk[index*5+2].decode('gbk').encode('utf-8'),zpk[index*5+3].decode('gbk').encode('utf-8'),zpk[index*5+4].decode('gbk').encode('utf-8'))
				print zpk[index*5].decode('gbk')
	except Exception, e:
		print e
		time.sleep(5)
		
	
