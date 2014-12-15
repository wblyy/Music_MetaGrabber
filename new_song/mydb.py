#coding=utf-8
import random
import csv
import MySQLdb
import sys
import re

class Mydb(object):
    def __init__(self, user, passwd, dbname):
        self._id = 0           # use in pop function
        self.user = user
        self.passwd = passwd
        self.dbname = dbname

    @property
    def db(self):
        return MySQLdb.connect("localhost", self.user, self.passwd, self.dbname, charset='utf8')

    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def _execute(self, *args, **kwargs):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args, **kwargs)
        conn.commit()

    def _query_row(self, *args):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args)
        rows = cur.fetchone()
        return rows

    def _query_rows(self, *args):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args)
        rows = cur.fetchall()
        return rows    

class Tiedb(Mydb):
    def __init__(self):
        Mydb.__init__(self, 'root', '', 'music_meta')


    def get_album_info(self, album_id):
        return self._query_row('select company,publishDate from album_info where id=%s', (album_id, ))
    def get_album_company(self, album_name):
        return self._query_row('select company from album_info where album=%s', (album_name, ))
    def get_lyric_id_163music(self,song):
        return self._query_row('select lyricid from song_info_163music where title=%s limit 1', (song,))
        #song_info_china
    def get_lyric_id_china(self,song):
        return self._query_row('select lyricid from song_info_china where title like "'+song+'%" limit 1')

    def get_lyric_id_163music(self,song):
        return self._query_row('select lyricid from song_info_163music where title=%s limit 1', (song,))
    def get_lyric_id_qqmusic(self,song):
        return self._query_row('select lyricid from song_info_qqmusic where title=%s limit 1', (song,))
    def get_lyric_id_xiami(self,song):
        return self._query_row('select lyricid from song_info_xiami where title=%s limit 1', (song, ))
    def get_lyric_by_id(self,id):
        return self._query_row('select lyric from lyrics where id=%s ', (id, ))


    def get_song_info_xiami(self,song, artist):
        return self._query_row('select album_id,album,musicUrl,lyricid,song_id from song_info_xiami where title=%s and artist=%s limit 1', (song, artist))
    def get_proxim_song_info_xiami(self,song, artist):
        return self._query_row('select album_id,album,musicUrl,lyricid,song_id from song_info_xiami where title=%s and artist=%s limit 1', (song, artist))
    
    def get_song_info_qqmusic(self,song, artist):
        return self._query_row('select album_id,album,musicUrl,lyricid,song_id from song_info_qqmusic where title=%s and artist=%s limit 1', (song, artist))
    def get_song_info_163music(self,song, artist):
        return self._query_row('select album_id,album,musicUrl,lyricid,song_id from song_info_163music where title=%s and artist=%s limit 1', (song, artist))
    def get_song_album_id_163music(self,song, artist):
        return self._query_row('select album_id from song_info_163music where title=%s and artist=%s limit 1', (song, artist))
    
    def get_album_company_by_id_163music(self,id):
        return self._query_row('select company from album_info_163music where id=%s', (id, ))
    
    def get_song_album_id_qqmusic(self,song, artist):
        return self._query_row('select album_id from song_info_qqmusic where title=%s and artist=%s limit 1', (song, artist))
    
    def get_album_company_by_id_qqmusic(self,id):
        return self._query_row('select company from album_info_qqmusic where id=%s and company!="" ', (id, ))

    def get_song_info_deezer(self,song, artist):
        return self._query_row('select album_id,album,musicUrl,lyricid,song_id from song_info_deezer where title=%s and artist=%s limit 1', (song, artist))

    def get_lyric(self, song_id):
        return self._query_row('select lyric from lyrics where song_id=%s', (song_id, ))
    def get_artist_xiami(self,song):
        return self._query_row('select artist from song_info_xiami where title=%s limit 1', (song, ))
      
class Meta(Mydb):
    def __init__(self):
        Mydb.__init__(self, 'root', '', 'metadata')
    def get_song_match(self,song, artist):
        return self._query_row('select song,artist from meta_new where song=%s and artist=%s limit 1', (song, artist))
