#coding=utf-8
import PIL
import random
import csv
import MySQLdb
import sys
from mydb import Tiedb
from mydb import Meta
import re
import os
from PIL import Image



mydb = Tiedb()
meta = Meta()
path = '/home/pogo/meta_harvest/album/'

    # for row in mydb.get_random_rows(100, "%gmail.com"):
        # print row
    # sys.exit(0)
    #print mydb.get_song_info("青花瓷","周杰伦")[0],mydb.get_song_info("青花瓷","周杰伦")[1],mydb.get_song_info("青花瓷","周杰伦")[2]
csvfile = file('meta_no_cover.csv', 'rb')
reader = csv.reader(csvfile)
index=0
index_error=0
index_full=0
for lrow in list(reader):
    index=index+1
    #print '处理前:',lrow[0].decode('gbk'),lrow[1].decode('gbk'),'index:',index
    try:
        song=lrow[0].decode('gbk').encode('UTF-8')
        #song=re.sub('\(.*?\)|\[.*?]|{.*?}|（.*?）','',song)#去括号

        artist=lrow[1].decode('gbk').encode('UTF-8')
        #artist=re.sub('\(.*?\)|\[.*?]|{.*?}|（.*?）','',artist)#去括号

        album=lrow[2].decode('gbk').encode('UTF-8')
        cover_name=song+' - '+artist+'.jpg'
        print cover_name
        print album

        if '好声音' in album:
            meta.update_album_img_path(cover_name,album)
            img = Image.open(path+'好声音.jpg')
            img.save(path+cover_name)
        elif 'M-net' in album:
            #meta.update_album_company(album,cover_name)
            meta.update_album_img_path(cover_name,album)    
            img = Image.open(path+'M-net.jpg')
            img.save(path+cover_name)
        elif '好歌曲' in album:
            #meta.update_album_company(album,cover_name)
            meta.update_album_img_path(cover_name,album)    
            img = Image.open(path+'好歌曲.jpg')
            img.save(path+cover_name)
        elif '雪碧' in album:
  #          meta.update_album_company(album,cover_name)
            meta.update_album_img_path(cover_name,album)    
            img = Image.open(path+'雪碧.jpg')
            img.save(path+cover_name)
        elif '最美和声' in album:
#            meta.update_album_company(album,cover_name)
            meta.update_album_img_path(cover_name,album)     
            img = Image.open(path+'最美和声.jpg')
            img.save(path+cover_name)
        elif '我是歌手' in album: 
#            meta.update_album_company(album,cover_name)
            meta.update_album_img_path(cover_name,album)     
            img = Image.open(path+'我是歌手.jpg')
            img.save(path+cover_name)
        elif '华语单曲榜' in album:
        #    meta.update_album_company(album,cover_name)
            meta.update_album_img_path(cover_name,album)             
            img = Image.open(path+'华语单曲榜.jpg')
            img.save(path+cover_name)
        elif '新歌速递' in album:
#            meta.update_album_company(album,cover_name)
            meta.update_album_img_path(cover_name,album)     
            img = Image.open(path+'好声音.jpg')
            img.save(path+cover_name)
        elif '最强音' in album:
#            meta.update_album_company(album,cover_name)
            meta.update_album_img_path(cover_name,album)     
            img = Image.open(path+'新歌速递.jpg')
            img.save(path+"\\cover\\"+cover_name)
        elif '直通春晚' in album:
#            meta.update_album_company(album,cover_name)
            meta.update_album_img_path(cover_name,album)     
            img = Image.open(path+'直通春晚.jpg')
            img.save(path+"\\cover\\"+cover_name)


        #print album
        #album_id=mydb.get_song_album_id_qqmusic(song,artist)
        #for aid in album_id:
        #    print aid
        #    album_company=mydb.get_album_company_by_id_qqmusic(str(aid))

        #for company in album_company:
        #    meta.update_album_company_by_song(song,artist,company)
        #    print company
        #print 'done'
        





        #company_info=mydb.get_album_company(album)
        #if company_info:
        #    company=company_info[0]
        #    print '处理后：',album,company            
            
        #    index_full=index_full+1

    except Exception, e:
        index_error=index_error+1
        print e,index_error
        

