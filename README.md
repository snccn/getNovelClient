#getNovelClient
----
##Useage
```
	python client.py <novelid>
```
##About 
* novelid 是资源的内部id 这个一般存放在 ./Config/aviliable.json 资源索引存放于 ./Data/novel.db
* 以上的两个文件是由getNovelser爬去的索引创建而成，后期会有update.py用于获取这两个文件
* 爬取到的文字将会被放置于./Assets/|novelid|/文件夹下具体
* 这个程序尚未完成以后可能会有wxpython 或者其他python图形化界面
