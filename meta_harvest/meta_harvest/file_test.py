#coding=utf-8
lyric='いくらい　マケナイクライニ'
song='梦的列车'
artist='Alex'
file_object = open(r'lyric/'+song+' - '+artist+'.lrc', 'w')
file_object.write(lyric)
file_object.close()