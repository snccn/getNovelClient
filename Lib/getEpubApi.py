#!/usr/bin/env python
# -*-coding:utf8 -*-
# author snccn
# for python 2.7.x not support on python 3.x

import urllib2 as urlli
# normally the urlpaser can deal with the header [HOST] in the url gived  create socket for just once
import urlparse
class getEpub(object):
    def __init__(self,url):
        self.url=url             
        self.send_headers=feeler(self.url)
        self.connobj=self.getUrlHealth()
        self.status=self.retConnectionStatus()
        self.docraw=self.getdocraw()
    def geturl(self):
        return self.url
        pass
    def getUrlHealth(self):
        try:
            req=urlli.Request(self.url,headers=self.send_headers)
            return urlli.urlopen(req)
        except:
            return "NOT HEALTH"
        pass
    def anlzURL(self):
        pass
    def retConnectionStatus(self):
        return self.connobj.headers
        pass
    def getdocraw(self):
        #print type(self.connobj)
        if type(self.connobj)==str:
            pass
        else:
            return self.connobj.read()
        pass
    def rawoutput(self): 
        print self.docraw
    def download(self):
        pass
    def disconnect(self):
        self.connobj.close()
        pass
    def getrequest(self):
        pass
def feeler(URL):
    # feelc=urlli.Request(URL)
    # try:
    #     feelerobj=urlli.urlopen(feelc)
    # except :
    #     return "socket error "
    # host=feelc.host
    # feelerobj.close()
    host=urlparse.urlsplit(URL).netloc
    #print host
    send_headers = {
        'Host':host,
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection':'keep-alive'     
    }
    # print (send_headers)
    return send_headers
    pass
if __name__=="__main__":
    print ("hello world")
    a=getEpub("http://www.wenku8.com/novel/1/1009/index.htm")
    a.disconnect()
    a.rawoutput()
    print a.docraw
    print a.retConnectionStatus()