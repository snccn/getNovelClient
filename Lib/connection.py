#!/usr/bin/env python
# -*- coding:UTF-8-*-
# author: snccn

# this script is just for store the data into the database
# we also can build the db file to store the

import sqlite3
from findkeywords import *
CREATE_TABLE='''
create table if NOT EXISTS novels  (
innerid int PRIMARY KEY ,
novelid VARCHAR(255),
novelname VARCHAR(255),
novelauthor varchar(255),
charaname varchar(255),
charaurl VARCHAR(255)
);
'''
status=0
class storetodb(object):
    def __init__(self,novelid,novelauthor,novelname,charaname,charaurl):
        self.connobj=sqlite3.connect("./novel.db")
        self.commoncursor=self.connobj.cursor()
        self.checktables()
        self.isDBbusy=0
        self.indexhandle(novelid,novelauthor,novelname,charaname,charaurl)
    def checktables(self):
        self.commoncursor.execute(CREATE_TABLE)
        self.connobj.commit()
        pass
    def indexhandle(self,novelid,novelauthor,novelname,charaname,charaurl):
        global status
        status+=1
        if self.isDBbusy==0:
            self.isDBbusy=1
            a=self.createsql(novelid,novelauthor,novelname,charaname,charaurl).replace("'","\"")
            self.commoncursor.execute(a)
            self.connobj.commit()
    def createsql(self,novelid,novelauthor,novelname,charaname,charaurl):
        return "insert into  novels (novelid,novelname,novelauthor,charaname,charaurl)VALUES ("+str(novelid)+",'"+novelname+"','"+novelauthor+"','"+charaname+"','"+str(charaurl)+"');"
        pass
def run(id2):
    global status
    id=str(id2)
    if len(id)==4:
        url="http://www.wenku8.com/novel/"+str(id[0])+"/"+str(id)+"/index.htm"
    else:
        url="http://www.wenku8.com/novel/"+str(0)+"/"+str(id)+"/index.htm"
    print url
    try:
        b=findkeywords(url)
        for i in xrange(7,len(b.output)):
            a=storetodb(id,b.info.decode('gbk').replace("'"," "),b.tittle.decode('gbk').replace("'"," "),b.output[i].decode('gbk').replace("'"," "),b.urls[i].decode('gbk').replace("'"," "))
            #print status
    except:
        print "pass"
if __name__=="__main__":
    # for i in xrange(2000,2001):
    #     run(i)
    run(1281)
