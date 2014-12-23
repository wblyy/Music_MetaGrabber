#coding=utf-8
import random
import csv
import MySQLdb
import sys
from mydb import Tiedb
from mydb import Meta
import re


mydb = Tiedb()
meta = Meta()
    # for row in mydb.get_random_rows(100, "%gmail.com"):
        # print row
    # sys.exit(0)
    #print mydb.get_song_info("青花瓷","周杰伦")[0],mydb.get_song_info("青花瓷","周杰伦")[1],mydb.get_song_info("青花瓷","周杰伦")[2]
csvfile = file('meta_no_album_new.csv', 'rb')
reader = csv.reader(csvfile)
index=0
index_error=0
index_full=0
for lrow in list(reader):
    index=index+1
    #print '处理前:',lrow[0].decode('gbk'),index
    song=lrow[0].decode('gbk').encode('UTF-8')
    artist=lrow[1].decode('gbk').encode('UTF-8')
    print lrow[0],lrow[1]
    try:        
        #print '处理后：',song
        album_name=mydb.get_album_name_163music(song,artist)
        if album_name:
            index_full=index_full+1
            print lrow[0],lrow[1],album_name,index_full
        #artist=song_info[0]
        #print '处理后：',song,artist            
        #meta.update_artist_info(song,artist)
        

    except Exception, e:
        index_error=index_error+1
        print e,index_error
        

