#! /usr/bin/env python
# coding: utf-8
from sentimentanalysis.mapper import analyse_sent, sub_or_ob
fp = open("contents.txt", "r")
num = 1
sub_num = 0
for line in fp:
    print num
    sub = analyse_sent(line.decode("utf-8"), u"荒野猎人")
    if sub:
        sub_num += 1
        print line
        print "<------->"
    num += 1
print "total sub num: " + str(sub_num)
fp.close()