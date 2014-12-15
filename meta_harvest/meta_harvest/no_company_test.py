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
csvfile = file('meta_no_company_redirect.csv', 'rb')
reader = csv.reader(csvfile)
index=0
index_error=0
index_full=0
for lrow in list(reader):
    index=index+1
    print '处理前:',lrow[0].decode('gbk'),lrow[1].decode('gbk'),'index:',index
    try:
        song=lrow[0].decode('gbk').encode('UTF-8')
        song=re.sub('\(.*?\)|\[.*?]|{.*?}|（.*?）','',song)#去括号

        artist=lrow[1].decode('gbk').encode('UTF-8')
        artist=re.sub('\(.*?\)|\[.*?]|{.*?}|（.*?）','',artist)#去括号

        album=lrow[2].decode('gbk').encode('UTF-8')
        print album
        album_id=mydb.get_song_album_id_qqmusic(song,artist)
        for aid in album_id:
            print aid
        album_company=mydb.get_album_company_by_id_qqmusic(str(aid))
        if album_company:
            for company in album_company:
                meta.update_album_company_by_song(song,artist,company)
                print company
        
        print 'done'
        





        #company_info=mydb.get_album_company(album)
        #if company_info:
        #    company=company_info[0]
        #    print '处理后：',album,company            
            
        #    index_full=index_full+1

    except Exception, e:
        index_error=index_error+1
        print e,index_error
        

