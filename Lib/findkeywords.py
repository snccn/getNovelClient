#!/usr/bin/python 
# -*- coding :UTF-8 -*-
# author snccn
# change the class of findkeywords and the URL finding and indexfinding is suppored
from HTMLParser import HTMLParser
import getEpubApi

class findkeywords(HTMLParser):
    def __init__(self, URL):
        HTMLParser.__init__(self)
        self.tittle = ""
        self.output = []
        self.gettittle = 0
        self.getinfo = 0
        self.getindexlist = 0
        self.tittle = ""
        self.info = ""
        self.urls = []
        self.createobj(URL)
        # self.feed(target)
        pass

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            for (variable, value) in attrs:
                if value == "title":
                    self.gettittle = 1
                elif value == "info":
                    self.getinfo = 1
        if tag == "a":
            for (variable, value) in attrs:
                if variable == "href":
                    self.getindexlist = 1
                    self.urls.append(value)
        if tag == "td":
            for (variable, value) in attrs:
                if variable == "colspan":
                    self.getindexlist = 1
                    self.urls.append('NULL')

    def handle_data(self, data):
        if self.gettittle == 1:
            self.tittle = data
            self.gettittle = 0
        if self.getinfo == 1:
            self.info = data
            self.getinfo = 0
        if self.getindexlist == 1:
            self.output.append(data)
            self.getindexlist = 0

    def createobj(self, url):
        getraw = getEpubApi.getEpub(url)
        getraw.disconnect()
        target = getraw.docraw
        self.feed(target)


if __name__ == '__main__':
    a = findkeywords("http://www.wenku8.com/novel/0/513/index.htm")
    print a.tittle.decode('gbk')
    print a.info.decode('gbk')
    # print a.output
    for j in a.output[7:]:
        print j.decode('gbk')
    #print a.urls
    for n in a.urls[7:]:
        print n