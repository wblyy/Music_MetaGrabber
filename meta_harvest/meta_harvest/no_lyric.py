#coding=utf-8
import random
import csv
import MySQLdb
import sys
from mydb import Tiedb
from mydb import Meta
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
mydb = Tiedb()
meta = Meta()
    # for row in mydb.get_random_rows(100, "%gmail.com"):
        # print row
    # sys.exit(0)
    #print mydb.get_song_info("青花瓷","周杰伦")[0],mydb.get_song_info("青花瓷","周杰伦")[1],mydb.get_song_info("青花瓷","周杰伦")[2]
csvfile = file('hanwen.csv', 'rb')
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
        song=song[0:len(song)/3]

        artist=lrow[1].decode('gbk').encode('UTF-8')
        artist=re.sub('\(.*?\)|\[.*?]|{.*?}|（.*?）','',artist)#去括号

        #album=lrow[2].decode('gbk').encode('UTF-8')
        #print album
        lyric_id=mydb.get_lyric_id_china(song)
        for lid in lyric_id:
            print lid
            lyrics=mydb.get_lyric_by_id(str(lid))

        for lyric in lyrics:
            file_object = open(r'lyric/'+lrow[0]+' - '+lrow[1]+'.lrc', 'w')
            #for word in lyric:
            #print lyric
            file_object.write(lyric)
            file_object.close()
            lyric_path=song+' - '+artist+'.lrc'
            index_full=index_full+1
            meta.update_lyric_path_by_song(lrow[0].decode('gbk').encode('UTF-8'),lrow[1].decode('gbk').encode('UTF-8'),lyric_path)
            print lyric,index_full
        print 'done'
        





        #company_info=mydb.get_album_company(album)
        #if company_info:
        #    company=company_info[0]
        #    print '处理后：',album,company            
            
        #    index_full=index_full+1

    except Exception, e:
        index_error=index_error+1
        print e,index_error
        

