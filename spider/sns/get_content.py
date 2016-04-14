#! /usr/bin/env python
# coding: utf-8
from sentimentanalysis.mapper import analyse_sent, sub_or_ob
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
#fp = open(os.path.join(BASE_DIR, "media", 'localdata', 'contents.txt'), "r")
fp = open('contents.txt', 'r')
num = 1
sub_num = 0
for line in fp:
    print num
    print line
    result = analyse_sent(line.decode("utf-8"), None)
    if result.get('sub'):
        print
        sub_num += 1

    print "<------->"
    num += 1
print "total sub num: " + str(sub_num)
fp.close()