#!-*- coding:utf8 -*-
import os 
from mydb import Meta
from mutagen.mp3 import MP3
import mutagen.id3
from mutagen.easyid3 import EasyID3
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
meta = Meta()
index_match=0
path = 'F:\\QQmusic\\320K' 
for file in os.listdir(path): 
		if file.find('-')>0:
			file_seg=file.split('-')
			song=file_seg[0].decode('gbk').encode('utf-8')
			artist=file_seg[1].split('.')[0].decode('gbk').encode('utf-8')
			try:   
					index_match+=1
					id3info  = MP3(os.path.join(path,file), ID3=EasyID3)
					for k, v in id3info.items():
    						if k=='album':
    							album = '\n'.join(v)
    							#meta.insert_new(song,artist,album)
    							print album
    							#meta.update_album_like(album,song,artist)
    							#print album,index_match
					#newname=match[0]+' - '+match[1]+'.lrc' 
					#os.rename(os.path.join(path,file),os.path.join(path+'\\match\\',newname)) 
					#print match[0],match[1],index_match
					#meta.update_lrc_like(song,artist)					
    			except Exception, e:
        			print e
#2400+中完全一致的1393个
#用了like之后为1572个
#图片match的1008个
#lrc-match的1474
#1320个有专辑信息