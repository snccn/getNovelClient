#!/usr/bin/python
# Coding:utf-8
# author snccn
# this is the feeler to anlz if the novel id is valid
# attention new url to go http://www.wenku8.com/book/1072.htm
# the content is http://img.wkcdn.com/image/1/1074/1074s.jpg
import getEpubApi
import json
import time
import urllib2
from HTMLParser import HTMLParser

# ID_POOL=[]
ID_AVILIABLE = {}


def checkaviliable(id):
    url = "http://www.wenku8.com/book/" + id + ".htm"
    # aviliable = 0
    aviliable = urlcheck(url)
    print id, aviliable
    # time.sleep(.5)
    return aviliable


def run(top):
    for i in xrange(1000, top):
        ID_AVILIABLE[i] = checkaviliable(str(i))
    print ID_AVILIABLE
    a = json.dumps(ID_AVILIABLE)
    jsonfile = open("./aviliable.json", 'w')
    jsonfile.write(a)
    jsonfile.close()


def urlcheck(url):
    try:
        connobj = getEpubApi.getEpub(url)
        a=gettitle(connobj.docraw).title
        if a==u'\u51fa\u73b0\u9519\u8bef':
            return 0
        else:
            return 1
    except:
        return 0

class gettitle(HTMLParser):
    def __init__(self, raw_data):
        HTMLParser.__init__(self)
        self.flagofgettitle = 0
        self.title = []
        self.data = raw_data.decode('gbk')
        self.go()

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.flagofgettitle = 1

    def handle_data(self, data):
        if self.flagofgettitle == 1:
            self.title = data
            self.flagofgettitle = 0

    def go(self):
        self.feed(self.data)


if __name__ == "__main__":
    run(2100)
    #urlcheck("http://www.wenku8.com/book/9992.htm")
