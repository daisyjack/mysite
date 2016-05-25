# coding: utf-8
import urllib2
import urllib
import cookielib
import re
from lxml import etree
from bs4 import BeautifulSoup
#from lxml.html import soupparser
#values = {"username":"1016903103@qq.com","password":"XXXX"}
#data = urllib.urlencode(values)
import xml.etree.ElementTree as ET
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        pass


def req_302(opener, request):
    try:
        response = opener.open(request)
    except urllib2.HTTPError, e:
        print e.code
        if e.code == 301 or e.code == 302:
            response = req_302(opener, request)
    return response


def get_content(html, key_empha):
    content_list = []
    html = re.sub(key_empha, r'\1', html)
    dom = etree.HTML(html)
    for item in dom.iterfind("body/div"):
        if item.get("class") == 'c' and item.get("id"):
            if len(item) == 1:
                for subitem in item.iterfind("div/span"):
                    if subitem.get("class") == "ctt":
                        content = etree.tostring(subitem, method='text', encoding='utf-8').decode("utf-8")
                        content_list.append(content)
            else:
                for subitem in item.iterfind("div"):
                    is_target = True
                    for subsubitem in subitem.iterfind("span"):
                        if subsubitem.get("class") == "ctt":
                            is_target = False
                    if is_target:
                        raw = etree.tostring(subitem, method="text", encoding="UTF-8")
                        # raw = "赞[1]赞[1]"
                        pattern = re.compile(u'(赞\[\d*\])', re.U)
                        match = re.search(pattern, raw.decode("utf-8"))
                        content = raw.decode("utf-8")[:match.start()]
                        content_list.append(content)
    return content_list


print 'please input the keyword to crwal:'
keyword = raw_input()


headers = {"Cookie": "_T_WM=c5b9d937f930cc19d8ece8707cc62fc5; SUHB=0tKbB5kAVkO6ta; SUB=_2A256NGXLDeRxGeRP41YW9y_Ozz2IHXVZ1wuDrDV6PUJbrdAKLWnHkW1LHet0aFxl2np-I74CtG58F0MB5cgB7g..; gsid_CTandWM=4uzJcb1c1QQZEsr8s74YI9amf3T; M_WEIBOCN_PARAMS=from%3Dhome",
           "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2587.3 Safari/537.36"}
data = {"keyword": keyword}
url = "http://weibo.cn/search/mblog?hideSearchFrame=&{}&page=".format(urllib.urlencode(data))
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(RedirectHandler)

key_empha = re.compile(u'<span\s*class="kt">(\w+)</span>', re.U|re.I)
#fp = open(os.path.join(BASE_DIR, "media", 'localdata', 'contents.txt'), "w")
fp = open("content.txt", 'w')
total = 0
for page in range(1, 101):
    print page
    request = urllib2.Request(url + str(page), headers=headers)
    #response = urllib2.urlopen(request)
    response = req_302(opener, request)
    html = response.read()
    #print html
    content_list = get_content(html, key_empha)
    for item in content_list:
        print item
    for content in content_list:
        fp.write(content.encode("utf-8") + "\n")
        total += 1
fp.close()
print total
# soup = BeautifulSoup(html)
# for item in soup.html.head.descendants:
#     print type(item)
#     print "<----->"
# html = '<html><body id="1">abc<div>123</div>def<div>456</div>ghi</body></html>'
# dom = etree.HTML(html)
# for item in dom[0].iterfind(""):
#     print item




