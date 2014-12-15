# -*- coding: utf-8 -*- 
import os 
path = 'D:\\song\\' 
for file in os.listdir(path): 
		if file.find('-')>0:
			file_seg=file.split(' - ')
		#print file_seg[0]
		#print file_seg[1].split('.')[0]
			newname=file_seg[1].split('.')[0]+' - '+file_seg[0]+'.mp3' 
			os.rename(os.path.join(path,file),os.path.join(path,newname)) 
			print newname
		