# -*- coding: utf-8 -*-
'''
Created on 2013年12月9日
 
@author: hhdys
'''
 
import os
import mysql.connector
import MySQLdb
 
config = {
  'user': 'root',
  'password': '654321',
  'host': 'localhost',
  'database': 'SGK',
  'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)
 
class ReadFile:
    def readLines(self):
        f = open("qqlist.txt", "r",1)
        i=0
        list=[]
        for line in f:
            strs = line.split("@qq.com")
            #print strs
            for str in strs:
                #print str
                qqnumber=str.split('<')[-1]
                name=str.split('<')[0]
                #print qqnumber
                #for qqnumber in qqnumbers:
                
            #if len(strs) != 5:
            #    continue
            #if len(strs)>=2:
                #list.append(qqnumber)
                cursor=cnx.cursor()
                print 'qqnumber:',qqnumber
                sql = "select * from QQ_yiyi where qqnumber=%s"#+qqnumber
                #results=[]
                try:
                    cursor.execute(sql,(qqnumber,))
                except Exception, e:
                    print e
                #list=[]
                for result in cursor:
                    print result,name
                #result=cursor.fetchall()
                cnx.commit()
                cursor.close()
        cnx.close()
        f.close()
        print("ok")
    def listFiles(self):
        d = os.listdir("E:/data/")
        return d
        
             
if __name__ == "__main__":
    readFile = ReadFile()
    readFile.readLines()
