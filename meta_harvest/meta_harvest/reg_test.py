 # encoding: UTF-8
import random
import re
import urllib2
import urllib
import requests

proxy_dict=['http://221.10.102.203:82/',
			#r'http://113.11.198.164:2223/',
			#r'http://113.11.198.165:2223/',
			#r'http://113.11.198.166:222
			]

meta_url = "http://www.xiami.com/search/album?key="+urllib.quote("心花路放 电影原声带")
print meta_url
msg=requests.get(meta_url,proxies={"http": random.choice(proxy_dict)}).text
print msg
album_url=re.findall('"CDcover100" href="(.*?)" tit" onclick="'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
print album_url
#第一页筛子 #<p class="cover"><a class="CDcover100" href=" #" title="">

#第二页筛子 #title="搜索 唱片公司 #" target="_blank">