#like concat(info.title,'%%')
    def get_song_like(self,song, artist):
        #print 'select song,artist from meta_new where %s LIKE concat("%%",song,"%%") and %s LIKE concat("%%",artist,"%%") limit 1'
        #return self._query_row('select song,artist from meta_new where %s concat("%%",song,"%%") and %s LIKE concat("%%",artist,"%%") limit 1', (song,artist))
        return self._query_row('select song,artist from meta_new where "'+song+'"LIKE concat("%",song,"%") and "'+artist+'" LIKE concat("%",artist,"%")')
    def update_songmp3_like(self,song, artist):
        return self._execute('update meta_new set mp3_path=concat(song," - ",artist,".mp3") where "'+song+'"LIKE concat("%",song,"%") and "'+artist+'" LIKE concat("%",artist,"%")')
    def update_cover_like(self,song, artist):
        return self._execute('update meta_new set album_img_path=concat(song," - ",artist,".jpg") where "'+song+'"LIKE concat("%",song,"%") and "'+artist+'" LIKE concat("%",artist,"%")')
    def update_lrc_like(self,song, artist):
        return self._execute('update meta_new set lyric_path=concat(song," - ",artist,".lrc") where "'+song+'"LIKE concat("%",song,"%") and "'+artist+'" LIKE concat("%",artist,"%")')
    def update_album_like(self,album,song, artist):
        return self._execute('update meta_new set album_name="'+album+'" where "'+song+'"LIKE concat("%",song,"%") and "'+artist+'" LIKE concat("%",artist,"%")')
    

    def insert_data(self, song, artist):
        self._execute('insert ignore meta_new (song, artist) values (%s, %s)', (song, artist))

    def insert_data(self, song, artist):
        self._execute('insert ignore meta_new (song, artist) values (%s, %s)', (song, artist))
    def update_album_info(self, album_name,song,artist):
        self._execute("update meta set album_name=%s where song=%s and artist=%s", (album_name,song,artist))
    def update_album_company_by_song(self,song,artist,company):
        self._execute("update meta set producer=%s where song=%s and artist=%s", (company,song,artist))
    def update_album_company(self, album_name,company):
        self._execute("update meta set producer=%s where album_name=%s", (company,album_name))
    def update_artist_info(self,song,artist):
        self._execute("update meta set artist=%s where song=%s and artist='' ", (artist,song))
    def update_lyric_path_by_song(self,song,artist,lyric_path):
        self._execute("update meta set lyric_path=%s where song=%s and artist=%s", (lyric_path,song,artist))  
    def update_album_img_path(self, cover_name,album_name):
        self._execute("update meta set album_img_path=%s where album_name=%s", (cover_name,album_name)) 
    def update_songinfo(song,artist,album_id,album,musicUrl,lyricid):
        self._execute("update meta_new set album_id=%s,album_name=%s,musicUrl=%s,lyricid=%s where song=%s and artist=%s", (album_id,album,musicUrl,lyricid,song,artist)) 

    #update_lyric_path_by_song
     

        
if __name__ == "__main__":
    mydb = Tiedb()
    meta = Meta()
    # for row in mydb.get_random_rows(100, "%gmail.com"):
        # print row
    # sys.exit(0)
    #print mydb.get_song_info("青花瓷","周杰伦")[0],mydb.get_song_info("青花瓷","周杰伦")[1],mydb.get_song_info("青花瓷","周杰伦")[2]
    csvfile = file('meta_no_album_again.csv', 'rb')
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
            if ',' in artist:#表演者中若存在逗号，则分割之
                artists=re.split(r',',artist)
                for performer in artists:
                    print '分割后：',song,performer.decode('utf-8')
                    song_info=mydb.get_song_info_163(song,performer.decode('utf-8').encode('UTF-8'))
                

            else:            
                song_info=mydb.get_song_info_163(song,artist)

            if song_info:
                album_id=song_info[0]
                album_name=song_info[1]
                download_url=song_info[2]
                lyricid=song_info[3]
                song_id=song_info[4]
                print album_id,album_name,download_url,lyricid,song_id,'index_full:',index_full
                meta.update_album_info(album_name,song,artist)
            #album_info=mydb.get_album_info(album_id)
            #company=album_info[0]
            #publishDate=album_info[1]
            #if company:
                index_full=index_full+1
            else:
                index_error=index_error+1
            #lyric=mydb.get_lyric(song_id)[0]

            #print album_id,album_name,download_url,lyricid,song_id,company,publishDate,'index_full:',index_full
            #print lyric

        except Exception, e:
            index_error=index_error+1
            print e,index_error
        

