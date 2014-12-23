#!-*- coding:utf8 -*-
import os
import socket
import re
import requests
import MySQLdb as mysql
import threading
import Queue
import time
from HTMLParser import HTMLParser as htmlP
from BeautifulSoup import BeautifulSoup as bs4


from db import DB

socket.setdefaulttimeout(10)


class CheckMp3Path(object):
    def __init__(self, thread_num = 30):
        self.data_file = "prder"
        self.session = requests.session()
        self.session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"}
        self.get = self.session.get
        self.thread_num = thread_num
        self.html_parser = htmlP()

    def start(self):
        records = self.load_file()
        index = 0
        que = Queue.Queue()
        threads = []
        for i in records:
            index +=1
            que.put([i, self.req])
        for j in xrange(self.thread_num):
            threads.append(Down(que, "线程" + str(j), DB()) )
        for j in threads:
            j.setDaemon(True)
            j.start()
        for j in threads:
            j.join()
        print "END ALL"

    def req(self, album):
        url = "http://www.xiami.com/search/album?key=%s" % album
        print "搜索:", url
        con = self.get(url).content
        try:
            href = re.findall('CDcover100.+?href="(.+?)"', con, re.S)[0]
        except IndexError, e:
            print e,url
            return "",""

        print "专辑", href
        con = self.get(href).content
        try:
            language = re.findall("语种.+?td>.+?<td.+?>(.+?)</td", con, re.S)[0].strip()
            language = bs4(language).text
            language = self.html_parser.unescape(language).encode("utf8")
            #rtime = '-'.join(re.findall("<span>发行时间：(\d+)年(\d+)月(\d+)日</span", con, re.S)[0])
            #rtime = re.findall("发行时间.+?top\">(.+?)</td", con, re.S)[0].replace("年", '-').replace("月", '-').replace("日", '')
            genre = re.findall("专辑风格.+?<a.+?>(.+?)</a", con, re.S)[0].strip()
            genre = bs4(genre).text
            genre = self.html_parser.unescape(genre).encode("utf8")
        except Exception ,e:
            print e
            return "", ""
        return language, genre

    def load_file(self):
        with file(self.data_file)as f:
            r = f.read()
        records = [i.split('\t') for i in r.splitlines()]
        return records


class Down(threading.Thread):
    """docstring for Down"""
    def __init__(self, que, name, db):
        super(Down, self).__init__()
        self.que = que
        self.name = name
        self.db = db
		
    def run(self):
        while True:
            if not self.que.empty():
                record, self.req= self.que.get(block=False,timeout=1)
                key = record[1].strip()
                #key = self.query_song_artist_by_id(record[0]).strip()
                if not key:
                    continue
                language, genre = self.req(key)
                with file(".tmp", "w")as f:
                    f.write(" ".join(record))
                if language and genre:
                    self.save_db(record[0], language, genre)
                    print self.name, record, "save ok.."
                time.sleep(3)
            else:
                break
        return
    def query_song_artist_by_id(self, id):
        sql = "select id, song, artist  from metadata.meta_noart_process where id = %s;" % id
        with file("song_artist.sql", 'a')as f:
            f.write(sql + "\n")
        print sql
        result = self.db.query(sql)[0][0]
        return result.get("artist").strip() + " "  + result.get("song").strip()
    
    def save_db(self, meta_id, language, genre):
        try:
            meta_id = int(meta_id)
        except Exception:
            return
        sql = 'update metadata.meta_noart_process as meta set meta.genre = "%s" , meta.language="%s" where meta.id = %s;' % (mysql.escape_string(genre), mysql.escape_string(language), meta_id)
        print sql
        with file("update.sql", 'a')as f:
            f.write(sql + "\n")
        column_num = self.db.query(sql)[1]
        return column_num
	
    

if __name__ == '__main__':
    check_mp3_path = CheckMp3Path()
    check_mp3_path.start()
