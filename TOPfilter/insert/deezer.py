# -*- coding: utf-8 -*-

import sys
import re
import json
import requests
import functools
import traceback
import xlrd

from mydb import Mydb

db = Mydb.instance()

def yield_xl(xlpath):
    book = xlrd.open_workbook(xlpath)
    sheet = book.sheet_by_index(0)
    for i in range(sheet.nrows)[1:]:
        # print sheet.row_values(i)
        song, name, _ = sheet.row_values(i)
        try:
            yield song.encode('utf8'), name.encode('utf8')
        except:
            continue
    # print first_sheet.row_slice(rowx=0, start_colx=0, end_colx=2)
    

def yield_row(split=None, filelist=None):
    split = split if split else ' '
    for fn in filelist:
        with open(fn, 'r') as f:
            for line in f:
                try:
                    yield line.strip().split(',')[:2]
                except Exception, e:
                    print traceback.print_exc()
                    print e, line

def print_json(jsonobj):
    print json.dumps(jsonobj, indent=4)

class Deezer(object):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0'
    }
    timeout = 20
    def __init__(self):
        # self.api_token = api_token
        self.session = requests.session()
        self.session.headers.update(self.headers)
        self._set_auth_cookie('sg7bd5c222a29f052a725ec60c2d3cc588eeef8f')
        # print self.session.headers

    def search_song(self, song):
        # response = self.session.get('http://www.deezer.com/suggest', params={'q': song, 'c': 'CN', 'limit': '50'})
        # return response.json()
        html = self.session.get('http://www.deezer.com/search/%s' % song, timeout=self.timeout).content
        try:
            return json.loads(re.findall(r"naboo\.display.*?, (.*?)\);", html)[0])
        except:
            print "you need login, then copy you cookie.sid to here"
    
    def get_album_info(self, albumid):
        album = {}
        print 'http://www.deezer.com/album/%s' % albumid
        html = self.session.get('http://www.deezer.com/album/%s' % albumid, timeout=self.timeout).content
        try:
            album_json = json.loads(re.findall(r"naboo\.display.*?, (.*?)\);", html)[0])
        except:
            print "you need login, then copy you cookie.sid to here"
        # print_json(album_json)
        album['company'] = album_json["DATA"]["LABEL_NAME"]
        album['album_release'] = album_json["DATA"]["DIGITAL_RELEASE_DATE"]
        album['album_pic'] = album_json["DATA"]["ALB_PICTURE"]
        album['album_name'] = album_json["DATA"]["ALB_TITLE"]
        album['artist_pic'] = album_json["DATA"]["ARTISTS"][0]["ART_PICTURE"]
        return album

    def find_album_id(self, song, artist):
        search_songs = self.search_song(song)
        # print_json(search_songs)
        for item in search_songs['TRACK']['data']:
            if is_similar(artist, item["ARTISTS"][0]["ART_NAME"].encode('utf8')):
                return item['ALB_ID'].encode('utf8')

    def _set_auth_cookie(self, sid=None):
        self.session.headers.update({'Cookie': 'sid='+sid})

mydeezer = Deezer()

def rerun(method):
    """Decorate with this method to restrict to site admins."""
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        for i in range(1,4):
            try:
                return method(*args, **kwargs)
            except Exception, e:
                print e, 'run again!'
                continue
    return wrapper

@rerun
def test():
    print 'run test case!'
    raise Exception('test')

def is_similar(name1, name2):
    n1 = ''.join([i for i in re.sub(r'(\(.*?\))', '', name1).lower() if i in 'abcdefghijklmnopqrstuvwxyz'])
    n2 = ''.join([i for i in re.sub(r'(\(.*?\))', '', name2).lower() if i in 'abcdefghijklmnopqrstuvwxyz'])
    if n1 and n2:
        if n1 in n2 or n2 in n1:
            return True
    return False

@rerun
def get_meta_info(song, artist):
    album_id = mydeezer.find_album_id(song, artist)
    # print album_id
    if album_id:
        print 'find album! '
        return mydeezer.get_album_info(album_id)
    return {}

def main():             # 2850871
    for d in yield_xl('./bdtop.xlsx'):
    # for d in yield_row(split=',', filelist=filelist):
        # d = [i.decode('latin-1') for i in d]
        # print d
        print d[0], d[1]
        if db.get_id(d[0], d[1]):
            continue
        metadic = get_meta_info(d[0], d[1])
        if metadic:
            print d[0], d[1], metadic['artist_pic'], metadic['album_name'], metadic['album_pic'], metadic['album_release'], metadic['company']
            db.insert_data(d[0], d[1], metadic['artist_pic'], metadic['album_name'], metadic['album_pic'], metadic['album_release'], metadic['company'])
        else:
            db.insert_song(d[0], d[1])

if __name__ == '__main__':
    # print is_similar('laioxiaorong', '')
    # for row in get_meta_info('apologize', 'republic').items():
        # print row[0], row[1]
    # print get_deezer_track_id('if i were a boy', 'beyon')
    # main(sys.argv[1:])
    # yield_xl('./bdtop.xlsx')
    main()
