# -*- coding: utf-8 -*-
lyricist="  Tom "
print 'update ignore meta set lyricist ='+lyricist+',compser ='+compser+',arrangement ='+arrangement+',album_release ='+fxtime+'where song='+song+' and artist='+artist;

'update ignore meta set lyricist ='+''+',compser ='+compser+',arrangement ='+arrangement+',album_release ='+fxtime+'where song='+song+' and artist='+artist;

'update meta_test set lyricist = '+lyricist+',composer='+composer+',arrangement='+arrangement+' where song='+song+' and artist='+artist+';'


update meta_test set lyricist = 'aaa',composer='bbb',arrangement='ccc' where song='爱的勇气(电视剧《离婚律师》主题曲)' and artist='曲婉婷';