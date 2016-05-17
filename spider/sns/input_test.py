#! /usr/bin/env python
# coding: utf-8
import urllib
print 'please input the keyword to crwal:'
a = raw_input()
b = {'keyword': a}
c = {'data': a.decode('utf-8')}
print urllib.urlencode({"keyword": "荒野猎人"})
print urllib.urlencode(b)
print 'ee'
