 # encoding: UTF-8
import re
import urllib2
import urllib
import requests

proxy_dict=['http://113.11.198.163:2223/',
			#r'http://113.11.198.164:2223/',
			#r'http://113.11.198.165:2223/',
			#r'http://113.11.198.166:2223/',
			'http://113.11.198.167:2223/',
			'http://113.11.198.168:2223/',
			'http://113.11.198.169:2223/',
			]

meta_url = "http://www.xiami.com/search/album?key="+urllib.quote("心花路放 电影原声带")
msg=requests.get(meta_url,proxies={"http": random.choice(proxy_dict)}).text
album_url=re.findall('<p class="cover"><a class="CDcover100" href="(.*?)" title="">" onclick="'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
print album_url
#第一页筛子 #<p class="cover"><a class="CDcover100" href=" #" title="">

#第二页筛子 #title="搜索 唱片公司 #" target="_blank">
