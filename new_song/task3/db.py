#!-*- coding:utf8 -*-
import MySQLdb as Mysqldb


class DB(object):
    def __init__(self):
        try:
            self.conn=Mysqldb.connect(
                host='127.0.0.1',
                user='root',
                passwd='654321',
                port=3306,
                #db='',
                charset='utf8')
            self.conn.autocommit(1)
        except Exception, e:
            print e

    def query(self, sql):
        cur = self.conn.cursor(Mysqldb.cursors.DictCursor)
        ex = cur.execute(sql)
        result = cur.fetchall()
        return result, ex
        #conn.commit()


#select count(*) from metadata.meta as meta, music_meta.song_info10M as info where mp3_path='' and meta.song = info.title and meta.artist = info.artist;

if __name__ == '__main__':
    db = DB()
    print db.query("show databases;")
