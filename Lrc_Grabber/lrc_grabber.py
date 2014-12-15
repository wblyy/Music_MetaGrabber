 # encoding: UTF-8
import re
import urllib2
import urllib
import time
from mydbV2 import MydbV2

dbV2 = MydbV2()

#http://www.lrcgc.com/songlist-21856-1.html最后一页
#陈小春6 陈冠希末尾

for  url_index in xrange(1,21856):
	is_next_page=True#开始翻页
	page=1#初始页为1
	while is_next_page:
		lrc_url='http://www.lrcgc.com/songlist-'+str(url_index)+'-'+str(page)+'.html'
		print lrc_url.decode('utf-8')
		try:
			msg=urllib2.urlopen(lrc_url).read()
	#print msg.decode('utf-8')
			lrc=re.findall('<a class="ico-lrc" href="(.*?).lrc"'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
        #print zpk[2].decode('utf-8')

			for meta in lrc:
	    			lrc_download="http://www.lrcgc.com/"+urllib.quote(meta+".lrc")
	    			print meta.decode('utf-8')
	    			name=re.split( r"/", meta)[1].decode('utf-8')
	    			urllib.urlretrieve(lrc_download, u"1024/"+name+".lrc")
	    #urllib.urlretrieve(lrc_download, meta.decode('utf-8')+".lrc")
			if len(lrc)!=20:
				is_next_page=False#如果当页不满20，则停止翻页
			else:
				page=page+1
			
		except Exception, e:
			page=page+1
			is_next_page=True
			print e
			time.sleep(5)
		
		

		
