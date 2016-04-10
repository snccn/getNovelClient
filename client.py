#!/usr/bin/python2
# Coding:UTF-8
# Author:snccn

import sys,json,sqlite3,os,urlparse
import Lib.feeler,Lib.getEpubApi,Lib.getnovel,Lib.connection
import Lib.getnovel as getnov
import Lib.getPiC as getpic
ClientVersion=0.1
AVILIABLE_POOL={}
CONFIG={}
picturePool=[]
novelpoolJson=[]
picturePoolJson=[]
def loadFiles():
    global AVILIABLE_POOL,CONFIG
    configfile    =open('./Config/config.json','r').read()
    aviliablefile =open('./Config/aviliable.json','r').read()
    CONFIG        =json.JSONDecoder().decode(configfile)
    AVILIABLE_POOL=json.JSONDecoder().decode(aviliablefile) 
# first of all check if the novel id is aviliable

def checkAvlible(novelid):
    if AVILIABLE_POOL[str(novelid)]==1:
        return True
    else :
        return False

# if the novelid is aviliable now get the list of the chapter

def getChapter(novelid):
    print checkAvlible(novelid)
    if checkAvlible(novelid)==True:
        connobj=sqlite3.connect('./Data/novel.db')
        dbCursor=connobj.cursor()
        print dbCursor.execute("select novelname,charaname,charaurl from novels where novelid ="+str(novelid)+";")
        # for i,j,k in dbCursor.fetchall():
        #     print i , j ,k
        # print dbCursor.fetchall()
        index=dbCursor.fetchall()
        connobj.close()
        return index
# if we have the index of the novel why not find the novel 
def findnovel(novelid):
    global picturePool
    global novelpoolJson
    global picturePoolJson
    novelPool=[]
    a=getChapter(novelid)
    for i,j,k in a:
        if k != "NULL" and j != u"\u63d2\u56fe":            
            novelPool.append(k)
            novelpoolJson.append((i,j,k))
        elif j == u"\u63d2\u56fe":
            picturePool.append(k)
            picturePoolJson.append((i,j,k))
    # b=open('./1012.json','w').write(a)
    return novelPool
# now getthe novel and store it into txt files
def makeurlA(novelid):
    url=""
    id=str(novelid)
    if len(str(id))==4:      
        url="http://www.wenku8.com/novel/"+str(id[0])+"/"+str(id)+"/"
    else:
        url="http://www.wenku8.com/novel/"+str(0)+"/"+str(id)+"/"
    return url
def maketheURLPOOL(novelid):
    URLPOOL=[]
    URLA=makeurlA(novelid)
    for i in findnovel(novelid):         
        # print URLA+i
        URLPOOL.append(URLA+i)
        # URLPOOL.append(url)
    return URLPOOL
# now we have ALL the target URL and if i have an URL
def getNV(url,novelid):
    print novelid
    temp=getnov.chapter(url)
    filename="./Assets/"+str(novelid)+"/"+url.split('/')[-1][:-4]+".txt"
    try:
        fileobj=open(filename,'w')
        print(0)
    except Exception:
        os.mkdir("./Assets/"+str(novelid)+"/")
        fileobj=open(filename,'w')
        pass
    fileobj.write(temp.chaptername)
    for i in temp.chapter:
        fileobj.write(i)
    fileobj.close()
def getnovels(URLPOOL,novelid):
    for i in URLPOOL:
        getNV(i,novelid)
# add pictures into ./Assets/<novelid>/PICID/<PICID2>
def pictureGet(novelid):
    global picturePool
    urlA=makeurlA(novelid)
    for i in picturePool:
        url=urlA+i
        getpic.Tofile(Lib.getEpubApi.getEpub(url).docraw,"./Assets/"+str(novelid)+"/"+str(i[:-4])+"/")
def storeToJson(jsontarget):
    jsonfile=open("./Assets/"+str(novelid)+"/content.json",'w')
    jsonfile.write(jsontarget)
if __name__=="__main__":
    reload(sys)
    sys.setdefaultencoding('utf8');
    loadFiles()
    novelid0=sys.argv[-1]
    #getChapter(1012)
    #novelid0="1224"
    try:
        novelid=int(novelid0)
        getnovels(maketheURLPOOL(novelid),novelid)
        pictureGet(novelid)
    except Exception:
       print "SyntaxError"
       pass
# it is the time to add the picture support
# these are the index  of the novel value like 
    print picturePoolJson
    print novelpoolJson
    # for i in picturePool:
    #     Lib.getEpubApi.getEpub()
    jsontarget={"novelname":novelpoolJson[1][0],"chapter":novelpoolJson,"picture":picturePoolJson}
    print jsontarget
    storeToJson(json.dumps(jsontarget))
    