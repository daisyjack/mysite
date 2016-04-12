# coding: utf-8
import urllib2
import urllib
import cookielib
import re
#values = {"username":"1016903103@qq.com","password":"XXXX"}
#data = urllib.urlencode(values)
headers = {"Cookie": "_T_WM=00e82e1532da1ea90560014a419f57cb; SUB=_2A256D-BYDeRxGeRP41YW9y_Ozz2IHXVZ84AQrDV6PUJbrdAKLUbCkW1LHesTi5OCaGbN9DT99zjrVlZd8H2L4A..; gsid_CTandWM=4uHucb1c1gOXARzCFZIuB9amf3T",
           "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2587.3 Safari/537.36"}
url = "http://weibo.cn//search/mblog?hideSearchFrame=&keyword=%E6%B5%81%E6%84%9F&vt=4&page="
data = {"keyword": "流感",
        "smblog": "搜微博"}
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpsHandler, httpsHandler)
urllib2.install_opener(opener)
for page in range(1, 101):
    print page
    request = urllib2.Request(url + str(page), headers=headers)
    response = urllib2.urlopen(request)
    response = opener.open(request)
    print response.read()
