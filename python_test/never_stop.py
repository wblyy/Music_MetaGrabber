 # encoding: UTF-8
import re
import urllib2
import urllib
import random

while 1:
	#answer_url = "http://cn.bing.com/search?q="+urllib.quote(str(random.uniform(10, 20))+"我的歌声里+    -zhidao.baidu.com")
    answer_url="http://cn.bing.com/search?q=%E6%88%91%E4%B9%9F%E4%B8%8D%E7%9F%A5%E9%81%93%E8%BF%99%E9%A6%96%E6%AD%8C%E5%8F%AB%E4%BB%80%E4%B9%88%E5%90%8D%E5%AD%97+++-zhidao.baidu.com"
    #answer_url="http://cn.bing.com/search?q=%E8%BF%99%E9%A6%96%E6%AD%8C%E5%8F%AB%E4%BB%80%E4%B9%88%E5%90%8D%E5%AD%97+-zhidao.baidu.com"                                                                                     
	#print answer_url
    msg=urllib2.urlopen(answer_url).read()
    print msg