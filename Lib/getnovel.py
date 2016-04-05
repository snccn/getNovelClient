#!/usr/bin/python
# coding:UTF-8
# author snccn
# get the real novel from novel site www.wenku8.com
#
from HTMLParser import HTMLParser
import getEpubApi


class chapter(HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.connobj = self.createobj()
        self.rawHTML = self.send_rawHTML()
        self.chaptername = ""
        self.chapter = []
        self.flagofgetname = 0
        self.flagofgetchapter = 0
        self.starthandle()

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            for (variable, value) in attrs:
                if value == "title":
                    self.flagofgetname = 1
                elif value == "footlink":
                    self.flagofgetchapter = 0
        pass
        if tag == "ul":
            for (variable,value)in attrs:
                if value=="contentdp":
                    self.flagofgetchapter=1
    def handle_data(self, data):
        if self.flagofgetname==1:
            self.chaptername = data
            self.flagofgetname = 0
        if self.flagofgetchapter==1:
            self.chapter.append(data)
            #self.flagofgetchapter = 1

    def send_rawHTML(self):
        # for debug use
        # a = open("targetwenku8.txt", 'r')
        # b = a.read()
        # because of the terrible formart of the novels that i dont't know how to deal with i HTMLparser so i do this
        b=self.connobj
        e=b.replace("<br />","").replace("&nbsp;","")
        #print e
        return e
    def createobj(self):
        try:
            connobj = getEpubApi.getEpub(self.url)
            return connobj.docraw
        except:
            return "cannot open the target site"

    def starthandle(self):
        self.feed(self.rawHTML)


if __name__ == "__main__":
    c = chapter("http://www.wenku8.com/novel/1/1009/29434.htm")
    #print c.connobj
    print c.chaptername.decode('gbk')
    for i in c.chapter:
        print i.decode('gbk')
