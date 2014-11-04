# -*- coding: utf-8 -*-
import MySQLdb

class BaseDB(object):
    def __init__(self, database=None, user=None, passwd=None, host=None):
        self.database = database if database else 'mysql'
        self.user = user if user else 'root'
        self.passwd = passwd if passwd else ''
        self.host = host if host else '127.0.0.1'#不需要输端口号

    @property
    def db(self):
        return MySQLdb.connect(self.host, self.user, self.passwd, self.database, charset='utf8')

    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def _execute(self, *args, **kwargs):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args, **kwargs)
        insert_id = cur.lastrowid
        conn.commit()
        return insert_id
        
    def _query_rows(self, *args):
        cur = self.db.cursor()
        cur.execute(*args)
        return cur.fetchall()

    def test_db(self):
        return self._query_rows('show tables')

class MydbV1(BaseDB):
    def __init__(self):
        BaseDB.__init__(self, database='metadata')

    def insert_data(self, song, artist, artist_img, album_name, album_pic, album_release, company):
        self._execute('insert ignore meta(song, artist, artist_img, album_name, album_img, album_release, company) '
                      'values (%s, %s, %s, %s, %s, %s, %s)', (song, artist, artist_img, album_name, album_pic, album_release, company))

    def insert_song(self, song, artist,album):
        self._execute('insert ignore meta(song, artist, album_name) '
                      'values (%s, %s, %s)', (song, artist, album))
	
					  
    def get_id(self, song, artist):
        return self._query_rows('select id from meta where song=%s and artist=%s', (song, artist))
