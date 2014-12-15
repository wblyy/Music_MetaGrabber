#coding=utf-8
"""
Get songs info like lyricist, composer, arrangement.

How to use it:
    import songs
    songdic = songs.query(song, singer)
ddd
You can also test it on cmd
python songs.py 七里香 周杰伦
"""
import sys
import re
import urllib2
import urllib
import os
import csv
import time
from mydbV2 import MydbV2

dbV2 = MydbV2()

def open_url(url):
	return urllib2.urlopen(url).read()
def query(qsong, qsinger):
    song = escape_char(qsong)
    singer = escape_char(qsinger)
    songurl = "http://mojim.com/"+urllib.quote(song)+".html?g3"
    msg = open_url(songurl)
    re_url = singer+'</a></td>.*?"/(cny[0-9]{1,}x[0-9]{1,}x[0-9]{1,}\.htm)'
    re_fxtime = singer+'</a></td>.*?<td Class="iA">([0-9]{1}.*?[0-9]{1})</td>'
    print songurl
    lyurl = re_find_lyurls(re_url, msg)
    try:
        fxtime = re_find_lyurls(re_fxtime, msg)[-1]
    except:
        fxtime = ''
    if not lyurl: # if can't find match_singer_lyurl,then find first match_song url
        lyurl = re_find_lyurls('/(cny[0-9]{1,}x[0-9]{1,}x[0-9]{1,}\.htm)', msg)
    song = {}
    song['fxtime'] = fxtime
    if lyurl:
        for i in lyurl:
            # print lyurl
            lyric = open_url("http://mojim.com/"+i)
            song['song'] = qsong
            song['singer'] = qsinger
            song['lyricist'] =  re_find_item('content=".*?作词：(.*?)\s', lyric).strip()
            song['composer'] =  re_find_item('content=".*?作曲：(.*?)\s', lyric).strip()
            song['arrangement'] =  re_find_item('content=".*?编曲：(.*?)\s', lyric).strip()
            if song['lyricist']: # if find, return immediatly
               return song
    else:
        song['song'] = qsong
        song['singer'] = qsinger
        song['lyricist'] =  ''
        song['composer'] =  ''
        song['arrangement'] =  ''
    return song

def escape_char(singer):
    splitable = re.findall(ur'([&|;|/|+|(]{1})', singer)
    if splitable:
        singer = singer.split(splitable[0])[0].strip()
    elif singer == "S.H.E":
        singer = 's.h.e'
    return singer

def re_find_item(reg_text, msg):
    items = re.findall(reg_text.decode('UTF-8').encode('UTF-8'),msg, re.DOTALL)
    return items[0] if items else ''
    # return items if items else ''

def re_find_lyurls(reg_text, msg):
    items = re.findall(reg_text.decode('UTF-8').encode('UTF-8'),msg, re.DOTALL)
    return items if items else []
    # return items if items else ''    

if __name__ == "__main__":
    #song = sys.argv[1]
    #singer = sys.argv[2]
	csvfile = file('meta_test.csv', 'rb')
	reader = csv.reader(csvfile)

	for lrow in list(reader):
    
		print lrow[1].decode('gbk').encode('UTF-8')
		songdic = query(lrow[0].decode('gbk').encode('UTF-8'),lrow[1].decode('gbk').encode('UTF-8'))
		dbV2.insert_l(song['lyricist'],song['composer'],song['arrangement'])#,song['fxtime']
		#dbV2.get_id("dsds","sss")	
		for k in songdic:
			print k,songdic[k]


			
	
	

	csvfile.close()
    
    
