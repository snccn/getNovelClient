#!/usr/bin/env python 
# Coding: utf-8
# author : snccn
# get the pictrue and download the pic to ./Assets/<novelid>/pic/<picnovelid>
# Usage:
# Tofile(index_raw[with pic url]) the path of the picture must stored
from HTMLParser import  HTMLParser
import getEpubApi,os
import urllib2,urlparse
path=""
class getPic(HTMLParser):
    def __init__(self,rawdata):
        HTMLParser.__init__(self)
        self.getpic=0
        self.picurl=[]
        self.run(rawdata)
    def handle_starttag(self, tag, attrs):
        if tag=="div":
            for variable,value in attrs:
                if value=="divimage":
                    self.getpic=1
        if tag=="ul":
            for variable,value in attrs:
                if value=="contentdp":
                    self.getpic=0
                    
        if self.getpic==1 and tag=="a":
            for variable ,value in attrs:
                if variable=="href":
                    self.picurl.append(value)
    def run(self,rawdata):
        self.feed(rawdata)
class getpicfile():
    def __init__(self,url):
        self.url=url
        # host=urlparse.urlsplit(url).netloc
        self.sender_herader={
        'Host':"pic.wkcdn.com",
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection':'keep-alive'  
        }
        self.connobj=self.makeconnection()
        self.data=self.getfile()
    def makeconnection(self):
        try:
            req=urllib2.Request(self.url,headers=self.sender_herader)
            return urllib2.urlopen(req)         
        except:
            print "error"
            return 0
    def getfile(self):
        if type(self.connobj)!=int:
            raw_data=self.connobj.read()
            self.connobj.close()
            return raw_data
        else:
            return 0
        

def Tofile(index_target,pathw):
    global path
    path=locatePicPath(pathw)
    urlpool=getPic(index_target).picurl
    for i in urlpool:
        try:
            file=open(path+i.split('/')[-1],"wb")
            file.write(getpicfile(i).data)
        except:
            os.mkdir(path)
        finally:
            file=open(path+i.split('/')[-1],"wb")
            file.write(getpicfile(i).data)
def locatePicPath(pathw):
    return pathw
if __name__=="__main__":
    a=open('../test.txt','r').read()
    # print getPic(a).picurl
    Tofile(a)