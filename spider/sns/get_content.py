#! /usr/bin/env python
# coding: utf-8
from sentimentanalysis.mapper import analyse_sent
fp = open("contents.txt", "r")
num = 1
for line in fp:
    print num
    print line
    analyse_sent(line)
    num += 1
    print "<------->"
fp.close()